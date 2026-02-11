if __name__ == "__main__":

    dna = "ATGCGATCGATCGATCGATCGA"

    print(f"Length: {len(dna)}")
    print(f"First 5: {dna[:5]}")
    print(f"Last 3: {dna[-3:]}")
    print(f"Lowercase: {dna.lower()}")
    print(f"ATC count: {dna.count('ATC')} ")
    print(f"RNA: {dna.replace("T", "U")}")

