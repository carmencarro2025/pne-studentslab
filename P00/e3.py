from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    SEQUENCES = "S04/Sequences/"
    GENE_NAMES = ["U5", "ADA", "FRAT1", "FXN"]
    print("-----| Exercise 3 |------")
    for gene in GENE_NAMES:
        file_name = gene + ".txt"
        file = Path(SEQUENCES + file_name).read_text()
        print(f"Gene U5 -> Length: {seq_len(file)}")
