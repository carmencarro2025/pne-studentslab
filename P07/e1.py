import http.client
import json

PORT = 8080
SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'

print("Server:", SERVER)
print("URL:", SERVER + ENDPOINT + PARAMS)

conn = http.client.HTTPSConnection(SERVER)

conn.request("GET", ENDPOINT + PARAMS)


response = conn.getresponse()
print("Response received!:", response.status, response.reason)
data = json.loads(response.read().decode())

if data["ping"] == 1:
    print("ALIVE!")