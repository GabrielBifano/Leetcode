# Kids With the Greatest Number of Candies
# Easy

def kidsWithCandies(candies: 'list[int]', extraCandies: int) -> 'list[bool]':
    greatest_among_all = 0
    for realDeal in candies:
        if realDeal > greatest_among_all:
            greatest_among_all = realDeal
    trueseses_and_falseseses = []
    for sadKid in candies:
        if sadKid + extraCandies >= greatest_among_all:
            trueseses_and_falseseses.append(True)
        else:
            trueseses_and_falseseses.append(False)
    return trueseses_and_falseseses