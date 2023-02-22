from .logger_impl import LoggerImpl

from thrift import Thrift                                                                              
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from scribe import scribe

import json


class ScribeLogger(LoggerImpl):

    client: scribe = None

    def __init__(self, config: dict = None):
        if config is None:
            config = {}

        if "host" not in config:
            config["host"] = "localhost"
        
        if "port" not in config:
            config["port"] = 1463

        if "category" not in config:
            config["category"] = "scratch-pad-python"

        self.config = config


    def log(self, message: dict, option: dict = None):
        if option is None:
            option = {}
        if self.client is None:
            
            self.socktransport = TSocket.TSocket(self.config["host"], self.config["port"])
            self.socktransport.setTimeout(1000)

            self.transport = TTransport.TFramedTransport(self.socktransport)
            self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
            self.client = scribe.Client(self.protocol)

        try:
            if not self.transport.isOpen():
                self.transport.open()
            le = scribe.LogEntry(category=self.config['category'],message=json.dumps(message))
            self.client.Log([le])
        except Thrift.TException as tx:
            self.transport.close()
            print(tx.message)
    

    def __del__(self):
        try:
            self.transport.close()
            self.client = None
        except:
            pass