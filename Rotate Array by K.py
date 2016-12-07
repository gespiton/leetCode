"""
page 13
Challenge 2:
Rotate an array to the right by k steps in-place without allocating extra space. For
instance, with k = 3, the array [0, 1, 2, 3, 4, 5, 6] is rotated to [4, 5, 6, 0, 1, 2, 3].
"""


def rotator(arr, steps):
    # if steps == len(arr):  # already in place, don't need to rotate
    #     return

    steps %= len(arr)  # make sure steps is best suitable
    if steps is 0:
        return arr

    counter = 0
    curP = 0 - steps
    buf = None

    while True:

        nextP = (curP + steps) % len(arr)
        _buf = buf
        buf = arr[nextP]
        arr[nextP] = _buf
        curP = nextP

        counter += 1
        if counter > len(arr):
            break

        if buf is None:
            curP += 1
            _buf = arr[curP]
            arr[curP] = buf
            buf = _buf

    return arr


print(rotator([0, 1, 2, 3, 4], 5))
