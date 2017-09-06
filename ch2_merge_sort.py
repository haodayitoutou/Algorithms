def merge(nums, low, mid, high):
    i = low
    j = mid + 1
    aux = []

    for _ in range(high-low+1):
        if i > mid:
            aux.append(nums[j])
            j += 1
        elif j > high:
            aux.append(nums[i])
            i += 1
        elif nums[i] < nums[j]:
            aux.append(nums[i])
            i += 1
        else:
            aux.append(nums[j])
            j += 1

    nums[low: high+1] = aux


def mergesort(nums, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergesort(nums, low, mid)
    mergesort(nums, mid + 1, high)
    merge(nums, low, mid, high)


def test_merge():
    a_list = ["E", "E", "G", "M", "R", "A", "C", "E", "R", "T"]
    merge(a_list, 0, len(a_list)//2 - 1, len(a_list) - 1)
    print(a_list)


def test_sort():
    a_list = ["M", "E", "R", "G", "E", "S", "O", "R",
              "T", "E", "X", "A", "M", "P", "L", "E"]
    mergesort(a_list, 0, len(a_list) - 1)
    print(a_list)


test_merge()
test_sort()
