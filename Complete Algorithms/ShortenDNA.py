def shortenDNA(text):
    dna_list = ["A", "C", "G", "T"]
    output = ""
    count = 1
    i = 1
    for i in range(1, len(text)):
        if text[i] not in dna_list:
            print("Invalid sequence")
            return
        elif text[i] == text[i-1]:
            count += 1
        else:
            output = output + str(count) + text[i-1]
            count = 1
    output = output + str(count) + text[-1]
    print(output)

text = "ACCCCGGTTTTAA"
shortenDNA(text)