# class TwoSum:
#     def __init__(self):
#         self.li = list()
#         self.searchEnd = 0
#         self.found = False
#
#     def add(self, i):
#         if self.find(i) is not None:
#             return
#         else:
#             self.li.insert(self.searchEnd, i)
#
#     def find(self, v):
#         result = self.bsearch(0, len(self.li), v)
#         if self.found:
#             return result
#         else:
#             return None
#
#     def bsearch(self, s, e, target):
#         if s == e:
#             self.searchEnd = s
#             self.found = False
#             return None
#         mid = int((e + s) / 2)
#
#         if self.li[mid] != target:
#             if self.li[mid] > target:
#                 self.found = True
#                 return self.bsearch(s, mid, target)
#             else:
#                 self.found = True
#                 return self.bsearch(mid + 1, e, target)
#         else:
#             return mid


class TwoSum:
    def __init__(self):
        self.li = list()
        self.lookUp = {}

    def add(self, i):
        self.li.append(i)
        if len(self.li) > 1:
            self.updateTB(i)

    def find(self, target):
        return self.lookUp.get(target)

    def updateTB(self, i):
        iIndex = len(self.li) - 1
        for index, origin in enumerate(self.li[:-1]):  # don't calc the last element
            v = origin + i
            if self.lookUp.get(v) is None:
                self.lookUp[v] = [(index, iIndex)]
            else:
                self.lookUp.get(v).append((index, iIndex))


test = TwoSum()
test.add(12)
test.add(12)
print(test.find(24))
