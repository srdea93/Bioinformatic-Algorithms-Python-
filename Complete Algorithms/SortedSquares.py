# given a list of sorted pos and neg integers, return a list with the squares in
# sorted order without using a sort function
def squares(input):
    output = []
    input_sq = []
    for num in input:
       input_sq.append(num*num)

    # find the minimum index of the squared values
    min_index = input_sq.index(min(input_sq))

    # create left pointer and right pointer
    left = min_index - 1
    right = min_index + 1

    output.append(input_sq[min_index])

    while len(output) != len(input):
        # check if left is within range
        if left < 0 and right > len(input_sq)-1:
            break
        # go right
        elif left < 0:
            output.append(input_sq[right])
            right += 1
        # go left
        elif right > len(input) - 1:
            output.append(input_sq[left])
            left -= 1
        # if left < right, add left to output
        else:
            if input_sq[left] < input_sq[right]:
                output.append(input_sq[left])
                # move left pointer to the left
                left = left - 1
            # if left > right, add right to output
            else:
                output.append(input_sq[right])
                # move right pointer to the right
                right = right + 1
    print(output)

input = [-6, -5, -4, -3, -2, -1]
squares(input)


