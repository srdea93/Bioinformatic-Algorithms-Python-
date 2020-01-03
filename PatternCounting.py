def is_DNA(letter):
    DNA = ['A', 'C', 'T', 'G']
    if letter not in DNA:
        return False
    else:
        return True

def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern)-1):
        if is_DNA(text[i]) == False:
            print("Invalid sequence")
            break
        else:
            if text[i:i+len(pattern)] == pattern:
                count += 1
            else:
                pass
    return count

# given a text and a pattern length, determine most frequent
def most_freq_pattern(text, k):
    patterns = {}
    for i in range(len(text) - k-1):
        pattern = text[i:i+k]
        if pattern in patterns:
            pass
        else:
            count = pattern_count(text, pattern)
            patterns[pattern] = count
    print(patterns)
    print("Pattern with max counts: " + max(patterns, key=patterns.get) + ": " + str(patterns[max(patterns, key = patterns.get)]))