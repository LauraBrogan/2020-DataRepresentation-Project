from PersonDao import personDao

newperson1 = {
       'personid': 20,
       'personname':'sean',
       'age':66
}

newperson2 = {
       'personid': 2,
       'personname':'iarla',
       'age':66,
}
#returnValue = personDao.create(newperson)
#print(returnValue)
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
