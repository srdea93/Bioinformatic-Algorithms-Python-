def rna_to_protein(rna):
    # open the file and strip the lines of any excess characters
    with open(rna) as f:
        file_list = [line.strip() for line in f]

    # add each line of characters to a single string
    rna_string = ""
    for line in file_list:
        rna_string = rna_string + line

    # dictionary of rna to protein
    protein_dict = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
                    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
                    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
                    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
                    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
                    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
                    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
                    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

    # iterate through the string by every 3 characters
    i = 0
    protein_string = ""
    while i < len(rna_string):
        # slice every 3 characters
        rna_word = rna_string[i:i+3]
        protein_letter = protein_dict[rna_word]
        if protein_letter == "STOP":
            return protein_string
        else:
            protein_string = protein_string + protein_letter
        i = i + 3
    return protein_string


rna = "RNAtoProteinTest"
print(rna_to_protein(rna))