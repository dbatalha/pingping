from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from duck_html_parser import *
import os

def main():
    local_dir = os.getcwd()
    csv_dir = os.path.join(local_dir, 'words_data')

    driver = webdriver.Firefox()
    driver.get("https://duckduckgo.com/")

    for csv in os.listdir(csv_dir):
        if csv.endswith(".csv"):
            print csv

            current_file_path = os.path.join(csv_dir, csv)
            words_file = open(current_file_path, "r")

            for word in words_file:
                prep = word.strip()
                driver.find_element_by_id('search_form_input_homepage').send_keys(prep)
                driver.find_element_by_id('search_button_homepage').click()

                for times in range(0, 50):
                    driver.find_element_by_id('links_wrapper').send_keys(Keys.SPACE)

                html_source = driver.page_source

                parser = GoDuckParser()
                parser.feed(html_source)
                html_data = parser.get_data()

                html = html_data.split()
                lenhtml = len(html)

                i = 0
                while i < lenhtml:
                    net = html[i].find(".net")
                    if int(net) >= 0:
                        dots = html[i].find("...")
                        if int(dots) != -1:
                            print html[i]
                    '''
                    com = html[i].find(".com")
                    if int(com) >= 0:
                        print html[i]
                    org = html[i].find(".org")
                    if int(org) >= 0:
                        print html[i]
                    '''
                    i += 1

                driver.get("https://duckduckgo.com/")

        driver.close()
if __name__ == "__main__":
    main()