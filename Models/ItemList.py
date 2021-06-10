class itemListModel:
    def __init__(self, link,  host, port, username, password):
        self.link = link
        self.host = host
        self.port = port
        self.username = username
        self.password = password


class itemList:

    def __init__(self, link, proxy):
        self.link = link
        self.proxy = proxy

    def getItemList(self):

        return itemListModel(
            link= self.link,
            host= self.proxy.split(':')[0],
            port= self.proxy.split(':')[1],
            username= self.proxy.split(':')[2],
            password= self.proxy.split(':')[3])





