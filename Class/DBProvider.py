import sqlalchemy as db
import  pandas as pd

class DBProvider:
    def __init__(self):
        self.path = r'C:\Users\uriel\PycharmProjects\pythonProject'
        self.engine = ''
        self.connection  = ''
        self.metadata  = ''
        self.connect()

    def connect(self):
        try:
            self.engine = db.create_engine('sqlite:///{0}/DB/SNKRS_CONTROL.db'.format(self.path))
            self.connection = self.engine.connect()
            self.metadata = db.MetaData()
            print("Opened database successfully")
        except Exception as e:
            print(e)

    def getResults(self, table_name):
        census = db.Table(table_name, self.metadata, autoload=True, autoload_with=self.engine)
        query = db.select([census])
        ResultProxy = self.connection.execute(query)
        ResultSet = ResultProxy.fetchall()

        df = pd.DataFrame(ResultSet)
        df.columns = ResultSet[0].keys()

    def getAccounts(self):
        census = db.Table('ACCOUNTS', self.metadata, autoload=True, autoload_with=self.engine)
        b_tb = db.Table('STORES', self.metadata, autoload=True, autoload_with=self.engine)


        query = census.join(b_tb, census.c.ID_STORE == b_tb.c.ID_STORE).
        query = query.select()

        ResultProxy = self.connection.execute(query)
        ResultSet = ResultProxy.fetchall()

        df = pd.DataFrame(ResultSet)
        df.columns = ResultSet[0].keys()
        d = 's'



d = DBProvider()
d.getAccounts()
