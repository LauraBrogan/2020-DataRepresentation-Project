from flask import Flask, url_for, request, redirect, abort, jsonify
from PersonDao import personDao


app = Flask(__name__,
            static_url_path='', 
            static_folder='staticpages')

#@app.route('/')
#def index():
        #return "hello"
    #get all

@app.route('/person')
def getAll():
    return jsonify(personDao.getAll())

# curl -i http://127.0.0.1:5000/person
@app.route('/person/<int:personid>')
def findById(personid):
    return jsonify(personDao.findByID(personid))

#@app.route('/person/<string:personid>', methods =['GET'])
#def get_person(personid):
 #   foundperson = list(filter(lambda t : t['personid'] == personid, person))
 #   if len(foundperson) == 0:
 #       return jsonify( { 'personid' : '' }),204
  #  return jsonify( { 'personid' : foundperson[0] })
#curl -i http://127.0.0.1:5000/person/test  ?????

@app.route('/person/', methods=['POST'])
def create():
    #global nextId
    #return"served by createuser"
    if not request.json:
        abort(400)
      #  if not 'personid' in request.json:
     #   abort(400)
    person = {
        #"personid":  nextId,
            "personid": request.json["personid"],
            "personname": request.json["personname"],
            "age":request.json["age"]
    }
    return jsonify(personDao.create(person))
    #return"served by Create"
    #person.append(person)
    #nextId+=1
    #return jsonify( {'personid':personid }),201
# sample test 
# curl -X POST -d "{\"personid\":10, \"personname\":\"joesphine\", \"age\":46}" -H Content-Type:application/json http://127.0.0.1:5000/person/
@app.route('/person/<int:personid>', methods=['PUT'])
def update(personid):
    foundPerson=personDao.findByID(personid)
    print(foundPerson)
    if foundPerson == {}:
       return jsonify({}),404
    currentPerson = foundPerson
    if 'personname' in request.json:
        currentPerson['personname']= request.json['personname']
    if 'age' in request.json:
        currentPerson['age']= request.json['age']
    personDao.update(currentPerson)
    return jsonify(currentPerson)
#curl -X PUT -d "{\"personname\":\"test\", \"age\":46}" -H Content-Type:application/json http://127.0.0.1:5000/person/4

#DELETE
#curl -X DELETE http://127.0.0.1:5000/person/2
@app.route('/person/<int:personid>', methods = ['DELETE'])
def delete(personid):
    personDao.delete(personid)
    return jsonify({"done": True})

#@app.errorhandler(404)
#def not_found404(error):
   #return make_response( jsonify( {'error':'Not found' }), 404)

#@app.errorhandler(400)
#def not_found400(error):
  #return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)

#Laura Brogan 06/12/2020