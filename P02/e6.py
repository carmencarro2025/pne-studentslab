from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

SEQUENCES = "../P00/S04/Sequences/"
s = Seq()
FILENAME = SEQUENCES + "FRAT1" + ".txt"
s.read_fasta(FILENAME)
s_str = s.__str__()
print(f"Gene FRAT1: {s_str}")


IP = "127.0.0.1"
c1 = Client(IP, 8080)
c1.talk(f"Sending FRAT1 Gene to the server, in fragments of 10 bases...")
print(c1)
c2 = Client(IP, 8081)
c2.talk(f"Sending FRAT1 Gene to the server, in fragments of 10 bases...")
print(c2)

i = 0
n = 1
while n <= 10:
    if n % 2 != 0:
        print(f"Fragment {n}: {s_str[i:i + 10]}")
        c1.talk(f"Fragment {n}: {s_str[i:i + 10]}")
    else:
        print(f"Fragment {n}: {s_str[i:i + 10]}")
        c2.talk(f"Fragment {n}: {s_str[i:i + 10]}")
    i += 10
    n += 1







