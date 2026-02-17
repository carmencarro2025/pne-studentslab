from pathlib import Path

FILENAME = "Sequences/U5.txt"

file_contents = Path(FILENAME).read_text()

def body(seq):
    body = seq.find("\n")
    seq = seq[body:]
    return seq

print(f"Body of the U5.txt file:{body(file_contents)}")