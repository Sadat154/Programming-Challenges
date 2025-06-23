def minEatingSpeed(piles, h):
    min = max(1, sum(piles) // h)
    maxi = max(piles)
    result = maxi

    while min <= maxi:

        k = ((min + maxi) // 2)

        hours_needed = sum(-(-pile // k) for pile in piles)

        if hours_needed <= h:
            result = k
            maxi = k-1
        else:
            min = k+1



    return result



piles = [1,4,3,2]

h = 9


print(minEatingSpeed(piles, h))

