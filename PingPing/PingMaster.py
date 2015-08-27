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

        if ifs_address_1 is not -1:
            # Process string get ip address.
            ifs_ip_1 = str(self.ping_raw_data).find(")")

            # Assemble the variables for ip and address.
            self.address_ping = str(self.ping_raw_data)[ifs_address_1 + 5:ifs_address_2]
            self.ip_ping = str(self.ping_raw_data)[ifs_address_2 + 1:ifs_ip_1]

            # Process second step from ping command.
            ifs_64_bytes_string = str(self.ping_raw_data).find("64")

            if ifs_64_bytes_string is not -1:
                # Get icmp value from ping command.
                ifs_icmp_response_1 = str(self.ping_raw_data).find("=")
                ifs_icmp_response_2 = str(self.ping_raw_data).find("ttl")

                ifs_ttl_response_1 = str(self.ping_raw_data).find("=", ifs_icmp_response_2)
                ifs_ttl_response_2 = str(self.ping_raw_data).find("time")

                ifs_time_response_1 = str(self.ping_raw_data).find("=", ifs_ttl_response_2)
                ifs_time_response_2 = str(self.ping_raw_data).find("ms")

                icmp_string = str(self.ping_raw_data)[ifs_icmp_response_1 + 1:ifs_icmp_response_2]
                ttl_string = str(self.ping_raw_data)[ifs_ttl_response_1 + 1:ifs_ttl_response_2]
                time_string = str(self.ping_raw_data)[ifs_time_response_1 + 1:ifs_time_response_2]

                print "icmp: %s ttl: %s time: %s" % (icmp_string, ttl_string, time_string)

        else:
            print "Unable to perform ping operation"

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
