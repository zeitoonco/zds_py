import ServerMediator
from HelloWorldCHI import HelloWorld
from Utility.log import setup_logging

if __name__ == '__main__':
    setup_logging()
    chi = HelloWorld(ServerMediator.ServerMediator)
    chi.connect("127.0.0.1", 9666)
    chi.sm.joinNet()
