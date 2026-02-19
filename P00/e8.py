from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    print("-----| Exercise 8 |------")
    SEQUENCES = "S04/Sequences/"
    GENE_NAMES = ["U5", "ADA", "FRAT1", "FXN"]
    for gene in GENE_NAMES:
        file_name = gene + ".txt"
        file = Path(SEQUENCES + file_name).read_text()
        d = seq_count(file)
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        first_base = sorted_d[0][0]
        print(f"Gene {gene}: Most frequent Base: {first_base}")
