from .base_pyhandle import PyHandleBase
from ..tools import get_dataclass_attrs


class PyReprHandle(PyHandleBase):
    def __init__(self):
        self._pyattrs = None
        self._get_pyattr_map = dict()

    def Handle(self, pycls):
        self._pyattrs = get_dataclass_attrs(pycls)
        if self._pyattrs:
            self._init_pyattr_map()
            setattr(pycls, "__repr__", lambda x: self.repr(x))
        return pycls

    def repr(self, obj):
        return f"{obj.__class__.__qualname__}({self._repr(obj)})"

    def _repr(self, obj):
        return ', '.join([f"{attr}={_getattr(obj, attr)}" for attr, _getattr in self._get_pyattr_map.items()])

    def _init_pyattr_map(self):
        for pyattr in self._pyattrs:
            self._get_pyattr_map[pyattr] = getattr
