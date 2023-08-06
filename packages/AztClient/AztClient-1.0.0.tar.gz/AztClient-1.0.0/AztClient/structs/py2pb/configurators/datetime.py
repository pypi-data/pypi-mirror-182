import datetime

from .base import ConfiguratorBase, ProtoWrapper


class DatetimeConfigurator(ConfiguratorBase):
    def __init__(self, **dtformat):
        self._format = dtformat
        self._attrs = tuple(self._format.keys())

    def to_proto(self, pyobj, pbobj: ProtoWrapper):
        for _attr, formator in self._format.items():
            if pbobj.hasattr(_attr):
                val = getattr(pyobj, _attr)
                if not val:
                    continue
                if isinstance(formator, str):
                    dtval = val.strftime(formator)
                    pbobj.setattr(_attr, dtval)
                elif formator is None or isinstance(formator, datetime.tzinfo):
                    dtval = val.timestamp()
                    pbobj.setattr(_attr, dtval)
        return pbobj

    def to_pyobj(self, pbobj: ProtoWrapper, pyobj):
        for _attr, formator in self._format.items():
            val = pbobj.getattr(_attr, None)
            if val is not None:
                if isinstance(val, (int, float)):
                    dt = datetime.datetime.fromtimestamp(val)
                    setattr(pyobj, _attr, dt)
                elif isinstance(val, str) and val:
                    dt = datetime.datetime.strptime(val, formator)
                    setattr(pyobj, _attr, dt)
        return pyobj

    def get_attrs(self):
        return self._attrs
