from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='staticpages')

newperson = [
    {
        "personid":"4",
        "personname":"Joesph",
        "age":"65"
    },
    {
         "personid":"6",
        "personname":"Tim",
        "age":"72"
    },
    {
         "personid":"6",
        "personname":"Margaret",
        "age":"69"
    }
]
@app.route('/')
def index():
        return "hello"
    #get all

@app.route('/person')
def getAll():
    return jsonify([])

# curl -i http://127.0.0.1:5000/person
@app.route('/person/<int:personid>')
def findById(personid):
    return jsonify({})

@app.route('/person/<string:personid>', methods =['GET'])
def get_person(personid):
    foundperson = list(filter(lambda t : t['personid'] == personid , person))
    if len(foundperson) == 0:
        return jsonify( { 'personid' : '' }),204
    return jsonify( { 'personid' : foundperson[0] })
#curl -i http://127.0.0.1:5000/person/test  ?????

@app.route('/person', methods=['POST'])
def create_person():
    if not request.json:
        abort(400)
    if not 'personid' in request.json:
        abort(400)
    newperson={
        "personid":  request.json['personid'],
        "personname": request.json['personname'],
        "age":request.json['age']
    }
    newperson.append(newperson)
    return jsonify( {'personid':personid }),201
# sample test 
# curl -X POST -d "{\"personid\":10, \"personname\":\"joesphine\", \"age\":46}" -H Content-Type:application/json http://127.0.0.1:5000/person/
@app.route('/person', methods=['POST'])
def update(personid):
    foundperson=[]
    if len(foundperson) == 0:
        return jsonify({}),404
        currentperson = foundperson[0]
        if 'personname' in request.json:
            currentperson['personname']= request.json['personname']
        if 'age' in request.json:
            currentperson['age']= request.json['age']
        return jsonify(currentperson)
#curl -X PUT -d "{\"personname\":\"test\", \"age\":46}" -H Content-Type:application/json http://127.0.0.1:5000/person/4
@app.route('/person/<int:personid>', methods = ['DELETE'])
def delete(personid):
#curl -X DELETE http://127.0.0.1:5000/person/2

    return jsonify({"done": True})

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)

