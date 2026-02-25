from Seq1 import Seq
from pathlib import Path

print("-----| Practice 1, Exercise 9 |------")
# -- Create a Null sequence
s = Seq()

SEQUENCES = "S04/Sequences/"
FILENAME = "U5.txt"
print(s.read_fasta(SEQUENCES + FILENAME))

print(f"Sequence : (Length:{s.len()}) {s}")
print(f"  Bases: {s.count()}")
print(f"  Rev: {s.reverse()}")
print(f"  Comp: {s.complement()}")
