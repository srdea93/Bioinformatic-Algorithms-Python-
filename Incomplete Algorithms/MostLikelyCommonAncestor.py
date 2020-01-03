def most_likely_common_ancestor(dna1, dna2, dna3, dna4, dna5, dna6, dna7):
    dna_matrix = [[dna1], [dna2], [dna3], [dna4], [dna5], [dna6], [dna7]]
    for list in dna_matrix:
        print(list)
    dna_counts = [[0 for x in range(len(dna_matrix[0][0]))] for y in range(1,5)]
    for dna in dna_counts:
        print(dna)
    for list in dna_matrix:
        for dna in list:
            pass

dna1 = "ATCCAGCT"
dna2 = "GGGCAACT"
dna3 = "ATGGATCT"
dna4 = "AAGCAACC"
dna5 = "TTGGAACT"
dna6 = "ATGCCATT"
dna7 = "ATGGCACT"

most_likely_common_ancestor(dna1, dna2, dna3, dna4, dna5, dna6, dna7)
