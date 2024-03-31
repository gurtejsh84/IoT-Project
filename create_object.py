import json
from http.client import HTTPSConnection

myObject={
    "name": "Karan",
    "rfid": 87654321,
    "ssn": 11112222
}

connection = HTTPSConnection('parseapi.back4app.com', 443)
connection.connect()
connection.request('POST', '/classes/Employee', json.dumps(myObject), {
    "X-Parse-Application-Id": "XD512ac1lmVas7TNQOGfwNUkOdpLHjwjwagUHnC3",
    "X-Parse-REST-API-Key": "nwaHLQOYJ4yVdKlqwAXEGpiaEjzPehpKl7Uezd70",
    "Content-Type": "application/json"
})
results = json.loads(connection.getresponse().read())
print(results)