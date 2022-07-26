import unittest
import autoloader  # pylint: disable=unused-import

import json

from datetime import datetime

from scratchpad.logger import Logger
from scratchpad.composite_logger import CompositeLogger
from scratchpad.console_logger import ConsoleLogger
from scratchpad.file_logger import FileLogger
from scratchpad.fluent_logger import FluentLogger
from scratchpad.jandi_logger import JandiLogger
from scratchpad.line_logger import LineLogger
from scratchpad.memory_logger import MemoryLogger
from scratchpad.null_logger import NullLogger
from scratchpad.scribe_logger import ScribeLogger
from scratchpad.telegram_logger import TelegramLogger


class TestLogger(unittest.TestCase):
    def testSetLogger(self):

        #given
        nullLogger = NullLogger()

        #when
        Logger.setLogger(nullLogger)
        
        #then
        self.assertEqual(Logger.getLogger(), nullLogger)


    def testFileLogger(self):
        #given
        filePath = "/tmp/scratch-pad-py.log"
        logger = FileLogger(
            config={
                "filePath": filePath,
                "truncate": True
            }
        )
        message = {
            "type": "file",
            "message": "hello world"
        }

        #when
        logger.info(message)

        #then
        with open(filePath, "r", encoding="utf-8") as file:
            line = file.readline()
            self.assertEqual('{"level": "info", "type": "file", "message": "hello world"}\n', line)


    def testCompositeLogger(self):
        #given
        consoleLogger = ConsoleLogger(
                config={
                "appendNewLine": 1
            }
        )
        memoryLogger = MemoryLogger()
        memoryLoggerCompositeFilter = CompositeLogger.getSelectorLevel(["info", "error"])

        message = {
            "type": "composite",
            "message": "hello world"
        }

        compositLogger = CompositeLogger(
            config={
                "defaults": {
                    "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "program": "scratch-pad-python",
                },
                "loggerFilterPairs": [
                    {
                        "logger": consoleLogger,
                        "filter": None
                    },
                    {
                        "logger": memoryLogger,
                        "filter": memoryLoggerCompositeFilter
                    }
                ],
            }
        )

        #when
        compositLogger.info(message)
        compositLogger.notice(message) 

        #then
        logs: list = memoryLogger.getInMomory()
        self.assertEqual(1, len(logs))

        log: dict = logs[0]
        self.assertEqual("notice", log["level"])


    def testJandiLogger(self):
        #given 
        url = "url"
        logger = JandiLogger(
            url=url
        )

        #when
        message = {
            "type": "jandi",
            "message": "hello world"
        }

        #then
        logger.info(message)


    def testScribeLogger(self):
        #given 
        logger = ScribeLogger()

        #when
        message = {
            "type": "scribe",
            "message": "hello world"
        }

        #then
        logger.info(message)

    def testLineLogger(self):
        #given
        token = "token"

        message = {
            "type": "line",
            "message": "hello world"
        }

        #when
        logger = LineLogger(
            token=token
        )

        #then
        logger.info(message)


    def testTelegramLogger(self):
        #given
        token = "telegram"
        chat_id = 1234
        

        message = {
            "type": "telegram",
            "message": "hello world",
        }

        #when
        logger = TelegramLogger(
            chat_id=chat_id,
            token=token,
        )

        #then
        logger.info(message)


    def testFluentLogger(self):
        #given
        logger = FluentLogger()
        message = {
                "type": "fluent",
                "message": "hello world"
            }

        #when
        logger.info(message)