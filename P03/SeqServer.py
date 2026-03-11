import socket
from Seq1 import Seq

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

        seq = ["AAAA", "TTTT", "CCCC", "GGGG", "TATA"]

        SEQUENCES = "../P00/S04/Sequences/"
        GENE_NAMES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

        if cmd == "PING":
            print("PING command!")
            print("OK!\n")
            r1 = "OK!\n"
            cs.send(r1.encode())

        elif cmd == "GET" and 0 <= int(l[1]) <= 4:
            print("GET")
            r2 = seq[int(l[1])]
            print(r2)
            cs.send(r2.encode())
            print()

        elif cmd == "INFO":
            print("INFO")
            s = Seq(l[1])
            r3 = f"Sequence: {s}\n"
            r3 += f"Total length: {s.len()}\n"
            for base, count in s.count().items():
                if s.len() > 0:
                    percent = count / s.len() * 100
                    r3 += f"{base}: {count} ({round(percent, 1)}%)\n"
                else:
                    r3 += f"{base}: {count}\n"
            print(r3)
            cs.send(r3.encode())
            print()

        elif cmd == "COMP":
            print("COMP")
            s = Seq(l[1])
            r4 = s.complement()
            print(r4)
            cs.send(r4.encode())
            print()

        elif cmd == "REV":
            print("REV")
            s = Seq(l[1])
            r5 = s.reverse()
            print(r5)
            cs.send(r5.encode())
            print()

        elif cmd == "GENE" and l[1] in GENE_NAMES:
            print("GENE")
            s = Seq()
            FILENAME = SEQUENCES + l[1] + ".txt"
            s.read_fasta(FILENAME)
            r6 = s.__str__()
            print(r6)
            cs.send(r6.encode())
            print()

        # -- Close the data socket
        cs.close()


