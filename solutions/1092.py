import numpy as np
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        tile1 = np.tile(list(str1), (len(str2), 1))
        tile2 = np.tile(list(str2), (len(str1), 1)).T
        eq = tile1 == tile2
        #print(eq)

        h, w = eq.shape
        trace = [[[] for j in range(w+1)] for i in range(h+1)]
        dp = np.zeros((h+1, w+1), dtype=np.int)
        for i in reversed(range(h)):
            for j in reversed(range(w)):
                right = dp[i, j+1]
                bot = dp[i+1, j]
                if eq[i, j]:
                    inc = dp[i+1, j+1] + 1
                    m = max(right, bot, inc)
                    #print(m, inc, i, j)
                    if m == inc:
                        #print('aha', dp[i,j])
                        dp[i, j] = inc
                        #print(dp[i,j], inc)
                        trace[i][j] = trace[i+1][j+1] + [(i, j)]
                        continue

                m = max(right, bot)
                if m == right:
                    dp[i, j] = right
                    trace[i][j] = trace[i][j+1]
                else:
                    dp[i, j] = bot
                    trace[i][j] = trace[i+1][j]
        #print(dp)
        longest = max([subel for el in trace for subel in el], key=len)
        #print(longest)

        best_str = []
        prev_i, prev_j = 0, 0
        for i,j in reversed(longest):
            best_str.append(str2[prev_i:i])
            best_str.append(str1[prev_j:j])
            best_str.append(str2[i])
            prev_i, prev_j = i+1, j+1
            #print(i, j, best_str)

        best_str.append(str2[prev_i:])
        best_str.append(str1[prev_j:])


        return "".join(best_str)


