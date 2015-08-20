__author__ = 'dbatalha'
import ping


class PingMaster(object):
    def __init__(self):
        self.ping_main = None

    def ping_web(self):
        print self.ping_main
        #ping.quiet_ping("www.google.com")
        ping.do_one("www.google.com", 2, 5)
