__author__ = 'dbatalha'
import subprocess


class PingMaster(object):
    def __init__(self):
        self.ip_address = None

    def ping_web(self, address):
        """
        Ping websites, this method receive the ip address to scan.
        :param address:
        :return:
        """
        print self.ip_address
        subprocess.call(["ping", "-c", "1", address])
