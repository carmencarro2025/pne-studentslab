class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases=None):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence created!")
        else:
            valid = True
            bases = "ACTG"
            for base in strbases:
                if base not in bases:
                    valid = False
            if not valid:
                self.strbases = "ERROR"
                print("INVALID sequence!")
            else:
                self.strbases = strbases
                print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            result = 0
        else:
            result = len(self.strbases)
        return result

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        bases = {"A": 0, "C": 0, "G": 0, "T": 0}
        for base in self.strbases:
            if base in bases:
                bases[base] += 1
        return bases

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            result = self.strbases
        else:
            result = self.strbases[::-1]
        return result

    def complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            result = self.strbases
        else:
            complementary_seq = ""
            complementary_bases = {"A": "T", "C": "G", "G": "C", "T": "A"}
            for base in self.strbases:
                complementary_seq += complementary_bases[base]
            result = complementary_seq
        return result

    def read_fasta(self, filename):
        body = filename.find("\n")
        seq = filename[body:]
        seq = seq.replace("\n", "")
        return seq


def print_seqs(seq_list):
    i = 1
    for seq in seq_list:
        print(f"Sequence {i}: (Length:{ seq.len()}) {seq}")
        i += 1
