from Class.ReadFiles import ReadFiles

class ModelAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Accounts:
    def __init__(self):
        pass

    def getAccounts(self):
        accounts = []
        read = ReadFiles("C:/Users/uriel/PycharmProjects/pythonProject/Data/accounts.txt")

        for l in read.onRead():
            accounts.append(ModelAccount(
                username=l.split(':')[0],
                password=l.split(':')[1]
            ))
        return accounts