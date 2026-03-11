import socket
from Seq1 import Seq

PORT = 8080
IP = "212.128.255.78"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("SEQ server configured!")

while True:
    print("Waiting for Clients...")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:


        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()
        l = msg.strip().split(" ")
        cmd = l[0]
        n = l[1]

        sequences = ["AAAA", "TTTT", "CCCC", "GGGG", "TATA"]


        SEQUENCES = "../P00/S04/Sequences/"
        GENE_NAMES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

        if cmd == "PING":
            print("PING command!")
            print("OK!\n")
            response = "OK!\n"
            cs.send(response.encode())

        elif cmd == "GET" and 0 <= int(n) <= 4:
            print("GET")
            print(sequences[int(n)])
            print()

        elif cmd == "INFO":
            print("INFO")
            s = Seq(n)
            print(f"Sequence: {s}")
            print(f"Total length: {s.len()}")
            for base, count in s.count().items():
                percent = count / s.len() * 100
                print(f"{base}: {count} ({round(percent, 1)}%)")
            print()

        elif cmd == "COMP":
            print("COMP")
            s = Seq(n)
            print(s.complement())
            print()

        elif cmd == "REV":
            print("REV")
            s = Seq(n)
            print(s.reverse())
            print()

        elif cmd == "GENE" and n in GENE_NAMES:
            print("GENE")
            s = Seq()
            FILENAME = SEQUENCES + n + ".txt"
            s.read_fasta(FILENAME)
            print(s.__str__())
            print()




        # -- Close the data socket
        cs.close()


