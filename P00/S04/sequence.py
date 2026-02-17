from pathlib import Path

FILENAME = "Sequences/ADA.txt"

file_contents = Path(FILENAME).read_text()

def body(seq):
    body = seq.find("\n")
    seq = seq[body:]
    seq = seq.replace("\n", "")
    return len(seq)

print(f"Total number of bases of the ADA.txt file: {body(file_contents)}")
