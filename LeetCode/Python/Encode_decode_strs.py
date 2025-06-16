class Solution:

    def encode(self, strs: list[str]) -> str:
        pass


    def decode(self, s: str) -> list[str]:
        pass



def encode(strs):
    lengths = [len(i) for i in strs]
    newStrs =[f"{lengths[i]}#{strs[i]}" for i in range(len(strs))]

    return newStrs


def decode(self, s: str) -> list[str]:
    res = []
    i = 0

    while i < len(s):
        # Read the length (scan until '#')
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        j += 1  # Move past '#'
        res.append(s[j:j + length])
        i = j + length

    return res

encode(["neet","code","love","you"])
decode("4#neet4#code4#love3#you")