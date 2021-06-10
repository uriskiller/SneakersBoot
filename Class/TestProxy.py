from Models.Proxies import Proxies
import cloudscraper
import requests
import time
import datetime
from bs4 import BeautifulSoup
from requests_toolbelt.auth.http_proxy_digest import HTTPProxyDigestAuth

class TestProxy:
    def __init__(self):
        self.proxies = Proxies()



    def getIp(self):


        proxy = self.proxies.getProxies()
        instances = []

        for p in proxy:
            session = requests.Session()
            session.proxies = {
                    'http': '{0}:{1}@{2}:{3}'.format(p.username, p.password, p.host, p.port)
                }

            session.auth = HTTPProxyDigestAuth(p.username, p.password)

            scraper = cloudscraper.create_scraper(sess=session)

            #instances.append(scraper)

            ip = scraper.get("https://api.myip.com/").text

            #ip = session.get("https://api.myip.com/").text

            print(ip)
            


        cont = 0
        exit()
        while True:
            val = cont % len(instances)
            print(val)
            ti = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            f = open("history.txt", "a")
            try:
                html = instances[val].get("https://www.innvictus.com/hombres/basket/calzado/nike/tenis-air-jordan-1-retro-high-og/p/000000000000145303")

                soup = BeautifulSoup(html.text, 'html.parser')

                confirmed = False if soup.find("div", {"class": "notify-box notify-box-soldout hidden"}) is None else True

                f.write("\n{0}\t-\t:{1}\t-\tSTOCK: {2}".format(ti, html.status_code, confirmed))
                time.sleep(7)
            except Exception as e:
                f.write("\n{0}\t-\t:{1}".format(ti, e))
                time.sleep(7)

                a = ""

                pass
            cont = cont + 1
            f.close()

t = TestProxy()
t.getIp()
