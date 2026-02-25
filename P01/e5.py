from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

seqs = [s1, s2, s3]
i = 1
BASES = ["A", "C", "T", "G"]
for seq in seqs:
    print(f"Sequence {i}: (Length:{seq.len()}) {seq}")
    i += 1
    for base in BASES:
        if base == "G":
            print(f"  {base}: {seq.count_base(base)}")
        else:
            print(f"  {base}: {seq.count_base(base)}", end=",")