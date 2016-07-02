# coding=utf-8
import Queue
import logging
import random
import threading
from sys import stdout
from threading import Thread

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ReconnectingClientFactory


class TCPClientProtocol(Protocol):
    qthread = None  # type: Thread
    send_is_busy = False

    dataQ_Pops = 0
    dataQ_Pushes = 0
    lastDataQSize = 0
    check2 = 0
    __stopDataProcess = True
    __stopSendProcess = True

    logger = logging.getLogger(__name__)

    sentinel = None
    TaskDispatcherQueue = Queue.Queue()
    num_threads = 5

    def TaskDispatcher(self, queue):
        while True:
            n = queue.get()
            self.logger.info('task called: {n}'.format(n=n))
            if n is self.sentinel: break
            n = random.random()
            if n > .25:
                self.logger.info("task appended to dispatcher queue")
                queue.put(n)
            queue.task_done()

    def TaskDispatcherSetup(self):
        for i in range(self.num_threads):
            self.TaskDispatcherQueue.put(i)

        threads = [threading.Thread(target=self.TaskDispacher, args=(self.TaskDispatcherQueue,))
                   for n in range(self.num_threads)]
        for t in threads:
            t.start()

        self.TaskDispatcherQueue.join()
        for i in range(self.num_threads):
            self.TaskDispatcherQueue.put(self.sentinel)

    def Join(self):
        """
            Join Running Threads
        """
        for t in self.threads:
            t.join()
        self.logger.info("Dispatcher threads are closed")

    def __init__(self):
        pass

    def dataReceived(self, data):
        stdout.write(data)

    def dataProcessor(self):
        pass


class TCPClientFactory(ReconnectingClientFactory):
    def __init__(self):
        pass

    def startedConnecting(self, connector):
        print 'Started to connect.'

    def buildProtocol(self, addr):
        print 'Connected.'
        return TCPClientProtocol()

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection.  Reason:', reason
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason
        ReconnectingClientFactory.clientConnectionFailed(self, connector, reason)


class TCPClientCallBackHolder:
    MessageCallBack = None
    ClientConnectCallBack = None
    ClientDisconnectCallBack = None

    @staticmethod
    def safe_caller(method, data=None):
        if data is None:
            try:
                method()
            except:
                print "Error"
        else:
            try:
                method(data)
            except:
                print "Error"


class TCPClient:
    thread = None  # type: Thread

    def __init__(self):
        pass

    def connect(self, ip, port):
        reactor.connectTCP(ip, port, TCPClientFactory())

    def run(self):
        self.thread = Thread(target=reactor.run, args=(False,))
        self.thread.start()

    def join(self):
        self.thread.join()

    def registerOnMessageCallBack(self, data_received):
        TCPClientCallBackHolder.MessageCallBack = data_received

    def registerOnClientConnectCallBack(self, on_net_connect):
        TCPClientCallBackHolder.ClientConnectCallBack = on_net_connect

    def registerOnClientDisconnectCallBack(self, on_net_disconnect):
        TCPClientCallBackHolder.ClientDisconnectCallBack = on_net_disconnect
