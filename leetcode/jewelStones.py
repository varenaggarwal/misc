'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''


def numJewelsInStones(J : str , S:str ) -> int:
    numJ = len(J)
    nums = len(S)
    ans = 0
    # brute force - travese over s and match if it is a jevel or not - O(len(s))
    # can be count array 
    for letter in S:
        if (letter in J):
            ans += 1
    return ans
    # create a count array  - better O(n)
    dic ={}
    count =0
    for letter in S:
        if letter in dic.keys():
            dic[letter] += 1
        else:
            dic[letter] =1
    for letter in J:
        if letter in dic.keys():
            count += dic[letter]
    return count


J ="aA"
s ="aAAbbbb"
print(numJewelsInStones(J , s))