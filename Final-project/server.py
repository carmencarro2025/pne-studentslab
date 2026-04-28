import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import termcolor
from pathlib import Path
import jinja2 as j
import json

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

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

        # Print the request line
        global info, output
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path  # "/echo"
        arguments = parse_qs(url_path.query)

        if path == "/":
            contents = Path('html/index.html').read_text()

        elif path == "/listSpecies":
            ENDPOINT = '/info/species'
            conn = http.client.HTTPSConnection(SERVER)
            conn.request("GET", ENDPOINT + PARAMS)
            response = conn.getresponse()

            d = json.loads(response.read().decode())
            list_species = d["species"]
            print(list_species)
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
            print(arguments)
            contents = read_html_file("listSpecies.html").render(context={"limit": limit,
                                                                              "names": names,
                                                                              "num_species": len(list_species)})

        elif path == "/karyotype":
            ENDPOINT = f'/info/assembly/{arguments["species"][0]}'
            conn = http.client.HTTPSConnection(SERVER)
            conn.request("GET", ENDPOINT + PARAMS)
            response = conn.getresponse()

            d = json.loads(response.read().decode())
            karyotype = d["karyotype"]
            kar = ""
            for n in karyotype:
                kar += n + "<br>"

            contents = read_html_file("karyotype.html").render(context={"kar": kar})

        elif path == "/chromosomeLength":
            pass




        else:
            contents = Path('html/error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

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
