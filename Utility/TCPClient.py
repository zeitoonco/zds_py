# coding=utf-8
import Queue
import logging
import struct
import sys
import threading
import traceback
from threading import Thread

from twisted.internet import reactor, task
from twisted.internet.protocol import Protocol, ReconnectingClientFactory

logger = logging.getLogger(__name__)


class TCPClientProtocol(object, Protocol):
    qthread = None  # type: Thread
    send_is_busy = False

    dataQ_Pops = 0
    dataQ_Pushes = 0
    lastDataQSize = 0
    check2 = 0
    __stopDataProcess = True
    __stopSendProcess = True

    logger = logging.getLogger('TCPClientProtocol')

    sentinel = None
    TaskDispatcherQueue = Queue.Queue()
    num_threads = 5

    _buff = None
    _lastPacketLen = 0

    def TaskDispatcher(self, queue):
        while True:
            n = queue.get()
            self.logger.info('task called: {n}'.format(n=n))
            if n is self.sentinel:
                break
            if hasattr(TCPClientCallBackHolder.MessageCallBack, '__call__'):
                TCPClientCallBackHolder.safe_caller(TCPClientCallBackHolder.MessageCallBack, n)
            queue.task_done()

    def TaskDispatcherSetup(self):
        threads = [threading.Thread(target=self.TaskDispatcher, args=(self.TaskDispatcherQueue,))
                   for n in range(self.num_threads)]
        for t in threads:
            t.start()

    def Join(self):
        """
            Join Running Threads
        """
        for t in self.threads:
            t.Join()
        self.logger.info("Dispatcher threads are closed")

    def __init__(self):
        super(TCPClientProtocol, self).__init__()
        self.TaskDispatcherSetup()
        self.startSendProcess()

    def startSendProcess(self):
        self.lc = task.LoopingCall(self.sendProcessor)
        self.lc.start(0.15)

    def sendProcessor(self):
        if self.send_is_busy or self.transport is None:
            return
        try:
            data = TCPClient.pendingBuffs.get_nowait()
            if data:
                data = data.encode('utf-8')
                signature = (chr(12) + chr(26) + struct.pack("L", long(len(data))))
                self.send_is_busy = True
                self.transport.write(signature + data)
                self.send_is_busy = False
        except Exception, e:
            self.send_is_busy = False
            pass

    def dataReceived(self, data):
        nread = len(data)
        if nread < 0:
            self.logger.error("Client read ERR ")

        if nread == 0:
            self.logger.error("TCPClient: read 0!")
        else:
            ci = 0
            while ci < nread:
                if (nread - ci) > 6 and ord(data[ci + 0]) == 12 and ord(data[ci + 1]) == 26:  # New packet
                    size = struct.unpack("L", data[ci + 2:ci + 6])[0]
                    ci += 6
                    if (ci + size) <= nread:  # its whole
                        self._buff = data[ci:ci + size]
                        self._packetReceived()
                        ci += size
                    else:  # part of packet
                        self._lastPacketLen = size
                        self._buff = data[ci:]
                        ci = nread  # fin.
                elif ci == 0 and self._lastPacketLen > 0:  # Next part of last packet
                    rem = (self._lastPacketLen - len(self._buff))
                    if rem <= nread:  # packet complated
                        self._buff += data[:rem]
                        self._packetReceived()
                        ci += rem
                else:  # another part
                    self._buff += data
                    ci = nread  # fin.

    def dataProcessor(self):
        pass

    def _packetReceived(self):
        if TCPClientCallBackHolder.MessageCallBack is not None:
            self.TaskDispatcherQueue.put(self._buff)

        self._buff = ""
        self._lastPacketLen = 0


class TCPClientFactory(ReconnectingClientFactory):
    logger = logging.getLogger('TCPClientFactory')

    def __init__(self):
        pass

    def startedConnecting(self, connector):
        self.logger.info('Started to connect.')

    def buildProtocol(self, addr):
        TCPClient.connected = True
        TCPClientCallBackHolder.safe_caller(TCPClientCallBackHolder.ClientConnectCallBack)
        self.logger.info('Connected.')
        return TCPClientProtocol()

    def clientConnectionLost(self, connector, reason):
        TCPClient.connected = False
        TCPClientCallBackHolder.safe_caller(TCPClientCallBackHolder.ClientDisconnectCallBack)
        self.logger.error('Lost connection. Reason: ' + reason.getErrorMessage())
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        TCPClient.connected = False
        self.logger.error('Connection failed. Reason: ' + reason.getErrorMessage())
        ReconnectingClientFactory.clientConnectionFailed(self, connector, reason)


class TCPClientCallBackHolder:
    MessageCallBack = None
    ClientConnectCallBack = None
    ClientDisconnectCallBack = None
    logger = logging.getLogger('TCPClientCallBackHolder')

    @staticmethod
    def safe_caller(method, data=None):
        try:
            if data is None:
                method()
            else:
                method(data)
        except Exception, e:
            ex_type, ex, tb = sys.exc_info()
            traceback.print_tb(tb)
            TCPClientCallBackHolder.logger.error("Error in %s %s" % (str(method), str(e)))


class TCPClient:
    logger = logging.getLogger('TCPClient')
    thread = None  # type: Thread
    pendingBuffs = Queue.Queue()
    _connector = None
    connected = False

    def __init__(self):
        pass

    def Connect(self, ip, port):
        self._connector = reactor.connectTCP(ip, port, TCPClientFactory())

    def Run(self):
        self.thread = Thread(target=reactor.run, args=(False,))
        self.thread.start()

    def Join(self):
        self.thread.join()

    def Disconnect(self):
        self._connector.disconnect()

    def registerOnMessageCallBack(self, data_received):
        TCPClientCallBackHolder.MessageCallBack = data_received

    def registerOnClientConnectCallBack(self, on_net_connect):
        TCPClientCallBackHolder.ClientConnectCallBack = on_net_connect

    def registerOnClientDisconnectCallBack(self, on_net_disconnect):
        TCPClientCallBackHolder.ClientDisconnectCallBack = on_net_disconnect

    def send(self, data):
        print data
        TCPClient.pendingBuffs.put(data)

    def isConnected(self):
        return TCPClient.connected
