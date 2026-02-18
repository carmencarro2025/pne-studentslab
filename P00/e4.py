from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    print("-----| Exercise 4 |------")
    SEQUENCES = "S04/Sequences/"
    GENE_NAMES = ["U5", "ADA", "FRAT1", "FXN"]
    for gene in GENE_NAMES:
        print(f"\nGene {gene}:")
        file_name = gene + ".txt"
        file = Path(SEQUENCES + file_name).read_text()
        BASES = ["A", "C", "G", "T"]
        for base in BASES:
            print(f"  {base}: {seq_count_base(file, base)}")