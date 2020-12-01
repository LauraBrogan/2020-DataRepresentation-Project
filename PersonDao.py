import mysql.connector
from mysql.connector import cursor

class PersonDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Brogan33',
            database = 'holidays'
        )
        #print("connection made")

    def create (self, newperson):
        cursor = self.db.cursor()
        sql = "insert into person (personname, age) values (%s, %s, %s)"
        values = [
           newperson['personname'],
           newperson['age']
        ]
        cursor.execute(sql,values)
        self.db.commit()
        return cursor.lastrowid


    def getAll(self):
         cursor = self.db.cursor()
         sql = 'select * from person'
         cursor.execute(sql) 
         results = cursor.fetchall()
         returnArray=[]
        # print(results)
         for result in results:
            resultAsDict=self.convertToDict(result)
            returnArray.append(resultAsDict)

         return returnArray

    def findByID(self,personid):
        cursor = self.db.cursor()
        sql = 'select * from person where personid = %s'
        values = [ personid ]
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDict(result)


    def update(self, person):
        cursor = self.db.cursor()
        sql = "update person set personname = %s, age = %s where personid = %s"
        values = [
           person['personname'],
           person['age'],
           person['personid']
        ]
        cursor.execute(sql,values)
        self.db.commit()
        return person


    def delete(self,personid):
        cursor = self.db.cursor()
        sql = 'delete from person where personid = %s'
        values = [personid]
        cursor.execute(sql,values)
        return{}

    def convertToDict(self,result):
        colnames= ['personid', 'personname','age']
        person = {}
        
        if result:
            for i, colName in enumerate(colnames):
                 value = result[i] 
                 person[colName]= value
        return person

personDao = PersonDao()

#Laura Brogan 01/12/2020