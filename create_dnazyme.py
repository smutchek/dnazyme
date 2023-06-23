#define vars
HD3_catalytic = "ATGAAGGATCGGCGTGTCGGGGCAA" #3' to 5', so it can be reversed with the sequence later
#RNA = "rGrCrArGrArCrUrCrArCrUrArUrArGrGrArGrArCrGrArCrCrCrGrArG"
print("Enter RNA sequence separated by r delim")
RNA = input()

def dnazyme(rna_sequence):
    seq = rna_sequence.split("r")
    halflen = len(seq)//2
    if((seq[halflen] != 'A') or (seq[halflen+1] != 'G') or (seq[halflen+2] != 'G')):
       # print("Sequence does not contain AGG in its center.")
        return("Sequence does not contain AGG in its center.")
    dnazyme35 = ""
    for index, nt in enumerate(seq):
        if index == (halflen):
            dnazyme35 += "ATGAAGGATCGGCGTGTCGGGGCAA"
            continue
        elif index == (halflen+1):
            continue
        elif index == (halflen+2):
            continue
        elif nt == 'A':
            dnazyme35 += "T"
        elif nt == 'U':
            dnazyme35 += "A"
        elif nt == 'G':
            dnazyme35 += 'C'
        elif nt == 'C':
            dnazyme35 += 'G'
    dnazyme53 = dnazyme35[::-1]
    return(dnazyme53)

print(dnazyme(RNA))