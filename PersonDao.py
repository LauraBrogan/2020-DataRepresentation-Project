# My Data Representation Project 2020
# Data Access Object
import mysql.connector
import dbconfig as cfg
from mysql.connector import cursor
# creating a class for the database and connection to the mysql database
class PersonDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            
           host=        cfg.mysql['host'],
           user=        cfg.mysql['user'],
           password=    cfg.mysql['password'],
           database=    cfg.mysql['database']
        )
        #print("connection made")  test code
# defining create function
    def create(self, person):
       cursor = self.db.cursor()
       sql = "insert into person (personid, personname, age) values (%s, %s, %s)"
       values =[ 
       person['personid'],
       person['personname'],
       person['age']
       ]
       cursor.execute(sql, values)
       self.db.commit()
       return cursor.lastrowid
# defining get all function
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from person'
        cursor.execute(sql) 
        results = cursor.fetchall()
        returnArray=[]
        #print(results) test code
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray
# defining findby id function
    def findByID(self,personid):
        cursor = self.db.cursor()
        sql = 'select * from person where personid = %s'
        values = [ personid ]
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDict(result)

# defininf update function
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

# defining delete function 
    def delete(self,personid):
        cursor = self.db.cursor()
        sql = 'delete from person where personid = %s'
        values = [personid]
        cursor.execute(sql,values)
        return{}
# converting output of find and get all fucntions
    def convertToDict(self,result):
         colnames = ['personid', 'personname','age']
         person = {}
         
         if result:
            for i, colName in enumerate(colnames):
                value = result[i] 
                person[colName] = value
         return person

personDao = PersonDao()

# Laura Brogan 01/12/2020