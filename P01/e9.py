from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
FILENAME = "../P00/S04/Sequences/U5.txt"
s.read_fasta(FILENAME)

print(f"Sequence : (Length:{s.len()}) {s}")
print(f"  Bases: {s.count()}")
print(f"  Rev: {s.reverse()}")
print(f"  Comp: {s.complement()}")
