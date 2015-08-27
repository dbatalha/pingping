__author__ = 'dbatalha'
import subprocess


class PingMaster(object):
    def __init__(self):
        # Used on ping_web
        self.ping_raw_data = None

        # Used on method get_ip_address
        self.address_ping = None
        self.ip_ping = None

    def get_ip_address(self):
        """
        This method get the data from website ip address and address from ping command.
        :return:
        """

        # Process string from ping subprocess command, string address name.
        ifs_address_1 = str(self.ping_raw_data).find("PING")
        ifs_address_2 = str(self.ping_raw_data).find("(")

        # Process string get ip address.
        ifs_ip_1 = str(self.ping_raw_data).find(")")

        # Assemble the variables for ip and address.
        self.address_ping = str(self.ping_raw_data)[ifs_address_1 + 5:ifs_address_2]
        self.ip_ping = str(self.ping_raw_data)[ifs_address_2 + 1:ifs_ip_1]

        print "Address: %s IP: %s" % (self.address_ping, self.ip_ping)

    def ping_web(self, address):
        """
        Ping websites, this method receive the ip address to scan.
        :param address:
        :return:
        """

        process = subprocess.Popen(["ping", "-c", "1", address], stdout=subprocess.PIPE)
        self.ping_raw_data, error = process.communicate()

        self.get_ip_address()
