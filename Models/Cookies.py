from Class.ReadFiles import ReadFiles
from datetime import datetime
import re

class ModelCookies:
    def __init__(self, domain, include_subdomains, path, secure, expiry, name, value):
        self.domain = domain
        self.include_subdomains = include_subdomains
        self.path = path
        self.secure = secure
        self.expiry = expiry
        self.name = name
        self.value = value



class Cookies:
    def __int__ (self):
        pass

    def getCookies(self):

        cookies = []
        read = ReadFiles("C:/Users/uriel/PycharmProjects/pythonProject/Data/innvictus.com_cookies.txt")

        for l in read.onRead():

            expire = datetime.utcfromtimestamp(int(l.split(':')[4])).strftime('%Y-%m-%d %H:%M:%S') \
                if len(re.findall('^[0-9]{10}$',l.split(':')[4])) > 0 \
                else l.split(':')[4]

            cookies.append(ModelCookies(
                domain=l.split(':')[0],
                include_subdomains=l.split(':')[1],
                path=l.split(':')[2],
                secure=l.split(':')[3],
                expiry=expire,
                name=l.split(':')[5],
                value=l.split(':')[6]
            ))
        return cookies