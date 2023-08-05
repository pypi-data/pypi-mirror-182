try:
    from .. import Http
    from .. import Base64
    from .. import Lg
except:
    import sys
    sys.path.append("..")
    import Http
    import Base64
    import Lg

import typing
import pickle

class queueQueueConfirm():
    def __init__(self, server:str, name:str, length:int=0, timeout:int=300) -> None:
        self.server = server 
        self.name = name 
        Http.PostForm(self.server + "/new", {"qname": "test", "length": length, "timeout": timeout})
    
    def Put(self, item:typing.Any, force:bool=False):
        Http.PostForm(self.server + "/put", {"qname": "test", "value": Base64.Encode(pickle.dumps(item, 2)), "force": str(force)})

    def Get(self) -> typing.Tuple[str, typing.Any]:
        res = Http.Get(self.server + "/get", {"qname": "test"}, Timeout=900)
        Lg.Trace(res)

        tid = res.Headers["Tid"]
        value = pickle.loads(Base64.Decode(res.Content))

        return tid, value 
    
    def Done(self, tid:str):
        Http.Get(self.server + "/done", {"qname": "test", "tid": tid})
    
    def Size(self) -> int:
        res = Http.Get(self.server + "/size", {"qname": "test"})
        return int(res.Content)

class Queue():
    def __init__(self, server:str) -> None:
        self.server = server 
    
    def QueueConfirm(self, name:str, length:int=0, timeout:int=300) -> queueQueueConfirm:
        return queueQueueConfirm(self.server, name, length, timeout)

if __name__ == "__main__":
    qs = Queue("http://192.168.1.230:8080")
    qt = qs.QueueConfirm("test", 100, 10)
    Lg.Trace("put value")
    qt.Put({1:2})
    for i in range(10):
        Lg.Trace("Get value")
        res = qt.Get()
        tid, value = res
        Lg.Trace(res)
        size = qt.Size()
        Lg.Trace(size)
        qt.Done(tid)