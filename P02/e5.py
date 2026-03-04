from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.77" # your IP address
PORT = 8081

c = Client(IP, PORT)
print(c)
c.__str__()
SEQUENCES = "../P00/S04/Sequences/"
s = Seq()
FILENAME = SEQUENCES + "FRAT1" + ".txt"
s.read_fasta(FILENAME)
print(f"Gene FRAT1: {s.__str__()}")
response = c.talk(s.__str__())
print(f"From server: {response}")
print(f"To server: {s.__str__()}\n")