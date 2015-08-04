__author__ = 'dbatalha'

import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from DuckGo.DuckHTMLParser import *


class DuckParser(object):

    def __init__(self):
        self.local_dir = os.getcwd()
        self.csv_dir = os.path.join(self.local_dir, "words_data")

        self.driver = webdriver.Firefox()

    def get_duck_websites(self):
        self.driver.get("https://duckduckgo.com/")

        for csv in os.listdir(self.csv_dir):
            if csv.endswith(".csv"):

                current_file_path = os.path.join(self.csv_dir, csv)
                words_file = open(current_file_path, "r")

                for word in words_file:
                    prep = word.strip()
                    self.driver.find_element_by_id('search_form_input_homepage').send_keys(prep)
                    self.driver.find_element_by_id('search_button_homepage').click()

                    for times in range(0, 50):
                        self.driver.find_element_by_id('links_wrapper').send_keys(Keys.SPACE)

                    html_source = self.driver.page_source

                    parser = GoDuckParser()
                    parser.feed(html_source)
                    html_data = parser.get_data()

                    html = html_data.split()
                    lenhtml = len(html)

                    domains = [".net", ".com", ".org", ".edu"]
                    for domain in domains:
                        i = 0
                        while i < lenhtml:
                            net = html[i].find(str(domain))
                            if int(net) >= 0:
                                dots = html[i].find("...")
                                more = html[i].find("More")
                                if int(dots) != -1 and int(more) != -1:
                                    complete_url = html[i][int(dots)+3:int(more)]
                                    garbage = complete_url.find(")")
                                    random_dot = complete_url.find(".")
                                    if int(garbage) == 0:
                                        print html[i][int(garbage)+2:int(dots)]
                                    if int(random_dot) == 0:
                                        print "Random dot here"
                                    print complete_url
                            i += 1

                    self.driver.get("https://duckduckgo.com/")

            self.driver.close()