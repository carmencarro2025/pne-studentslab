def seq_ping():
    print("OK")

def seq_read_fasta(seq):
    body = seq.find("\n")
    seq = seq[body:]
    seq = seq.replace("\n", "")
    return seq

def seq_len(seq=None):
    body = seq.find("\n")
    seq = seq[body:]
    seq = seq.replace("\n", "")
    return len(seq)

def seq_count_base(seq, base=None):
    return seq.count(base)

def seq_count(seq):
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in seq:
        if base in bases:
            bases[base] += 1
    return bases

def seq_reverse(seq, n):
    body = seq.find("\n")
    seq = seq[body:]
    seq = seq.replace("\n", "")
    seq_n = seq[:n]
    print(f"Fragment: {seq_n}")
    reversed = seq_n[::-1]
    return reversed

def seq_complement(seq):
    complementary_bases = {"A": "U", "C": "G", "G": "C", "T": "A"}
    body = seq.find("\n")
    seq = seq[body:]
    seq = seq.replace("\n", "")
    seq = seq.replace("\n", "")
    seq_20 = seq[:20]
    print(f"Frag: {seq_20}")
    complementary_seq = ""
    for base in seq_20:
        complementary_seq += complementary_bases[base]
    return complementary_seq
