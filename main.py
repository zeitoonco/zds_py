import ServerMediator
from HelloWorldCHI import HelloWorld
from Utility.log import setup_logging

if __name__ == '__main__':
    setup_logging()
    chi = HelloWorld(ServerMediator.ServerMediator)
    chi.connect("138.201.152.83", 5458)
    chi.sm.joinNet()
