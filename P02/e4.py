from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1" # your IP address
PORT = 8080

c = Client(IP, PORT)
print(c)

SEQUENCES = "../P00/S04/Sequences/"
GENE_NAMES = ["U5", "ADA", "FRAT1"]
s = Seq()
for gene in GENE_NAMES:
    response1 = c.talk(f"Sending the {gene} Gene to the server...")
    print(f"To server: Sending the {gene} Gene to the server...")
    print(f"From server: {response1}")
    FILENAME = SEQUENCES + gene + ".txt"
    s.read_fasta(FILENAME)
    response2 = c.talk(s.__str__())
    print(f"To server: {s.__str__()}")
    print(f"From server: {response2}\n")

