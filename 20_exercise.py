import structlog

logger = structlog.get_logger()
logger.msg("greeted", whom="world", more_than_a_string=[1, 2, 3])


class structlog:

    instances = 0
    def get_logger(self):
        if self.instances == 1:
            return self
