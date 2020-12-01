from PersonDao import personDao

newperson1 = {
       'personid': 13,
       'personname':'kieran',
       'age':56,
}

newperson2 = {
       'personid': 16,
       'personname':'iarla',
       'age':66,
}
#returnValue = personDao.create(newperson)
returnValue =  personDao.getAll() 
print (returnValue)
returnValue =  personDao.findByID(newperson2['personid']) 
print ("Find by Id")
returnValue =  personDao.update(newperson2) 
print (returnValue)
returnValue =  personDao.findByID(newperson2['personid']) 
print (returnValue)
returnValue =  personDao.delete(newperson2['personid']) 
print (returnValue)
returnValue =  personDao.getAll() 
print (returnValue)
