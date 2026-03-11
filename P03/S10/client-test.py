from Client0 import Client

IP = "212.128.254.248"
PORT = 8080

c = Client(IP, PORT)
print(c)

i = 0
while i < 5:
    response = c.talk(f"Message {i}")
    print(f"To server: Message {i}")
    print(f"From server: {response}")
    i += 1