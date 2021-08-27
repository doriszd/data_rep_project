from flask import Flask, jsonify, request, abort
from hotel_guestsDAO import guestsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

#curl "http://127.0.0.1:5000/books"
@app.route('/guest')
def getAll():
    #print("in getall")
    results = guestsDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/guest/<int:id>')
def findById(id):
    foundguest = guestsDAO.findById(id)

    return jsonify(foundguest)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"guestID\":124,\"guest_name\":\"Marija\",\"guest_surname\":\"Maric\", \"country\":\"Serbia\"}" "http://127.0.0.1:5000/guest"
@app.route('/guest', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    
    guest = {
        "guestID": request.json['guestID'],
        "guest_name": request.json['guest_name'],
        "guest_surname": request.json['guest_surname'],
        "country": request.json['country'],
    }
    values =(guest['guestID'],guest['guest_name'],guest['guest_surname'], guest['country'])
    newId = guestsDAO.create(values)
    guest['id'] = newId
    return jsonify(guest)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
@app.route('/guest/<int:id>', methods=['PUT'])
def update(id):
    foundguest = guestsDAO.findById(id)
    if not foundguest:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'guestID' in reqJson and type(reqJson['guestID']) is not int:
        abort(400)

    if 'guest_name' in reqJson:
        foundguest['guest_name'] = reqJson['guest_name']
    if 'guest_surname' in reqJson:
        foundguest['Aguest_surname'] = reqJson['guest_surname']
    if 'country' in reqJson:
        foundguest['country'] = reqJson['country']
    if 'guestID' in reqJson:
        foundguest['guestID'] = reqJson['guestID']
    values = (foundguest['guestID'],foundguest['guest_name'],foundguest['guest_surname'],foundguest['country'], foundguest['id'])
    guestsDAO.update(values)
    return jsonify(foundguest)
        

 

@app.route('/guest/<int:id>' , methods=['DELETE'])
def delete(id):
    guestsDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)