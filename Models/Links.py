from Class.ReadFiles import ReadFiles

class ModelLink:
    def __init__ (self, Url):
        self.Url = Url

class Links:

    def __int__ (self):
        pass

    def getLinks(self):

        links = []
        read = ReadFiles("C:/Users/uriel/PycharmProjects/pythonProject/Data/Enlaces.txt")

        for l in read.onRead():
            links.append(ModelLink(l))
        return links
