from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    print("-----| Exercise 6 |------")
    SEQUENCES = "S04/Sequences/"
    FILENAME = "U5"
    print(F"Gene {FILENAME}")
    file_contents = Path(SEQUENCES + FILENAME + ".txt").read_text()
    print(f"Reverse: {seq_reverse(file_contents, 20)}")
