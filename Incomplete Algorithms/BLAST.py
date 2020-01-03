# given two DNA sequences find minimum cost
# deletion/insertion = 2
# mutation = 1
# same = 0

# simplified version with indels and mutations counting for the same distance
seq1 = "AGCGTG"
seq2 = "GCGCC"

def min_cost_blast(seq1, seq2):
    m = len(seq1) + 1
    n = len(seq2) + 1
    indel = 1
    mutation = 1
    same = 0

    matrix = [[0 for x in range(m)]for y in range(n)]
    for i in range(1, m):
        matrix[0][i] = matrix[0][i-1] + indel
    for j in range(1, n):
        matrix[j][0] = matrix[j-1][0] + indel

    for i in range(1, m):
        for j in range(1, n):
            above = matrix[j-1][i]
            left = matrix[j][i-1]
            diagonal = matrix[j-1][i-1]
            if seq1[i-1] == seq2[j-1]:
                matrix[j][i] = same + min(above, left, diagonal)
            else:
                matrix[j][i] = 1 + min(above, left, diagonal)

    for row in matrix:
        print(row)




    # fill in the first of each row

    # fill in the first of each col


min_cost_blast(seq1, seq2)
