# given a collection of 10 DNA strings of same length, return consensus string and matrix profile for the collection
def most_likely_common_ancestor(file):
    dna_matrix = []
    dna_string = ""
    with open(file) as f:
        # remove new lines
        file_list = [line.strip() for line in f]
        start = True
        for line in file_list:
            if start:
                start = False
            elif line[0] == ">":
                dna_matrix.append(dna_string)
                dna_string = ""
            else:
                dna_string = dna_string + line
    # for seq in dna_matrix:
    #     print(seq)

    collection_matrix = [[0 for x in range(len(dna_matrix[0]))] for y in range(4)] # ACGT
    dna_list = ["A", "C", "G", "T"]

    # iterate every sequence and add the nucleotide to the collection matrix
    for seq in dna_matrix:
        # iterator through the collection_matrix
        i = 0
        for letter in seq:
            if letter == "A":
                collection_matrix[0][i] = collection_matrix[0][i] + 1
            elif letter == "C":
                collection_matrix[1][i] = collection_matrix[1][i] + 1
            elif letter == "G":
                collection_matrix[2][i] = collection_matrix[2][i] + 1
            else:
                collection_matrix[3][i] = collection_matrix[3][i] + 1
            i += 1

    # print collection matrix with proper formatting
    i = 0
    for row in collection_matrix:
        print_str = dna_list[i] + ":"
        for number in row:
            print_str = print_str + " " + str(number)
        print(print_str)
        print(len(row))
        i += 1

    # iterate through the collection matrix to find the max at each position
    # set max to A first and compare
    consensus_nums = collection_matrix[0]
    j = 0
    consensus_seq = ["A" for x in range(len(consensus_nums))]
    for nucleotide_list in collection_matrix:
        # iterator through the consensus_nums
        i = 0
        for number in nucleotide_list:
            if number > consensus_nums[i]:
                consensus_nums[i] = number
                if j == 0:
                    consensus_seq[i] = "A"
                elif j == 1:
                    consensus_seq[i] = "C"
                elif j == 2:
                    consensus_seq[i] = "G"
                else:
                    consensus_seq[i] = "T"
            i += 1
        j += 1

    consensus_str = ""
    for letter in consensus_seq:
        consensus_str += letter
    print(consensus_str)
    print(len(consensus_str))


file = "ConsensusAndProfile.txt"
most_likely_common_ancestor(file)
