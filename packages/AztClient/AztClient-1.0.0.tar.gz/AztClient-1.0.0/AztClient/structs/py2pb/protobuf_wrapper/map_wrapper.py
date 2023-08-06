from ..tools import get_protoclass_attrs
from .wrapper_base import ProtoWrapperBase


# 映射封装
class ProtoMapWrapper(ProtoWrapperBase):
    def __init__(self, proto, attrs_map):
        super(ProtoMapWrapper, self).__init__(proto)
        protoattrs = get_protoclass_attrs(proto, wrap=True)
        self._attrs_map = dict(zip(protoattrs, protoattrs))
        self._attrs_map.update(attrs_map)

    def _get_attr_name(self, item):
        return self._attrs_map.get(item)

    def getattr(self, item, default=None, _raise=False):
        if _raise:
            return getattr(self._proto, self._get_attr_name(item))
        return getattr(self._proto, self._get_attr_name(item), default)

    def setattr(self, key, value):
        setattr(self._proto, self._get_attr_name(key), value)

    def hasattr(self, item):
        return hasattr(self._proto, self._get_attr_name(item))
