
def wordBreak(s, wordDict):
    memo = {}

    def dfs(i):
        if i == len(s):
            return True

        if i in memo:
            return memo[i]

        for word in wordDict:
            n = len(word)

            if s[i:i+n] == word:
                if dfs(i+n):
                    memo[i] = True
                    return True
        memo[i] = False
        return False


    return dfs(0)



s = "applepenapple"
wordDict = ["apple","pen","ape"]
print(wordBreak(s, wordDict))

s = "catsincars"
wordDict = ["cats","cat","sin","in","car"]

print(wordBreak(s, wordDict))