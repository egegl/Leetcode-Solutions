"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000


class Solution(object):
    def romanToInt(self, s):
        sum = 0
        i_count = 0
        x_count = 0
        c_count = 0

        while(len(s) > 0):
            currChar = s[0]

            if(currChar == 'I'):
                i_count += 1
            elif(currChar == 'V'):
                if(i_count == 1):
                    sum += (V - I)
                    i_count -= 1
                else:
                    sum += V
            elif(currChar == 'X'):
                if(i_count == 1):
                    sum += (X - I)
                    i_count -= 1
                else:
                    x_count += 1
            elif(currChar == 'L'):
                if(x_count == 1):
                    sum += (L - X)
                    x_count -= 1
                else:
                    sum += L
            elif(currChar == 'C'):
                if(x_count == 1):
                    sum += (C - X)
                    x_count -= 1
                else:
                    c_count += 1
            elif(currChar == 'D'):
                if(c_count == 1):
                    sum += (D - C)
                    c_count -= 1
                else:
                    sum += D
            elif(currChar == 'M'):
                if(c_count == 1):
                    sum += (M - C)
                    c_count -= 1
                else:
                    sum += M
            
            s = s[1:]

        sum += (I * i_count)
        sum += (X * x_count)
        sum += (C * c_count)

        return sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("D"))