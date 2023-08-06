from ..tools import get_dataclass_attrs
from ..convertor import ToPyobj, ToProto, SetAutoConfigurator
from .base import ConfiguratorBase


class CopyConfigurator(ConfiguratorBase):
    def get_attrs(self):
        return self._attrs

    def __init__(self, *attrs, recur=False):
        self._attrs = attrs
        self._recur = recur

    def to_proto(self, pyobj, pbobj):
        if not self._attrs:
            self._attrs = get_dataclass_attrs(pyobj)
        if self._recur:
            for _attr in self._attrs:
                if pbobj.hasattr(_attr):
                    val = getattr(pyobj, _attr)
                    if val is None:
                        continue
                    pbobj.getattr(_attr, _raise=True).MergeFrom(ToProto(val))
            return pbobj
        for _attr in self._attrs:
            if pbobj.hasattr(_attr):
                val = getattr(pyobj, _attr)
                if val is None:
                    continue
                pbobj.setattr(_attr, val)
        return pbobj

    def to_pyobj(self, pbobj, pyobj):
        if not self._attrs:
            self._attrs = get_dataclass_attrs(pyobj)
        if self._recur:
            for _attr in self._attrs:
                val = pbobj.getattr(_attr, None)
                if val is not None:
                    setattr(pyobj, _attr, ToPyobj(val))
            return pyobj
        for _attr in self._attrs:
            val = pbobj.getattr(_attr, None)
            if val is not None:
                setattr(pyobj, _attr, val)
        return pyobj


SetAutoConfigurator(CopyConfigurator)
