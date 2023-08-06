from ..protobuf_wrapper import ProtoWrapper
from ..configurator_handles import DefaultConfigHandle


class MetaConfigurator(type):
    def __call__(cls, *args, **kwargs):
        obj = super(MetaConfigurator, cls).__call__(*args, **kwargs)
        obj._cfg_handles = (DefaultConfigHandle(),)
        return obj


class ConfiguratorBase(metaclass=MetaConfigurator):
    def ToProto(self, pyobj, pbobj):
        handles = getattr(self, "_cfg_handles")
        for handle in handles:
            pyobj, pbobj = handle.PreToProto(pyobj, pbobj)
        pbobj = self.to_proto(pyobj, pbobj)
        for handle in handles:
            pbobj = handle.PostToProto(pbobj)
        return pbobj

    def ToPyobj(self, pbobj, pyobj):
        handles = getattr(self, "_cfg_handles")
        for handle in handles:
            pbobj, pyobj = handle.PreToPyobj(pbobj, pyobj)

        pyobj = self.to_pyobj(pbobj, pyobj)
        for handle in handles:
            pyobj = handle.PostToPyobj(pyobj)
        return pyobj

    def SetCfgHandle(self, *handles):
        if handles:
            setattr(self, "_cfg_handles", getattr(self, "_cfg_handles") + handles)
        return self

    def to_proto(self, pyobj, pbobj: ProtoWrapper):
        raise NotImplementedError

    def to_pyobj(self, pbobj: ProtoWrapper, pyobj):
        raise NotImplementedError

    def get_attrs(self):
        raise NotImplementedError
