from ..protobuf_wrapper import ProtoWrapper


class ConfigHandleBase:
    def PreToProto(self, pyobj, pbobj):
        raise NotImplementedError

    def PostToProto(self, pbobj):
        raise NotImplementedError

    def PreToPyobj(self, pbobj, pyobj):
        raise NotImplementedError

    def PostToPyobj(self, pyobj):
        raise NotImplementedError


class DefaultConfigHandle(ConfigHandleBase):
    def PreToProto(self, pyobj, pbobj):
        return pyobj, ProtoWrapper(pbobj)

    def PostToProto(self, pbobj):
        if hasattr(pbobj, "getproto"):
            return pbobj.getproto()
        return pbobj

    def PreToPyobj(self, pbobj, pyobj):
        return ProtoWrapper(pbobj), pyobj

    def PostToPyobj(self, pyobj):
        return pyobj
