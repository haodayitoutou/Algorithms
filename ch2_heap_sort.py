def sink(nums, idx, length):
    while idx <= length // 2:
        j = idx * 2
        if j < length and nums[j] < nums[j + 1]:
            j += 1
        if nums[idx] >= nums[j]:
            break
        nums[idx], nums[j] = nums[j], nums[idx]
        idx = j


def heap_sort(nums):
    length = len(nums) - 1
    for k in reversed(range(1, length // 2 + 1)):
        sink(nums, k, length)

    while length > 1:
        nums[1], nums[length] = nums[length], nums[1]
        length -= 1
        sink(nums, 1, length)

    return nums


print(
    heap_sort(["0", "S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"])
)
