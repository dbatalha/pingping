from HTMLParser import HTMLParser

class GoDuckParser(HTMLParser):
    '''
    def handle_starttag(self, tag, attrs):
        print "Encounter a start tag:", tag

    def handle_endtag(self, tag):
        print "Encounter a end tag:", tag
    '''
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, data):
        self.fed.append(data)

    def get_data(self):
        return ''.join(self.fed)