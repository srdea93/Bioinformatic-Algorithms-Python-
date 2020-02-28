def is_DNA(letter):
    DNA = ['A', 'C', 'T', 'G']
    if letter not in DNA:
        return False
    else:
        return True

def pattern_count(text, pattern):
    count = 0
    # check each sliding window of pattern size ex. A T C A A T, pattern = ATC (range 0-3)
    for i in range(len(text) - len(pattern)+1):
        if is_DNA(text[i]) == False:
            print("Invalid sequence")
            break
        else:
            # slice is NOT inclusive of the last number ex. index 0-2
            if text[i:i+len(pattern)] == pattern:
                count += 1
            else:
                pass
    return count

# given a text and a pattern length, determine most frequent
def most_freq_pattern(text, k):
    patterns = {}
    # k + 1 because range is NOT inclusive
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        # dont need to do anything because already found all the counts of that pattern
        if pattern in patterns:
            pass
        else:
            count = pattern_count(text, pattern)
            patterns[pattern] = count
    print(patterns)
    print("Pattern with max counts: " + max(patterns, key=patterns.get) + ": " + str(patterns[max(patterns, key = patterns.get)]))

text = "AGTCCCGATAAAGTACGATACCACTGAGTAGT"
k = 3
most_freq_pattern(text, k)