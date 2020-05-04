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

print(canConstruct("fihjjjjei" , "hjibagacbhadfaefdjaeaebgi"))