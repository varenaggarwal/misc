from typing import List
def singleNumber(nums: List[int]) -> int:
    # count array - O(n*distinct Ns + O(n))
    # dic ={}
    # for i in nums:
    #     if i in dic.keys():
    #         dic[i] += 1
    #     else:
    #         dic[i] = 1
    # print(dic)
    # for i in dic.keys():
    #     if (dic[i] == 1 ):
    #         return i
    # return 0
    ans  = 0
    #XOR can be done in O(n) XOR of same is 1 so in the end only single element is left
    for num in nums:
        ans ^= num
    return ans

print(singleNumber([2,2,4,1,1]))