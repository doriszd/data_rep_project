
from hotel_guestsDAO import GuestsDAO



guest2 = {
    'guestID': 2,
    #'guest_name': 'Nenad',
    #'guest_surname': 'istra',
    #'country':'Croatia'
}

#returnvalue = GuestsDAO().create(guest2)
#print(returnvalue)

returnvalue = GuestsDAO().findById(guest2['guestID'])
print("find by id")
print(returnvalue)

#returnvalue = GuestsDAO().update(guest2)
#print("update")
#print(returnvalue)

#returnvalue =GuestsDAO().delete(guest2['guestID'])
#print("delete")
#print(returnvalue)