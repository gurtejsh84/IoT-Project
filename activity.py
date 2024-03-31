import json,urllib
from http.client import HTTPSConnection

params=urllib.parse.urlencode({"where": json.dumps({
    "ssn": 11223344
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


connection = HTTPSConnection('parseapi.back4app.com', 443)
connection.connect()
# The below line is used when we are updating by using the objectId of the object
# connection.request('PUT', '/classes/Employee/object_id', json.dumps({
# example: connection.request('PUT', '/classes/Employee/dEMVhhHoVv', json.dumps({

# The below line id used when we are updating by using a particular column value of the object 
# connection.request('PUT', '/classes/Employee/'+ result['results'][0]['objectId'], json.dumps({
# result['name of result shown in terminal'][object number]['column name']
connection.request('PUT', '/classes/Employee/'+ result['results'][0]['objectId'], json.dumps({
    "salary": 2000
}), {
    "X-Parse-Application-Id": "XD512ac1lmVas7TNQOGfwNUkOdpLHjwjwagUHnC3",
    "X-Parse-REST-API-Key": "nwaHLQOYJ4yVdKlqwAXEGpiaEjzPehpKl7Uezd70",
    "Content-Type": "application/json"
})
result = json.loads(connection.getresponse().read())
print(result)