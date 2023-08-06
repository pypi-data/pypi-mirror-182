from ..convertor import ToPyobj, ToProto
from .base import ConfiguratorBase


class RepeatConfigurator(ConfiguratorBase):
    def get_attrs(self):
        return self._attrs

    def __init__(self, *attrs, recur=False):
        self._attrs = attrs
        self._recur = recur

    def to_proto(self, pyobj, pbobj):
        for _attr in self._attrs:
            rep = pbobj.getattr(_attr, None)
            if rep is not None:
                val = getattr(pyobj, _attr)
                if val is None:
                    continue
                if self._recur:
                    rep.extend(list(map(ToProto, val)))
                    continue
                rep.extend(val)
        return pbobj

    def to_pyobj(self, pbobj, pyobj):
        for _attr in self._attrs:
            rep = pbobj.getattr(_attr, None)
            if rep is not None:
                if self._recur:
                    setattr(pyobj, _attr, list(map(ToPyobj, rep)))
                    continue
                setattr(pyobj, _attr, rep)
        return pyobj
