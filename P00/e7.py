from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    print("-----| Exercise 7 |------")
    SEQUENCES = "S04/Sequences/"
    FILENAME = "U5"
    print(F"Gene {FILENAME}:")
    file_contents = Path(SEQUENCES + FILENAME + ".txt").read_text()
    print(f"Comp: {seq_complement(file_contents)}")
