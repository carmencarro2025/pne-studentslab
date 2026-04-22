import http.client
import json

genes = {"FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"}

SERVER = 'rest.ensembl.org'
ENDPOINT = f'/sequence/id/{genes["MIR633"]}'
PARAMS = '?content-type=application/json'

print("Server:", SERVER)
print("URL:", SERVER + ENDPOINT + PARAMS)

conn = http.client.HTTPSConnection(SERVER)

conn.request("GET", ENDPOINT + PARAMS)


response = conn.getresponse()
print("Response received!:", response.status, response.reason)
data = json.loads(response.read().decode())
print(f"\nGene: {list(genes.keys())[4]}")
print(f"Description: {data['desc']}")
print(f"Bases: {data['seq']}")