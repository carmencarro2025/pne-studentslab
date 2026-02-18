from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    SEQUENCES = "S04/Sequences/"
    FILENAME = "U5.txt"
    print(F"DNA file: {FILENAME}")
    file_contents = Path(SEQUENCES + FILENAME).read_text()
    print(f"The first 20 bases are:\n{seq_read_fasta(file_contents)[:20]}")

