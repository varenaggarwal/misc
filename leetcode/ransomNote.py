def canConstruct(ransomNote: str, magazine: str) -> bool:
    if ransomNote in magazine:
        return True
    ransomdic ={}
    for s in ransomNote:
        if s in ransomdic.keys():
            ransomdic[s]+=1
        else:
            ransomdic[s] = 1
    magazinedic ={}
    for s in magazine:
        if s in magazinedic.keys():
            magazinedic[s]+=1
        else:
            magazinedic[s] = 1
    ans =False
    for i in ransomdic.keys():
        if i in magazinedic.keys():
            if (ransomdic[i]<= magazinedic[i]):
                ans = True 
            else:
                return False
        else:
            return False
    return ans
    # another - Counter from collections
    from collections import Counter
    c1 = Counter(s1)
    c2 = Counter(s2)
    ans = False
    for i in c1.keys():
        if i in c2.keys():
            if c1[i]<= c2[i]:
                ans = True
            else:
                return False
        else: return False
    return ans
    ## another way to do it is 
    for i in set(ransomNote):
        if ransomNote.count(i) > magazine.count(i):
            return False
        return True

print(canConstruct("fihjjjjei" , "hjibagacbhadfaefdjaeaebgi"))