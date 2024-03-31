import json,urllib
from http.client import HTTPSConnection


connection = HTTPSConnection('parseapi.back4app.com', 443)
connection.connect()
# The below line is used to delete all the record of the the given object by specifying the 
# objectId of that particular object
# connection.request('DELETE', '/classes/Employee/dEMVhhHoVv', '', {
#     "X-Parse-Application-Id": "XD512ac1lmVas7TNQOGfwNUkOdpLHjwjwagUHnC3",
#     "X-Parse-REST-API-Key": "nwaHLQOYJ4yVdKlqwAXEGpiaEjzPehpKl7Uezd70"
# })

#The below line os used to fetch info by using its name
params=urllib.parse.urlencode({"where": json.dumps({
    "name":"Gurtej"
})})

connection = HTTPSConnection('parseapi.back4app.com', 443)
connection.connect()
# connection.request('GET', '/classes/Employee', '', {
connection.request('GET', '/classes/Employee?%s' %params, '', {
    "X-Parse-Application-Id": "XD512ac1lmVas7TNQOGfwNUkOdpLHjwjwagUHnC3",
    "X-Parse-REST-API-Key": "nwaHLQOYJ4yVdKlqwAXEGpiaEjzPehpKl7Uezd70"
})
result = json.loads(connection.getresponse().read())
print(result)

# The below line is used to delete the ssn column value of a object by using its objectId
connection.request('PUT', '/classes/Employee/'+ result['results'][0]['objectId'], json.dumps({
    "rfid": {
        "__op" : "Delete"
    }
}), {
    "X-Parse-Application-Id": "XD512ac1lmVas7TNQOGfwNUkOdpLHjwjwagUHnC3",
    "X-Parse-REST-API-Key": "nwaHLQOYJ4yVdKlqwAXEGpiaEjzPehpKl7Uezd70",
    "Content-Type": "application/json"
})
result = json.loads(connection.getresponse().read())
print(result)