from collections import Counter
from typing import List

def majorityElement(self, nums: List[int]) -> int:
    c = Counter(nums)
    print (c)
    return c.most_common(1)[0][0]
    #another way sort then the element at half way. it is sure majority element exists
    nums.sort()
    length = len(nums) // 2
    return nums[length]
