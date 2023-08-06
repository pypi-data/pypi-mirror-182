import threading
from threading import Thread
from traceback import format_exc
import warnings


class QujamThreadWarning(UserWarning):
    pass


class QujamThread(Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None, _warning=False) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self._exception = None
        self._exc_traceback = ''
        self._enable_warning = _warning

    def run(self) -> None:
        try:
            super().run()
        except Exception as exc:
            self._exception = exc
            self._exc_traceback = format_exc()
            if self._enable_warning:
                exc_warning = f"Execption happened in {self.getName()}:\n{self._exc_traceback}"
                warnings.warn(exc_warning, category=QujamThreadWarning)

    def has_exception(self) -> bool:
        return not not self._exception

    def get_exception(self) -> Exception:
        return self._exception

    def exception_traceback(self) -> str:
        return self._exc_traceback

    def joinable(self):
        if threading.current_thread() is self:
            return False
        return True
