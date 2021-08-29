# Server.py

# importing flask, jsonify, request and abort
from flask import Flask, jsonify, request, abort
# importing class guestsDAO from my file hotel_guestsDAO 
from hotel_guestsDAO import guestsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

#@app.route('/')
#def index():
    #return "Hello, World!"


####################################################################################################################

# Get All: gets all data from the table guest
#curl "http://127.0.0.1:5000/guest"
@app.route('/guest')
def getAll():
    #print("in getall")
    # Connects to guest table
    result = guestsDAO.getAll()
    # return result
    return jsonify(result)



####################################################################################################################

# FindById: finds specific data based on id. In this case it found guest with id 2.
#curl "http://127.0.0.1:5000/guest/2"
@app.route('/guest/<int:id>')
def findById(id):
    # return guest from db by requested id
    foundguest = guestsDAO.findById(id)
    # Check if id exists
    if not foundguest:
        return "That id does not exist in the database table"
        abort(404)

    return jsonify(foundguest)



####################################################################################################################

# Create: Creates new data in a table
#curl  -i -H "Content-Type:application/json" -X POST -d "{\"guestID\":124,\"guest_name\":\"Marija\",\"guest_surname\":\"Maric\", \"country\":\"Serbia\"}" "http://127.0.0.1:5000/guest"
@app.route('/guest', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    
    # id increments automatically
    guest = {
        "guestID": request.json['guestID'],
        "guest_name": request.json['guest_name'],
        "guest_surname": request.json['guest_surname'],
        "country": request.json['country'],
    }

    # Make the tuple for database
    values =(guest['guestID'],guest['guest_name'],guest['guest_surname'], guest['country'])
    newId = guestsDAO.create(values)
    guest['id'] = newId
    return jsonify(guest)


####################################################################################################################

#Update: updating some data in a table. In this case name of the country was updated
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"country\":\"Spain\"}" "http://127.0.0.1:5000/guest/4"
@app.route('/guest/<int:id>', methods=['PUT'])
def update(id):
    # Find the guest in a table
    foundguest = guestsDAO.findById(id)
    if not foundguest:
        return "That id does not exist in the database table"
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json

    if 'guestID' in reqJson and type(reqJson['guestID']) is not int:
        abort(400)

    # data to update
    if 'guestID' in reqJson:
        foundguest['guestID'] = reqJson['guestID']
    if 'guest_name' in reqJson:
        foundguest['guest_name'] = reqJson['guest_name']
    if 'guest_surname' in reqJson:
        foundguest['guest_surname'] = reqJson['guest_surname']
    if 'country' in reqJson:
        foundguest['country'] = reqJson['country']
    
    
    # Make the tuple for database
    values = (foundguest['guestID'],foundguest['guest_name'],foundguest['guest_surname'],foundguest['country'], foundguest['id'])
    # Do the update on database
    guestsDAO.update(values)
    return jsonify(foundguest)
        

####################################################################################################################
 
# Delete: deletes data based on id
#curl -X DELETE "http://127.0.0.1:5000/guest/4"
@app.route('/guest/<int:id>' , methods=['DELETE'])
def delete(id):
    # Remove guest from database by id
    guestsDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)