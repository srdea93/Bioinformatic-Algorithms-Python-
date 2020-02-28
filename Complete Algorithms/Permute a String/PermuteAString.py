# Recursion demonstration
def factorial_recursion(number):
    if number == 1:
        return 1
    else:
        return number * factorial_recursion(number-1)

# print(factorial_recursion(5))


def to_string(list):
    return "".join(list)


# Given a string, print all permutations of that string
def string_permutations(string, start, end):
    # turn string into a list of characters for index swapping later
    string = list(string)
    # if the start value of a recursive call = end value, print the string that is saved
    if start == end:
        print(to_string(string))
    else:
        for i in range(start, len(string)):
            # swap values at index start and whatever iteration we are on
            string[start], string[i] = string[i], string[start]

            # recursive call with start + 1
            string_permutations(string, start + 1, end)

            # backtracking
            string[start], string[i] = string[i], string[start]


# string_permutations("vinnie", 0, len("vinnie") - 1)


def sentence_permutation(sentence, start, end):
    if start == end:
        print(sentence)
    else:
        for i in range(start, len(sentence)):
            sentence[start], sentence[i] = sentence[i], sentence[start]
            sentence_permutation(sentence, start + 1, end)
            sentence[start], sentence[i] = sentence[i], sentence[start]


sentence = ["Hello", "my", "name", "is", "Steven"]
sentence_permutation(sentence, 0, len(sentence))