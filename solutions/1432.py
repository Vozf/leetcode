class Solution:
    def change(self, num, old, to):
        return int(str(num).replace(str(old), str(to)))

    def maxDiff(self, num: int) -> int:
        num = str(num)
        idx_max, idx_min = 0, 0
        min_to = 1
        for i, char in enumerate(num):
            if char != "9":
                idx_max = i
                break

        for i, char in enumerate(num):
            if char != "1" and char != "0":
                idx_min = i
                if i == 0:
                    min_to = 1
                else:
                    min_to = 0
                break

        ma = self.change(num, num[idx_max], 9)
        mi = self.change(num, num[idx_min], min_to)
        return ma - mi
        
