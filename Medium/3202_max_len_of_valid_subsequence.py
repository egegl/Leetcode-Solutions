"""
You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.

Example 1:
Input: nums = [1,2,3,4,5], k = 2
Output: 5

Explanation:
The longest valid subsequence is [1, 2, 3, 4, 5].

Example 2:
Input: nums = [1,4,2,3,1,4], k = 3
Output: 4

Explanation:
The longest valid subsequence is [1, 4, 1, 4].

Constraints:
2 <= nums.length <= 103
1 <= nums[i] <= 107
1 <= k <= 103
"""


class Solution(object):
    def get_k_mod(self, first, second, k):
        return (first + second) % k

    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        first_second_mod_ks = {}
        mod_k_equals_and_contenders = {}

        for i in range(len(nums)- 1):
            first = nums[i]
            second = nums[i+1]

            k_mod_equals = self.get_k_mod(first, second, k)

            first_second_mod_ks[first] = k_mod_equals

            if(k_mod_equals in mod_k_equals_and_contenders.keys()):
                list = mod_k_equals_and_contenders[k_mod_equals]
                last_couple = list[len(list) - 1]
                if(self.get_k_mod(last_couple[1], first, k) == k_mod_equals):
                    mod_k_equals_and_contenders[k_mod_equals].append([first, second])
            else:
                mod_k_equals_and_contenders[k_mod_equals] = ([[first, second]])

            
            print(f"{first} + {second} % {k} =      {k_mod_equals}  ->   {mod_k_equals_and_contenders[k_mod_equals]}")
        
        print(mod_k_equals_and_contenders)

        # Get sub
        contenders = []

        mxa = max()

    




def main():
    nums = [1,4,2,3,1,4]
    k = 3

    print(Solution().maximumLength(nums, k))


if __name__ == "__main__":
    main()