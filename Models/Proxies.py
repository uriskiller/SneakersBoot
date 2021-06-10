from Class.ReadFiles import ReadFiles

class ModelProxy:
    def __init__ (self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

class Proxies:
    def __init__(self):
        pass

    def getProxies(self, path="C:/Users/uriel/PycharmProjects/pythonProject/Data/Proxies.txt"):
        proxies = []
        read = ReadFiles(path)

        for l in read.onRead():
            proxies.append(ModelProxy(
                host=l.split(':')[0],
                port=l.split(':')[1],
                username=l.split(':')[2],
                password=l.split(':')[3]
            ))
        return proxies
