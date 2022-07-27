# scratch-pad-py

## Projects that have been ported below.
https://github.com/polonaiz/scratch-pad


mind blowing python toolset. why not pr?


# Spec

Loggers: composite, console, file, fluent, jandi, line, memory, null, scribe, telegram



# Logger interface
```
from .logger_interface import LoggerInterface

class Logger(LoggerInterface):
    logger: LoggerInterface = None

    @classmethod
    def setLogger(cls, logger: LoggerInterface):
        cls.logger = logger

    @classmethod
    def getLogger(cls) -> LoggerInterface:
        return cls.logger

    @classmethod
    def info(cls, message: dict, option: dict = {}):
        cls.logger.info(message, option)

    @classmethod
    def notice(cls, message: dict, option: dict = {}):
        cls.logger.notice(message, option)

    @classmethod
    def warning(cls, message: dict, option: dict = {}):
        cls.logger.warning(message, option)

    @classmethod
    def error(cls, message: dict, option: dict = {}):
        cls.logger.error(message, option)

    @classmethod
    def critical(cls, message: dict, option: dict = {}):
        cls.logger.critical(message, option)
```



# Usage
FileLogger
```
filePath = "/tmp/scratch-pad-python.log"
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
logger.info(message)
```
CompositeLogger
```
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

compositLogger.info(message)
```

JandiLogger
```
url = "url"
logger = JandiLogger(
    url=url
)

message = {
    "type": "jandi",
    "message": "hello world"
}

logger.info(message)
```

TelegramLogger
```
token = "telegram"
chat_id = 1234

message = {
    "type": "telegram",
    "message": "hello world",
}

logger = TelegramLogger(
    chat_id=chat_id,
    token=token,
)

logger.info(message)
```

FluentLogger
```
logger = FluentLogger()
message = {
        "type": "fluent",
        "message": "hello world"
    }

logger.info(message)
```

#
stuff) 


scribe-docker for ScribeLogger : https://hub.docker.com/r/polonaiz/facebook-scribe


fluent-docker for FluentLogger : https://github.com/chirichidi/fluent-docker/tree/main
