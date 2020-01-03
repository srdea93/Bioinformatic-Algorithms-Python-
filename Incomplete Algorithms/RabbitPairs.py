def rabbit_pairs(months, litter):
    output_arr = [0 for x in range(months)]
    output_arr[0] = 1
    output_arr[1] = 1
    i = 2
    while i < months:
        output_arr[i] = output_arr[i-1] + output_arr[i-1]*litter
        i += 1
    print(output_arr)
    return output_arr[months-1]

months = 5
litter = 3

print(rabbit_pairs(months, litter))
