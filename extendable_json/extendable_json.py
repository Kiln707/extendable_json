import json as j
from . import  json_serialize, json_deserialize

class _JSONEncoder(j.JSONEncoder):
    def default(self, obj):
        for type_, handler in json_serialize.registry.items():
            if isinstance(obj, type_) and type_ is not object:
                return handler(obj)
            return super(_JSONEncoder, self).default(obj)

class _JSONDecoder(j.JSONDecoder):
    def __init__(self, *args, **kwargs):
        j.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        for type_, handler in json_deserialize.registry.items():
            try:
                o = handler(obj)
                if o and isinstance(o, type_):
                    return o
            except:
                pass
        return obj

def dump(*args, cls=_JSONEncoder, **kwargs):
    return j.dump(*args, cls=cls, **kwargs)

def dumps(*args, cls=_JSONEncoder, **kwargs):
    return j.dumps(*args, cls=cls, **kwargs)

def load(*args, cls=_JSONDecoder, **kwargs):
    return j.load(*args, cls=cls, **kwargs)

def loads(*args, cls=_JSONDecoder, **kwargs):
    return j.loads(*args, cls=cls, **kwargs)
