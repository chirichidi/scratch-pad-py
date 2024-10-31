import unittest
from time import sleep

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
from scratchpad.slack_logger import SlackLogger


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
        memoryLoggerCompositeFilter = CompositeLogger.getSelectorLevel(["notice", "error"])

        
        compositLogger = CompositeLogger(
            config={
                "defaults": {
                    "datetime": lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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
        compositLogger.info(message = {
            "type": "composite",
            "message": "hello world",
            "aa": 123
        })
        sleep(2)
        compositLogger.notice(message = {
            "type": "composite",
            "message": "hello world",
            "bb": 12345
        }) 

        #then
        logs: list = memoryLogger.getInMomory()
        self.assertEqual(1, len(logs))

        log: dict = logs[0]
        self.assertEqual("notice", log["level"])


    def testJandiLogger(self):
        #given 
        url = "url"
        logger = JandiLogger(
            url=url,
        )

        #when
        message = {
            "type": "jandi",
            "message": "hello world"
        }

        #then
        logger.info(message)

    def testJandiLoggerWithBodyStyle(self):
        #given 
        url = "url"
        logger = JandiLogger(
            url=url,
            config={
                "headers": {"Content-Type": "application/json", "Accept": "application/vnd.tosslab.jandi-v2+json"},
            }
        )

        #when
        message = {
            "type": "jandi",
            "message": "hello world"
        }
        option = {
            "connectColor": "#FAC11B",
            "connectInfo": [{"title": "connectInfo TITLE", "description": "connectInfo description"}]
        }
        
        #then
        logger.info(message, option)

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
        
    def testSlackLogger(self):
        #given
        url = "https://hooks.slack.com/services/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"
        channel = "#slack_test"
        message = {
            "type": "slack",
            "message": "hello world"
        }

        # when

        # no channel
        logger = SlackLogger(url=url)
        logger.info(message)

        # with channel
        logger = SlackLogger(url=url, channel=channel)
        logger.info(message)