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
