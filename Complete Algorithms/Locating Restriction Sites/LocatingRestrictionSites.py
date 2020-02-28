def DNA_compliment(text):
    compliment = []
    rev_text = text[::-1]
    for letter in rev_text:
        if letter == "A":
            compliment.append("T")
        elif letter == "T":
            compliment.append("A")
        elif letter == "G":
            compliment.append("C")
        elif letter == "C":
            compliment.append("G")
        else:
            print("Invalid sequence")
            return
    compliment = "".join(compliment)
    return compliment

def restriction_sites(file):
    sequence = ""
    with open(file) as f:
        file_list = [line.strip() for line in f]
        for line in file_list:
            if line[0] == ">":
                pass
            else:
                sequence = sequence + line
    output = [] # list of tuples
    w = 4 # starting sliding window
    while w < 13:
        for i in range(len(sequence) - w + 1): # keep within the string size
            str_window = list(sequence[i:i+w])
            if list(str_window) == list(DNA_compliment(str_window)):
                output_tup = (i+1, w) # add 1 to i for the correct position
                output.append(output_tup)
            else:
                pass
        w += 1
    for tuple in output:
        print (str(tuple[0]) + " " + str(tuple[1]))

input = "LocatingRestrictionSites.txt"
restriction_sites(input)
