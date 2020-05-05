import math
def numberColmpliment(n:int)-> int:
    # print(bin(n).replace("0b" , ""))
    x = int(math.log2(n)) + 1
    print(x)
    for i in range(x):  
        n = (n ^ (1 << i))  
    print(n)  

    ## another way is using join
    # x = bin(n).replace("0b", "")
    # res = ''.join(['1'])

numberColmpliment(5)