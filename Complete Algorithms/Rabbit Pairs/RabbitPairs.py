def rabbit_pairs(months, litter):
    output_arr = [0 for x in range(months)]
    output_arr[0] = 1 # first generation are not reproduction-aged yet
    output_arr[1] = 1 # now first generation is reproduction-aged
    i = 2
    while i < months:
        # the next index of the array is = previous index + previous-previous index * size of litter
        output_arr[i] = output_arr[i-1] + output_arr[i-2]*litter
        i += 1
    print(output_arr)
    return output_arr[months-1]

months = 32
litter = 3

print(rabbit_pairs(months, litter))
