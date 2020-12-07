#This was a testing file I used to test the commands in the PersonDao.py 
# to return the results to ther terminal
from PersonDao import personDao


person1 = {
   'personid': 27,
   'personname':'eugene',
   'age':45
}

person2 = {
       'personid': 27,
       'personname':'martin',
       'age':50,
}
#returnValue = personDao.create(person)
#print(returnValue)
returnValue = personDao.getAll()
print(returnValue)
returnValue =  personDao.findByID(person2['personid']) 
print("find byID")
print (returnValue)
returnValue =  personDao.update(person2) 
print (returnValue)
returnValue =  personDao.findByID(person2['personid']) 
print (returnValue)
returnValue =  personDao.delete(person2['personid']) 
print (returnValue)
returnValue =  personDao.getAll() 
print (returnValue)

# Laura Brogan 06/12/2020