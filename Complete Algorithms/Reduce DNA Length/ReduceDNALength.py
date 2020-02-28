# Given DNA string, reduce it so numbers in front of DNA letter
# "AAAGGCCTTA" -> "3A2G2C2T1A"
def reduce_DNA(text):
    # account for lower case letters
    dna = ["A", "C", "G", "T"]
    text = text.upper()
    count = 1
    output = ""
    for i in range(1, len(text)+1):
        if text[i-1] not in dna:
            print("Not valid DNA sequence")
            return
        else:
            if i == len(text):
                output = output + str(count) + str(text[i-1])
            elif text[i] == text[i-1]:
                count += 1
            else:
                output = output + str(count) + str(text[i-1])
                count = 1
    return output

text = "AAAGGCCTTAaaaf"
print(reduce_DNA(text))


