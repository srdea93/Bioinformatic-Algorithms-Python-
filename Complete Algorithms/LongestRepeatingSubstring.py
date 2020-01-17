def longest_repeating_substring(string):
    # hashtable used to calculate hash for letters and once it is calculated once, can be retrieved with O(1)
    hash_table = []
    # define sliding window size at max - 1: go from largest to smallest
    k = len(string) - 1
    while k > 1:
        for i in range(len(string) - k + 1):
            string_hash = ascii(string[i:i+k])
            if string_hash in hash_table:
                print(string[i:i+k])
                return
            else:
                hash_table.append(string_hash)
        k -= 1
    if k == 1:
        print("No repeating substrings found.")
        return

longest_repeating_substring("aaaagggttttcccaaaatttt")