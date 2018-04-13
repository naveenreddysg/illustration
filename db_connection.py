import MySQLdb

# class Db():
#
#     def __init__(self ):
#         # print('DB is initiated')
#         self.conn = MySQLdb.connect(user="root", password="Test!234", database="illustration")
#         # print('DB is created')
#         # print(self.conn)
#
#     def execute(self, query):
#         cur = self.conn.cursor()
#         cur.execute(query)
#         result = cur.fetchall()
#         return result
#
#     def commit(self):
#         self.conn.commit()
#
#     def close(self):
#         self.conn.close()
#
# Db()


class Db():

    def __init__(self ):
        # print('DB is initiated')
        self.conn = MySQLdb.connect(user="webanalytics", password="PyPrince@123", database="webanalytics", host='68.178.217.13')
        # print('DB is created')
        # print(self.conn)

    def execute(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

Db()