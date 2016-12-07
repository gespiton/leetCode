help(dict)


def twoSum(arr, target):
    seem = {}
    e = int(len(arr) / 2) + 1
    for i, v in enumerate(arr):
        if i >= e or v >= target:
            return;
        else:
            if seem.get(target - v) is not None:
                return seem[target - v] + 1, i + 1
            seem[v] = i


print(twoSum([1, 1, 1, 1, 4, 3, 2, 1], 5))
