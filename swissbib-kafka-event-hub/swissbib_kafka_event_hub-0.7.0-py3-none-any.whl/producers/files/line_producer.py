from kafka_event_hub.producers.base_producer import AbstractBaseProducer
from kafka_event_hub.config import BaseConfig


class LineProducer(AbstractBaseProducer):

    def __init__(self, config: str):
        super().__init__(config, config_parser=BaseConfig)
        self.count = 0

    def process(self):
        with open(self.configuration['path'], 'r') as fp:
            for line in fp:
                self._produce_kafka_message("{}".format(self.count), line.strip())   
                self.count += 1
                self._poll(0)

                
        self._flush()
