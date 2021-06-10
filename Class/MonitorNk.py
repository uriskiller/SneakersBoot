import requests
import cloudscraper
from bs4 import BeautifulSoup
import json
import pandas as pd
from Class.Email import Email
from Models.Proxies import Proxies
from Models.Links import Links
import time
import datetime
from threading import Thread

class MonitorNk:
    def __init__(self, link):
        self.link = 'https://api.nike.com/deliver/available_gtins/v2?filter=styleColor%28{0}%29&filter=merchGroup%28mx%29'.format(link)
        self.proxies = Proxies().getProxies()
        self.session_instances = []

    def setSessionInstances(self):
        for p in self.proxies:
            try:
                session = requests.Session()
                session.proxies = {
                    'http': '{0}:{1}@{2}:{3}'.format(p.username, p.password, p.host, p.port)
                }

                scraper = cloudscraper.create_scraper(sess=session)

                self.session_instances.append(scraper)

                # ip = scraper.get("https://api.myip.com/").text

                # print(ip)
            except Exception as e:
                print(e)

    def onMonitoring(self):
        # SE CREAN LAS INSTANCIAS PARA EL MONITOR  CON UN PROXY DIFERENTE
        self.setSessionInstances()

        cont = 0

        while True:
            try:
                val = cont % len(self.session_instances)
                response = self.session_instances[val].get(self.link)
                soup = BeautifulSoup(response.text, 'html.parser')
                site_json = json.loads(soup.text)['objects']
                tb = pd.json_normalize(site_json).sort_values(by=['gtin'])
                d = 12
            except Exception as e:
                print(e)



mnk = MonitorNk('554724-122')
mnk.onMonitoring()