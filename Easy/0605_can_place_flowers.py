"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

Constraints:
    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        size = len(flowerbed)

        if size == 1:
            if flowerbed[0] == 0:
                n -= 1
        elif size == 2:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                n -= 1
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1

            for i in range(1, size - 2):
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1

            if flowerbed[size - 2] == 0 and flowerbed[size - 1] == 0:
                flowerbed[size - 1] = 1
                n -= 1

        return n < 1

if __name__ == "__main__":
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    solution = Solution()
    result = solution.canPlaceFlowers(flowerbed, n)
    print(f"Can place {n} flowers: {result}")

    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    result = solution.canPlaceFlowers(flowerbed, n)
    print(f"Can place {n} flowers: {result}")