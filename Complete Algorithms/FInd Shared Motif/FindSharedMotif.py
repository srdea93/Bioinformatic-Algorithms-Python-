# find and return the longest common substring given multiple DNA sequences
def find_shared_motif(file):
    with open(file) as f:
        file_list = [line.rstrip() for line in f]

    # add all DNA sequences to a list
    dna_list = []
    dna_string = ""
    first = True
    for line in file_list:
        if first == True:
            first = False
        elif line[0] == ">":
            dna_list.append(dna_string)
            dna_string = ""
        else:
            dna_string = dna_string + line
    # add last dna_string
    dna_list.append(dna_string)

    # start with sliding window of highest length and work way down
    # find all motifs of window size k in first seq and compare
    # remove motifs that do not match others
    # find all motifs of window size k - 1 in first seq and compare
    motif_list = []
    found = False
    k = len(min(dna_list))
    # starting window size & iterate down
    while(found == False and k > 0):
        # add to motif list
        for i in range(len(dna_list[0]) - k + 1):
            if dna_list[0][i:i + k] not in motif_list:
                motif_list.append(dna_list[0][i:i + k])
            else:
                pass
        # print(motif_list)

        # Motif removal
        remove_motif =[]

        # remove motifs from motif list if they are not found in the others
        for motif in motif_list: #List of substrings
            keep_going = True
            for seq in dna_list: #List of DNA strings
                if keep_going == True:
                    for i in range(len(seq) - k + 1): # Comparison of other DNA strings to substrings
                        if (i+k) == len(seq):
                            if seq[i:i+k] != motif:
                                # motif_list.remove(motif)
                                remove_motif.append(motif)
                                keep_going = False
                                break
                        elif seq[i:i+k] == motif:
                            break

        motif_list = [x for x in motif_list if x not in remove_motif]
        if not motif_list:
            k = k-1
        else:
            found = True
    print(motif_list)
    return motif_list

find_shared_motif("FindSharedMotifTest")