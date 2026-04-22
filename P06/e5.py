from Seq1 import Seq
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

i = 0
for gene, id in genes.items():

    SERVER = 'rest.ensembl.org'
    ENDPOINT = f'/sequence/id/{id}'
    PARAMS = '?content-type=application/json'

    print("\nServer:", SERVER)
    print("URL:", SERVER + ENDPOINT + PARAMS)

    conn = http.client.HTTPSConnection(SERVER)

    conn.request("GET", ENDPOINT + PARAMS)


    response = conn.getresponse()
    print("Response received!:", response.status, response.reason)
    data = json.loads(response.read().decode())

    print(f"\nGene: {gene}")
    print(f"Description: {data['desc']}")

    s = Seq(data['seq'])
    print(f"Total length: {s.len()}")
    for base, count in s.count().items():
        if s.len() > 0:
            percent = count / s.len() * 100
            print(f"{base}: {count} ({round(percent, 1)}%)")
        else:
            print(f"{base}: {count}")

    sorted_d = sorted(s.count().items(), key=lambda x: x[1], reverse=True)
    first_base = sorted_d[0][0]
    print(f"Most frequent Base: {first_base}")
    i += 1