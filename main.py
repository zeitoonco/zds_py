import ServerMediator
from AccountingRelay import AccountingRelay
from Utility.log import setup_logging

if __name__ == '__main__':
    setup_logging()
    chi = AccountingRelay(ServerMediator.ServerMediator)
    chi.connect("138.201.152.83", 5458)
    chi.sm.joinNet()
