from Client0 import Client
from Seq1 import Seq

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 8080
IP = "212.128.255.78"
c = Client(IP, PORT)
print(c)

print("* Testing PING...")
c.talk("PING")

print("* Testing GET...")
