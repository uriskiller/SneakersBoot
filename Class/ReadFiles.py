class ReadFiles:
    def __init__ (self, fullLocation):

        self.fullLocation = fullLocation

    def onRead(self):
        list = []
        f = open(self.fullLocation, "r")

        for x in f:
            if x[:2] != '--':
                list.append(x.strip('\n'))
        f.close()
        return list