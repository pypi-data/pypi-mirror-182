from atexit import register
from .qujam_spi_base import QujamSpiObject
from .qujam_logger import get_logger, _QujamLogger


class MetaQujamApi(type):
    objs = []

    def __call__(cls, *args, **kwargs):
        obj = super(MetaQujamApi, cls).__call__(*args, **kwargs)
        cls.objs.append(obj)
        return obj


@register
def __clear():
    for obj in MetaQujamApi.objs:
        if not obj.isStopped():
            obj.Stop()
            obj.Join()


class QujamApiObject(metaclass=MetaQujamApi):
    def __init__(self):
        self.__logger = None
        self.__logger_title = None
        self._spi = QujamSpiObject(None)

    def _set_heart_beat(self, *args, **kwargs):
        pass

    def _set_logger(self, logger=None, title=None):
        if not logger:
            logger = get_logger()
        assert isinstance(logger, _QujamLogger), "'logger' must be returned from 'get_logger' method"
        self.__logger = logger

        if title is not None:
            assert isinstance(title, str), "'title' must be a string"
            self.__logger_title = title
            return
        self.__logger_title = title

    def _get_logger(self):
        if not self.__logger:
            self._set_logger()
        return self.__logger

    def debug(self, *msgs):
        self._get_logger().debug(*msgs, title=self.__logger_title)

    def info(self, *msgs):
        self._get_logger().info(*msgs, title=self.__logger_title)

    def warning(self, *msgs):
        self._get_logger().warning(*msgs, title=self.__logger_title)

    def error(self, *msgs):
        self._get_logger().error(*msgs, title=self.__logger_title)

    def critical(self, *msgs):
        self._get_logger().critical(*msgs, title=self.__logger_title)

    def _stop(self):
        self._spi.clear()

    def _join(self, wait: float = None):
        pass
