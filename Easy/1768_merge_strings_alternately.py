"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r

Example 2:
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    Explanation: Notice that as word2 is longer, "rs" is appended to the end.
    word1:  a   b 
    word2:    p   q   r   s
    merged: a p b q   r   s

Example 3:
    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    word1:  a   b   c   d
    word2:    p   q 
    merged: a p b q c   d

Constraints:
    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        sb = []
        len1 = len(word1)
        len2 = len(word2)
        minLen = min(len1, len2)

        for i in range(minLen):
            sb.append(word1[i])
            sb.append(word2[i])

        if minLen == len1:
            for i in range(minLen, len2):
                sb.append(word2[i])
        else:
            for i in range(minLen, len1):
                sb.append(word1[i])

        return ''.join(sb)

if __name__ == "__main__":
    word1 = "abc"
    word2 = "xyzdef"
    solution = Solution()
    result = solution.mergeAlternately(word1, word2)
    print(result) # axbyczdef