from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

SEQUENCES = "../P00/S04/Sequences/"
GENE_NAMES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in GENE_NAMES:
    s = Seq()
    FILENAME = SEQUENCES + gene + ".txt"
    s.read_fasta(FILENAME)
    d = s.count()
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    first_base = sorted_d[0][0]
    print(f"Gene {gene}: Most frequent Base: {first_base}")