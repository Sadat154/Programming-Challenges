from itertools import permutations


def permute(nums):
    perms = [[]]
    for num in nums:
        new_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, num)
                new_perms.append(p_copy)
                print(new_perms)
        perms = new_perms
    return perms

print(permute([1,2,3]))