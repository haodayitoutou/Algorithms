def partition(nums, low, high):
    if low == high:
        return low
    i = low + 1
    j = high
    value = nums[low]

    while True:
        while nums[i] < value and i < high:
            i += 1
        while nums[j] > value:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick_sort(nums, low, high):
    """
    Length N with distince keys: 2NlnN compares +
     1/6 that many exchanges on the average.
    """
    if low >= high:
        return
    j = partition(nums, low, high)
    quick_sort(nums, low, j - 1)
    quick_sort(nums, j + 1, high)


def quick_sort_3way(nums, low, high):
    if low >= high:
        return

    i = low + 1
    less = low
    greater = high
    value = nums[low]
    while i <= greater:
        if nums[i] < value:
            nums[less], nums[i] = nums[i], nums[less]
            i += 1
            less += 1
        elif nums[i] > value:
            nums[greater], nums[i] = nums[i], nums[greater]
            greater -= 1
        else:
            i += 1

    quick_sort_3way(nums, low, less-1)
    quick_sort_3way(nums, greater+1, high)


def test_partition():
    input_list = [[1],
                  [1, 2],
                  [1, 2, 3, 4, 5],
                  [5, 4, 3, 2, 1],
                  [3, 2, 4, 5, 6, 1]]

    for a_list in input_list:
        print(partition(a_list, 0, len(a_list) - 1))


def test_quick_sort():
    input_list = [[1],
                  [1, 2],
                  [3, 2, 4, 5, 6, 1],
                  ["Q", "W", "E", "R", "T", "Y", "U", "I", "O",
                   "P", "A", "S", "D", "F", "G", "H", "J", "K",
                   "L", "Z", "X", "C", "V", "B", "N", "M"]]

    for a_list in input_list:
        quick_sort(a_list, 0, len(a_list) - 1)
        print(a_list)


def test_quick_sort_3way():
    input_list = [[1],
                  [1, 2],
                  [3, 2, 4, 5, 6, 1],
                  ["Q", "W", "E", "R", "T", "Y", "U", "I", "O",
                   "P", "A", "S", "D", "F", "G", "H", "J", "K",
                   "L", "Z", "X", "C", "V", "B", "N", "M"],
                  ["R", "B", "W", "W", "R", "W", "B", "R", "R", "W", "B", "R"],
                  ["W", "W", "W", "W", "B"]]

    for a_list in input_list:
        quick_sort_3way(a_list, 0, len(a_list) - 1)
        print(a_list)


# test_partition()
# test_quick_sort()
test_quick_sort_3way()
