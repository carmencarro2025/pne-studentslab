import http.server
import http.client
import socketserver
from urllib.parse import urlparse, parse_qs
import termcolor
from pathlib import Path
import jinja2 as j
import json
from Seq1 import Seq

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def get_id(arguments):
    gene = arguments["gene"][0].upper()
    ENDPOINT = f'/lookup/symbol/human/{gene}'
    conn = http.client.HTTPSConnection('rest.ensembl.org')
    conn.request("GET", ENDPOINT + '?content-type=application/json')
    response = conn.getresponse()
    d = json.loads(response.read().decode())
    if d["display_name"] == gene:
        gene_id = d["id"]
    else:
        print(f"Gene {gene} not found")
    return gene_id

def get_name(id):
    ENDPOINT = f'/lookup/id/{id}'
    conn = http.client.HTTPSConnection('rest.ensembl.org')
    conn.request("GET", ENDPOINT + '?content-type=application/json')
    response = conn.getresponse()
    d = json.loads(response.read().decode())
    if not d.get("display_name", None):
        print(f"Gene {id} not found")
        only_id = (id, "")
        return only_id
    else:
        gene_name = d.get("display_name", None)
        id_and_name = (id + ": ", gene_name)
        return id_and_name


def get_seq(arguments):
    gene = arguments["gene"][0].upper()
    gene_id = get_id(arguments)
    ENDPOINT = f'/sequence/id/{gene_id}'
    conn = http.client.HTTPSConnection('rest.ensembl.org')
    conn.request("GET", ENDPOINT + '?content-type=application/json')
    response = conn.getresponse()

    d = json.loads(response.read().decode())
    seq = d['seq']
    return seq


PORT = 8080
SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        status = 200
        try:
            global info, output, chromosome_length, id, gene_id
            termcolor.cprint(self.requestline, 'green')

            url_path = urlparse(self.path)
            path = url_path.path  # "/echo"
            arguments = parse_qs(url_path.query)

            if path == "/":
                contents = Path('html/index.html').read_text()

            elif path == "/listSpecies":
                try:
                    ENDPOINT = '/info/species'
                    conn = http.client.HTTPSConnection(SERVER)
                    conn.request("GET", ENDPOINT + PARAMS)
                    response = conn.getresponse()

                    d = json.loads(response.read().decode())
                    list_species = d["species"]
                    names = ""
                    if not arguments:
                        limit = "None"
                        for species in list_species:
                            name = species["common_name"]
                            names += "<li>" + name.capitalize() + "</li>"

                    else:
                        limit = int(arguments["limit"][0])
                        for species in list_species[:limit]:
                            name = species["common_name"]
                            names += "<li>" + name.capitalize() + "</li>"
                    contents = read_html_file("listSpecies.html").render(context={"limit": limit,
                                                                                      "names": names,
                                                                                      "num_species": len(list_species)})
                except:
                    status = 404
                    contents = Path('html/error.html').read_text()

            elif path == "/karyotype":
                try:
                    ENDPOINT = f'/info/assembly/{arguments["species"][0].replace(" ", "%20")}'
                    conn = http.client.HTTPSConnection(SERVER)
                    conn.request("GET", ENDPOINT + PARAMS)
                    response = conn.getresponse()

                    d = json.loads(response.read().decode())
                    karyotype = d["karyotype"]
                    kar = ""
                    for n in karyotype:
                        kar += n + "<br>"

                    contents = read_html_file("karyotype.html").render(context={"kar": kar})
                except:
                    status = 404
                    contents = Path('html/error.html').read_text()

            elif path == "/chromosomeLength":
                try:
                    ENDPOINT = f'/info/assembly/{arguments["species"][0].replace(" ", "%20")}'
                    conn = http.client.HTTPSConnection(SERVER)
                    conn.request("GET", ENDPOINT + PARAMS)
                    response = conn.getresponse()

                    d = json.loads(response.read().decode())
                    top_level_region = d["top_level_region"]
                    for data in top_level_region:
                        if data['coord_system'] == 'chromosome' and arguments["chromo"][0] == data['name']:
                            chromosome_length = data['length']
                    contents = read_html_file("chromosomeLength.html").render(context={"chromosome_length": chromosome_length})
                except:
                    status = 404
                    contents = Path('html/error.html').read_text()

            elif path == "/geneLookup":
                try:
                    gene = arguments["gene"][0].upper()
                    gene_id = get_id(arguments)
                    contents = read_html_file("geneLookup.html").render(context={"gene_id": gene_id,
                                                                                 "gene": gene})
                except:
                    status = 404
                    contents = Path('html/error.html').read_text()

            elif path == '/geneSeq':
                try:
                    gene = arguments["gene"][0].upper()
                    seq = get_seq(arguments)
                    contents = read_html_file("geneSeq.html").render(context={"seq": seq,
                                                                                 "gene": gene})
                except:
                    status = 404
                    contents = Path('html/error.html').read_text()

            elif path == "/geneInfo":
                try:
                    gene = arguments["gene"][0].upper()
                    gene_id = get_id(arguments)
                    ENDPOINT = f'/lookup/id/{gene_id}?'
                    conn = http.client.HTTPSConnection(SERVER)
                    conn.request("GET", ENDPOINT + "content-type=application/json")
                    response = conn.getresponse()

                    d = json.loads(response.read().decode())
                    contents = read_html_file("geneInfo.html").render(context={"start": d["start"],
                                                                               "end": d["end"],
                                                                               "length": int(d["end"]) - int(d["start"]),
                                                                               "id": gene_id,
                                                                              "gene": gene,
                                                                               "chromo": d["seq_region_name"]})

                except:
                    status = 404
                    contents = Path('html/error.html').read_text()

            elif path =="/geneCalc":
                try:
                    gene = arguments["gene"][0].upper()
                    seq = Seq(get_seq(arguments))
                    output = ""
                    for base, count in seq.count().items():
                        percent = count / len(seq.__str__()) * 100
                        output += f"{base}: {count} ({round(percent, 1)}%)<br>"
                    print(output)
                    contents = read_html_file("geneCalc.html").render(context={"length": len(seq.__str__()),
                                                                               "percentage": output,
                                                                                "gene": gene})

                except:
                    status = 404
                    contents = Path('html/error.html').read_text()

            elif path == "/geneList":
                try:
                    chromo = arguments["chromo"][0]
                    start = arguments["start"][0]
                    end = arguments["end"][0]
                    ENDPOINT = f'/overlap/region/human/{chromo}:{start}-{end}?feature=gene;feature=transcript;feature=cds;feature=exon;'
                    conn = http.client.HTTPSConnection(SERVER)
                    conn.request("GET", ENDPOINT + "content-type=application/json")
                    response = conn.getresponse()
                    lst = json.loads(response.read().decode())
                    region = ""
                    for gene in lst:
                        id = gene["id"]
                        gene = get_name(id)
                        str_gene = gene[0] + gene[1]
                        region += "<li>" + str_gene + "</li>"
                    contents = read_html_file("geneList.html").render(context={"chromo": chromo,
                                                                               "start": start,
                                                                               "end": end,
                                                                               "region": region})

                except:
                    status = 404
                    contents = Path('html/error.html').read_text()

            else:
                contents = Path('html/error.html').read_text()

        except:
            status = 404
            contents = Path('html/error.html').read_text()

        # Generating the response message
        self.send_response(status)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
