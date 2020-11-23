class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        if len(S) == 0:
            return S

        nest = []
        opt_substrings = []
        for i in range(len(S)):
            char = S[i]
            if char == "1":
                nest.append(i)
            else:
                opened = nest.pop()

                if len(nest) == 0:
                    print("sending", S[opened+1:i], S[:i])
                    opt_substrings.append("1" +self.makeLargestSpecial(S[opened+1:i]) + "0")



        sort = list(reversed(sorted(opt_substrings)))
        print(sort)
        new_s = "".join(sort)

        return new_s

