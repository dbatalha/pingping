__author__ = 'dbatalha'

from GetWebData import *


class MasterParser(DuckParser):

    def __init__(self):
        super(MasterParser, self).__init__()

    def get_duck_websites(self):

        DuckParser.get_duck_websites(self)