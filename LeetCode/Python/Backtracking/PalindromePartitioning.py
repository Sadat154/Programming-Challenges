def paritition(s):
    res = []

    substrings = []

    def backtrack(i):
        if i >= len(s):
            res.append(substrings.copy())
            return


        for j in range(i, len(s)):
            if self.isPali(s, i, j):
                substrings.append(s[i:j+1])
                backtrack(j+1)
                substrings.pop()
    backtrack(0)
