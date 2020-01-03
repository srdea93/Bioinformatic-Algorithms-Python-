# given an array of coin values, try to make the least amount of change possible
def make_change(change_arr, value):
    change_arr.sort(reverse = True)
    count = 0
    for change in change_arr:
        count = count + value % change
    return count


change_arr = [1, 2, 5]
value = 13
print(make_change(change_arr, value))