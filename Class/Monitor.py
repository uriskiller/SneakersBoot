from Models.Links import Links
from Class.Load import Load
from Class.Email import Email
import cloudscraper
from bs4 import BeautifulSoup
from Models.Proxies import Proxies
from Models.Accounts import Accounts
import requests
import time
import datetime
from threading import Thread


class Monitor:
    def __init__ (self):
        self.list = Links().getLinks()
        self.proxies = Proxies().getProxies()
        self.accounts = Accounts().getAccounts()
        self.session_instances = []
        self.accounts_relation = []
        self.email = Email()
        self.load = None

    def manageDrivers(self, account, proxy, url):
        load = Load(account, proxy, url)
        load.Proccess()

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

    def relationship(self):

        # SE TRAE LA LISTA DE PROXIES QUE UTILIZARA PARA REALIZAR LAS COMPRAS
        proxyUsers = Proxies().getProxies("C:/Users/uriel/PycharmProjects/pythonProject/Data/proxies_users.txt")

        count = 0

        for p in self.accounts:
            self.accounts_relation.append({'account': p, 'proxy': proxyUsers[count]})
            count = count + 1

    def onMonitoring(self):
        # SE CREAN LAS INSTANCIAS PARA EL MONITOR  CON UN PROXY DIFERENTE
        self.setSessionInstances()

        # SE CREA RELACION ENTRE CUENTAS DE USUARIO Y EL PROXY QUE UTILIZARA PARA EFECTUAR LA COMPRA
        self.relationship()

        cont = 0

        while True:
            val = cont % len(self.session_instances)
            ti = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            f = open("history.txt", "a")
            try:
                # REVIEW EACH LINK
                for p in self.list:

                    html = self.session_instances[val].get(p.Url)

                    soup = BeautifulSoup(html.text, 'html.parser')

                    confirmed = False if soup.find("div",
                                                   {"class": "notify-box notify-box-soldout hidden"}) is None else True

                    print(confirmed)

                    if confirmed is True:
                        cont = 0
                        print("Stock")
                        for i in self.accounts_relation:
                            t = Thread(target=self.manageDrivers, args=(i['account'], i['proxy'], p.Url))
                            t.start()
                            cont = cont + 1
                        self.email.sendEmail("Stock disponible")

                        return

                    f.write("\n{0}\t-\t:{1}\t-\tSTOCK: {2}".format(ti, html.status_code, confirmed))
                    time.sleep(1)
            except Exception as e:
                f.write("\n{0}\t-\t:{1}".format(ti, e))
                print(e)
                return

                a = ""

                pass
            cont = cont + 1
            f.close()

print("corriendo")
monitor = Monitor()
monitor.onMonitoring()
