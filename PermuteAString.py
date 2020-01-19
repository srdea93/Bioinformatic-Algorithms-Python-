# Recursion demonstration
def factorial_recursion(number):
    if number == 1:
        return 1
    else:
        return number * factorial_recursion(number-1)

# print(factorial_recursion(5))

def toString(list):
    return "".join(list)

#Given a string, print all permutations of that string
def string_permutations(string, start, end):
    # turn string into a list of characters for index swapping later
    string = list(string)
    # if the start value of a recursive call = end value, print the string that is saved
    if start == end:
        print(toString(string))
    else:
        for i in range(start, len(string)):
            # swap values at index start and whatever iteration we are on
            string[start], string[i] = string[i], string[start]

            # recursive call with start + 1
            string_permutations(string, start + 1, end)

            # swap values at indexes again
            string[start], string[i] = string[i], string[start]

string_permutations("boat", 0, len("boat") - 1)