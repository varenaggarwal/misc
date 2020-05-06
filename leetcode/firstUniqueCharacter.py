def firstUniqChar(s: str) -> int:
    index =-1
    for i in s:
        index+=1
        if s.count(i)==1:
            return index
    return -1
    #another way 
    from collections import Counter
    s1=Counter(s)
    print(s1)
    for i in s1:
        if s1[i]==1:
            return s.index(i)
    return -1

print(firstUniqChar("eetcode"))