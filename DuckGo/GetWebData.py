__author__ = 'dbatalha'

import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from DuckGo.DuckHTMLParser import *
import PingPing


class DuckParser(object):

    def __init__(self):
        # Variables used on get duck websites.
        self.local_dir = os.getcwd()
        self.csv_dir = os.path.join(self.local_dir, "DuckGo", "words_data")

        # List wih all websites
        self.websites_list = []

        # List whit all trimmed websites (address only)
        self.websites_list_trimmed = []

        self.ping = PingPing.PingMaster()

    @staticmethod
    def get_website_address(website):
        site = str(website).find("/")

        if site == -1:
            website_processed = website
        else:
            website_processed = str(website)[0:site]

        return website_processed

    def get_duck_websites(self):
        """
        This method open the webpage "https://duckduckgo.com" and get all websites.
        Stores the output websites on a python list.
        :return:
        """

        for csv in os.listdir(self.csv_dir):
            if csv.endswith(".csv"):

                current_file_path = os.path.join(self.csv_dir, csv)
                words_file = open(current_file_path, "r")

                for word in words_file:
                    prep = word.strip()

                    # Load web driver variable.
                    driver = webdriver.Firefox()

                    driver.get("https://duckduckgo.com/")

                    driver.find_element_by_id('search_form_input_homepage').send_keys(prep)
                    driver.find_element_by_id('search_button_homepage').click()

                    for times in range(0, 50):
                        driver.find_element_by_id('links_wrapper').send_keys(Keys.SPACE)

                    html_source = driver.page_source

                    parser = GoDuckParser()
                    parser.feed(html_source)
                    html_data = parser.get_data()

                    html = html_data.split()
                    len_html = len(html)

                    domains = [".net", ".com", ".org", ".edu"]
                    for domain in domains:
                        i = 0
                        while i < len_html:
                            net = html[i].find(str(domain))
                            if int(net) >= 0:
                                dots = html[i].find("...")
                                more = html[i].find("More")
                                if int(dots) != -1 and int(more) != -1:
                                    complete_url = html[i][int(dots)+3:int(more)]
                                    garbage = complete_url.find(")")
                                    random_dot = complete_url.find(".")
                                    if int(garbage) == 0:
                                        self.websites_list.append(html[i][int(garbage)+2:int(dots)])
                                    if int(random_dot) == 0:
                                        print "Random dot here"

                                    try:
                                        trimmed = self.get_website_address(complete_url)
                                    except UnicodeEncodeError:
                                        trimmed = None

                                    self.ping.ping_web(trimmed)

                                    self.websites_list.append(complete_url)
                                    self.websites_list_trimmed.append(trimmed)

                                    print "Complete: %s Trimmed: %s" % (complete_url, trimmed)

                            i += 1

                    driver.get("https://duckduckgo.com/")
                    driver.close()
