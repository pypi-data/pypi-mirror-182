class ProtoWrapperBase:
    def __init__(self, proto):
        if isinstance(proto, ProtoWrapperBase):
            self._proto = proto.getproto()
            return
        self._proto = proto

    def getattr(self, item, default=None, _raise=False):
        raise NotImplementedError

    def setattr(self, key, value):
        raise NotImplementedError

    def hasattr(self, item):
        raise NotImplementedError

    def getproto(self):
        return self._proto


# 简单封装
class ProtoWrapper(ProtoWrapperBase):
    def getattr(self, item, default=None, _raise=False):
        if _raise:
            return getattr(self._proto, item)
        return getattr(self._proto, item, default)

    def setattr(self, key, value):
        setattr(self._proto, key, value)

    def hasattr(self, item):
        return hasattr(self._proto, item)