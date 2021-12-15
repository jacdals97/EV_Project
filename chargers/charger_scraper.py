from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities

import re
import pickle
import pandas as pd
import json



def log_filter(log_):
        return(
        # is an actual response
        log_["method"] == "Network.responseReceived"
        # and json
        and "json" in log_["params"]["response"]["mimeType"]
        )


class WebDriver:

    result = {}

    def __init__(self):
        self.options = Options()
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('load-extension=' + '1.38.6_0') #path to extensions, here adblock
        #self.options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=self.options, desired_capabilities= capabilities)
        self.result['latitude'] = 'NA'
        self.result['longitude'] = 'NA'
        self.result['address'] = 'NA'
        self.result['created_at'] = 'NA'
        self.result['id'] = 'NA'
        self.result['municipality'] = 'NA'
        self.result['city'] = 'NA'
        self.result['zip_code'] = 'NA'
        self.result['plugs'] = 'NA'
        self.result['cost_description'] = 'NA'
        self.result['description'] = 'NA'


    def log_filter(log_):
        return(
        # is an actual response
        log_["method"] == "Network.responseReceived"
        # and json
        and "json" in log_["params"]["response"]["mimeType"]
        )
    def scrape(self, url):
        scraping = True
        idd = re.search('[0-9]+$', url)[0]
        while scraping:
            try:
                self.driver.get(url)
                WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "display-title")))
                print(1)
            except Exception as e:
                #self.driver.quit()
                break
            try:
                logs_raw = self.driver.get_log("performance")
                logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
                for log in filter(log_filter, logs):
                    request_id = log["params"]["requestId"]
                    resp_url = log["params"]["response"]["url"]
                    if re.search('locations/' + idd, resp_url):
                        response = x.driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
                        response = json.loads(response['body'])
                        if response['reverse_geocoded_address_components']['country_code'] != 'DK':
                            break
                    elif re.search('locations/' + 'nearby', resp_url):
                        nearby = x.driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
                        for neighbor in json.loads(nearby['body']):
                            urls.append(neighbor['url'])
                n_outlets = 0
                for station in response['stations']:
                    n_outlets += len(station['outlets'])
                self.result['latitude'] = response['latitude']
                self.result['longitude'] = response['longitude']
                self.result['address'] = response['address']
                self.result['plugs'] = n_outlets
                self.result['created_at'] = response['created_at']
                self.result['id'] = response['id']
                self.result['cost_description'] = response['cost_description']
                self.result['description'] = response['description']
                self.result['municipality'] = response['reverse_geocoded_address_components']['administrative_area_2']
                self.result['city'] = response['reverse_geocoded_address_components']['locality']
                self.result['zip_code'] = response['reverse_geocoded_address_components']['postal_code']
                self.result['country_code'] = response['reverse_geocoded_address_components']['country_code']


                #self.driver.quit()
                scraping = False
            
            except:
                
                scraping = False
                pass

        return (self.result)


chargers = pd.read_csv("charger_links.csv")
urls = list(chargers["link"])
seen = dict()

x = WebDriver()
for url in urls:
    try:
        seen[url]
        continue
    except:
        seen[url] = True    
        res = x.scrape(url)
        print(res)
    try:
        pickle_out = open('raw_data/' + str(res["id"]) + res["city"] + '.pickle',"wb")
        pickle.dump(res, pickle_out)
        pickle_out.close()
    except:
        continue
