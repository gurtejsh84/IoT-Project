import json,urllib
from http.client import HTTPSConnection

# This is used to get info of rfid: value
params=urllib.parse.urlencode({"where": json.dumps({
    "rfid":12345678
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