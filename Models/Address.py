from Class.ReadFiles import ReadFiles

class ModelAddress:
    def __init__(self, name, lastname, telephone,  add1, add2, num_ext, cp):
        self.name = name
        self.lastname = lastname
        self.telephone = telephone
        self.add1 = add1
        self.add2 = add2
        self.num_ext = num_ext
        self.num_int = 'N/A'
        self.entre = '{0} - {1}'.format(add1, add2)
        self.cp = cp
        self.region = 'MX-22'
        self.ciudad = 'Querétaro'

class Address:
    def __int__ (self):
        pass

    def getAddress(self):

        address = []

        read = ReadFiles("C:/Users/uriel/PycharmProjects/pythonProject/Data/dom.csv")

        for l in read.onRead():
            address.append(ModelAddress(
                name=l.split(':')[0],
                lastname=l.split(':')[1],
                telephone=l.split(':')[2],
                add1=l.split(':')[3],
                add2=l.split(':')[4],
                num_ext=l.split(':')[5],
                cp=l.split(':')[6]
            ))
        return address
