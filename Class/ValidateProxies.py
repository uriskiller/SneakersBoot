from Models.Proxies import Proxies
import cloudscraper
import requests


class ValidateProxies:
    def __init__(self):
        self.proxies = Proxies()

    def validate(self):
        proxy = self.proxies.getProxies()

        for p in proxy:
            try:
                session = requests.Session()
                session.proxies = {
                        'http': '{0}:{1}'.format(p.host, p.port),
                        'https': '{0}:{1}'.format(p.host, p.port)
                    }

                scraper = cloudscraper.create_scraper(sess=session)


                ip = scraper.get("https://api.myip.com/").text

                print(ip)
            except Exception as e:
                pass

vp = ValidateProxies()
vp.validate()