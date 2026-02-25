from Seq1 import Seq

print("-----| Practice 1, Exercise 7 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

seqs = [s1, s2, s3]
i = 1
BASES = ["A", "C", "T", "G"]
for seq in seqs:
    print(f"Sequence {i}: (Length:{seq.len()}) {seq}")
    print(f"  Bases: {seq.count()}")
    print(f"  Rev: {seq.reverse()}")
    i += 1

