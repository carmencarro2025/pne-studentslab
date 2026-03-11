from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 8080
IP = "127.0.0.1"
c = Client(IP, PORT)
print(c)

seq = c.talk(f"GET 0")
GENE_NAMES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("* Testing PING...")
r1 = c.talk("PING")
print(r1)

print("* Testing GET...")
i = 0
while i < 5:
    r2 = c.talk(f"GET {i}")
    print(f"GET {i}: {r2}")
    i += 1

print("\n* Testing INFO...")
r3 = c.talk(f"INFO {seq}")
print(r3)

print("* Testing COMP...")
r4 = c.talk(f"COMP {seq}")
print(r4)

print("\n* Testing REV...")
r5 = c.talk(f"REV {seq}")
print(r5)

print("\n* Testing GENE...")
j = 0
for gene in GENE_NAMES:
    print(f"GENE {gene}")
    r6 = c.talk(f"GENE {gene}")
    print(r6)
    print()
    j += 1

