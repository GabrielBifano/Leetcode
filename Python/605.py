# Can Place Flowers
# Easy

def canPlaceFlowers(flowerbed: 'list[int]', n: int) -> bool:

        def g (l, idx, default):
            if idx < 0: 
                return default
            try:
                return l[idx]
            except IndexError:
                return default

        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0 and g(flowerbed, i - 1, 0) == 0 and g(flowerbed, i + 1, 0) == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
