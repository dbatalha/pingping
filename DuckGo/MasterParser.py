__author__ = 'dbatalha'

from GetWebData import *


class MasterParser(DuckParser):

    def __init__(self):
        super(MasterParser, self).__init__()

    def get_duck_websites(self):
        """
        This method override the class DuckParser open the webpage "https://duckduckgo.com" and get all websites.
        Stores the output websites on a python list.
        :return:
        """
        DuckParser.get_duck_websites(self)