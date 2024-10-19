class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}

        for charS in s:
            table[charS] = table.get(charS, 0) + 1
        for charT in t:
            table[charT] = table.get(charT, 0) - 1

        for key, values in table.items():
            if values != 0:
                return False
        return True


