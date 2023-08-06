import json
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer, TopicPartition
from scan.common import logger


class Kafka:

    def __init__(self, bootstrap_servers, security_protocol='PLAINTEXT',
                 ssl_context=None, user=None, password=None):
        self.bootstrap_servers = bootstrap_servers
        self.user = user
        self.password = password
        self.ssl_context = ssl_context
        self.security_protocol = security_protocol

    async def producer(self, topic, gen_func):
        """
        :param topic:
        :param gen_func:  generator func
        :return:
        """
        _producer = AIOKafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            security_protocol=self.security_protocol,
            ssl_context=self.ssl_context,
            sasl_plain_username=self.user,
            sasl_plain_password=self.password
        )
        await _producer.start()
        try:
            data = gen_func()
            async for d in data:
                if not isinstance(d, str):
                    d = json.dumps(d)
                await _producer.send_and_wait(topic, d.encode())
                logger.info(f'send data: {d}')
        except Exception as e:
            logger.error(f'producer error:{e}')
        finally:
            await _producer.stop()

    async def send_one(self, topic, message):
        """
        :param topic:
        :param message:
        :return:
        """
        _producer = AIOKafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            security_protocol=self.security_protocol,
            ssl_context=self.ssl_context,
            sasl_plain_username=self.user,
            sasl_plain_password=self.password
        )
        await _producer.start()
        try:
            if isinstance(message, dict):
                message = json.dumps(message)
            await _producer.send_and_wait(topic, message.encode())
        except Exception as e:
            logger.error(f'producer error:{e}')
        finally:
            await _producer.stop()

    async def consumer(self, call_back, topic, group_id='hscan'):
        """
        :param call_back: async func
        :param topic:
        :param group_id:
        :return:
        """
        try:
            _consumer = AIOKafkaConsumer(
                topic,
                bootstrap_servers=self.bootstrap_servers,
                group_id=group_id,
                enable_auto_commit=False,
                sasl_plain_username=self.user,
                sasl_plain_password=self.password
            )
            await _consumer.start()
            try:
                while 1:
                    # msg = await _consumer.getone()
                    # if not msg:
                    #     continue
                    # data = json.loads(msg.value)
                    # res = await call_back(data)
                    # if res:
                    #     tp = TopicPartition(msg.topic, msg.partition)
                    #     await _consumer.commit({tp: msg.offset + 1})
                    async for msg in _consumer:
                        data = json.loads(msg.value)
                        res = await call_back(data)
                        if res:
                            tp = TopicPartition(msg.topic, msg.partition)
                            await _consumer.commit({tp: msg.offset + 1})
            finally:
                await _consumer.stop()
        except Exception as e:
            logger.error(f'consumer error:{e}')
