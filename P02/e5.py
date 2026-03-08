from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.254.249" # your IP address
PORT = 8080

c = Client(IP, PORT)
print(c)

SEQUENCES = "../P00/S04/Sequences/"
s = Seq()
FILENAME = SEQUENCES + "FRAT1" + ".txt"
s.read_fasta(FILENAME)
s_str = s.__str__()
response1 = c.talk(f"Sending FRAT1 Gene to the server, in fragments of 10 bases...")
print(f"Gene FRAT1: {s_str}")

i = 0
n = 1
while n <= 5:
    print(f"Fragment {n}: {s_str[i:i + 10]}")
    response2 = c.talk(f"Fragment {n}: {s_str[i:i + 10]}")
    i += 10
    n += 1