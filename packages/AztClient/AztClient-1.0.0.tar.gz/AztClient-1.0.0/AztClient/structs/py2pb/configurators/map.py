from ..convertor import ToPyobj, ToProto
from .base import ConfiguratorBase


class MapConfigurator(ConfiguratorBase):
    def get_attrs(self):
        return self._attrs

    def __init__(self, *attrs, recur=False):
        self._attrs = attrs
        self._recur = recur

    def to_proto(self, pyobj, pbobj):
        for _attr in self._attrs:
            _map = pbobj.getattr(_attr, None)
            if _map is not None:
                pyval = getattr(pyobj, _attr)
                if pyval is None:
                    continue
                if self._recur:
                    for _key, _val in pyval.items():
                        _map[_key] = ToProto(_val)
                    continue
                for _key, _val in pyval.items():
                    _map[_key] = _val
        return pbobj

    def to_pyobj(self, pbobj, pyobj):
        for _attr in self._attrs:
            _map = pbobj.getattr(_attr, None)
            if _map is not None:
                if self._recur:
                    setattr(pyobj, _attr, {_key: ToPyobj(_val) for _key, _val in _map.items()})
                    continue
                setattr(pyobj, _attr, _map)
        return pyobj
