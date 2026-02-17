from pathlib import Path

FILENAME = "Sequences/RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()

def header(seq):
    header = seq.find("\n")
    seq = seq[:header]
    seq = seq.replace("\n", "")
    return seq

print(f"First line of the RNU6_269P.txt file:\n{header(file_contents)}")
