#https://stackoverflow.com/questions/10413052/is-there-a-way-to-step-into-decorated-functions-skipping-decorator-code
# magic_decorator.py
import bdb

oldBdp = bdb.Bdb


class DontDebugMeBdb(bdb.Bdb):
    @classmethod
    def __init__(cls, *args, **kwargs):
        if 'skip' not in kwargs or kwargs['skip'] is None:
            kwargs['skip'] = []
        kwargs['skip'].append(__name__)
        oldBdp.__init__(*args, **kwargs)

    @staticmethod
    def reset(*args, **kwargs):
        import bdb
        oldBdp.reset(*args, **kwargs)



bdb.Bdb = DontDebugMeBdb


def noDebuggingDecorator(func):
    "you should not ever see this message"
    def decorated(*args, **kargs):
        return func(*args, **kargs)
    return decorated
    
