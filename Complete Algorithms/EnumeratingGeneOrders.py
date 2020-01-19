# 1 2 3 4 5 6
def create_num_array(num):
    num_array = []
    for i in range(1, num + 1):
        num_array.append(i)
    return num_array

def factorial_recursion(number):
    if number == 1:
        return 1
    else:
        return number * factorial_recursion(number-1)

def enumerating_gene_orders(num_array, start, end):
    # recursive call of Heap's algorithm
    if start == end:
        # use map in conjunction with join to merge the lists of number permutations into strings
        print(", ".join(map(str, num_array)))
    else:
        for i in range(start, len(num_array)):
            num_array[start], num_array[i] = num_array[i], num_array[start]
            enumerating_gene_orders(num_array, start + 1, end)
            num_array[start], num_array[i] = num_array[i], num_array[start]

number = 3
num_array = create_num_array(number)
print(factorial_recursion(number))
enumerating_gene_orders(num_array, 0, len(num_array) - 1)