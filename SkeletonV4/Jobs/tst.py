import sqlite3

class learn():
    def __init__(self):
        self.conn = sqlite3.connect("SkeletonV4/databasev1/Timeline_selectV4.db")
        self.cursor = self.conn.cursor()
        self.descriptions = []

    def getInfo(self):
        self.cursor.execute('SELECT Description FROM engineer')
        result = self.cursor.fetchall()
        for i in result:
            self.descriptions.append(i[0])

database = learn()
database.getInfo()
print(database.descriptions)













