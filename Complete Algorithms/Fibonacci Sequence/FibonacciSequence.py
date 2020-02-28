def fib(number):
    fib_list = [0 for x in range(number)]
    fib_list[0] = 1
    fib_list[1] = 1
    i = 2
    while i < number:
        new_num = fib_list[i-2] + fib_list[i-1]
        fib_list[i] = new_num
        i += 1
    print(fib_list)
    print(fib_list[number-1])
    return fib_list

number = 20
fib(number)