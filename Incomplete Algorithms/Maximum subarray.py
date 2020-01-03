def maxSubArray (numbers):
    curMax = 0
    maxArr = []
    for num in numbers:
        curMax = max(num, curMax + num)
        maxArr.append(curMax)
    return max(maxArr)

numbers = [5, 10, -2, -4, 6, 2, -10, 5, 3]
print(maxSubArray(numbers))
