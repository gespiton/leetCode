"""
   O(nlogN) time O(1) space , i got it baby
"""


def search(arr, target):
    for i, v in enumerate(arr):
        if v > target:
            continue
        else:
            second = bsearch(arr, 0, len(arr), target - v)
            if second is not None:
                return i + 1, second + 1


def bsearch(arr, s, e, target):
    if s == e:
        return
    mid = int((e + s) / 2)

    if arr[mid] != target:
        if arr[mid] > target:
            return bsearch(arr, s, mid, target)
        else:
            return bsearch(arr, mid + 1, e, target)
    else:
        return mid


print(search([0, 1, 2, 3, 4, 6, 9, 10], 12))
