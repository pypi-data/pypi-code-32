from thespian.actors import *

class Hello(Actor):
    def receiveMessage(self, message, sender):
        self.send(sender, 'Hello, world!')

class SimpleSourceAuthority(Actor):
    def receiveMessage(self, msg, sender):
        if msg is True:
            self.registerSourceAuthority()
            self.send(sender, "Registered")
        if isinstance(msg, ValidateSource):
            self.send(sender,
                      ValidatedSource(msg.sourceHash,
                                      msg.sourceData,
                                      # Thespian pre 3.2.0 has no sourceInfo
                                      getattr(msg, 'sourceInfo', None)))

def zipMyself():
    zipname = 'hi.zip'
    import zipfile
    zf = zipfile.ZipFile(zipname, 'w')
    zf.writestr('hi.py', open('hi.py', 'r').read())
    zf.close()
    return zipname

def say_hello():
    actorSys = ActorSystem("multiprocTCPBase")
    try:
        sa = actorSys.createActor(SimpleSourceAuthority)
        print("Source authority", end=" ")
        print(actorSys.ask(sa, True, 1.5))
        loadHash = actorSys.loadActorSource(zipMyself())  #(ref:loadSource)
        hello = actorSys.createActor('hi.Hello',
                                     sourceHash = loadHash)  #(ref:hashCreate)
        print(actorSys.ask(hello, 'are you there?', 1.5))
        actorSys.tell(hello, ActorExitRequest)
    finally:
        actorSys.shutdown()

if __name__ == "__main__":
    say_hello()
