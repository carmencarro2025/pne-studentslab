lines = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]

f = open("dna.txt", "r") # r means we are reading through the file

from dna_count import count_bases

# Option 1
lines = f.readlines()
f.close() # At the end of the code, in order to avoid problems with different terminals
print("From file:", lines) # We get: From file: ['AGTACACTGGT\n', 'ACCAGTGTACT\n', 'ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG\n']

# Option 2
with open("dna.txt", "r") as f:
    lines = f.readlines() # These two lines runs the same as the three above, CLOSE FUNCTION automatically closed

total_number = 0
bases = {"A": 0, "C": 0, "G": 0, "T": 0}

for seq in lines:
    seq = seq.strip() # Remove spaces and newline characters at the end of the string
    total_number += len(seq)

    result = count_bases(seq)

print("Total number of bases:", total_number)

for base, count in bases.items():
    print(f"{base}: {count}")



