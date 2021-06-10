from selenium import webdriver
from Class.GenZip import genZip
import undetected_chromedriver as uc
from Models.ItemList import itemList


class LoadWindows:
    def __init__(self, link, proxy):
        self.link = link
        self.proxy = proxy
        self.config = None
        self.driver = None

    def Process(self):
        items = itemList(self.link, self.proxy).getItemList()

        self.addExtension(items)

    def addExtension(self, items):

        g = genZip(items.host, items.port, items.username, items.password)

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_extension(g.file)

        self.config = options

    def Navigate(self):
        self.driver = uc.Chrome(options=self.config)
        self.driver.get(self.link)