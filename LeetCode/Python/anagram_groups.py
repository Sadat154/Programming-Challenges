class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        orderedStrings = [''.join(sorted(string)) for string in strs]
        occurance = {}
        count = 0
        for string in orderedStrings:
            if string in occurance:
                occurance[string].append(strs[count])
            else:
                occurance[string] = [strs[count]]
            count += 1
        # finalAns = []
        # for values in occurance.items():
        #     x = []
        #     for item in values[1]:
        #         x.append(strs[item])
        #     finalAns.append(x)

        return list(occurance.values())
