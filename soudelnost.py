import math

def tabulka(k):
    if (type(k) is not int or k <= 0 or k > 100):
        print("ERROR")
        return -1
     
    tabulkaRes = []
     
     
    for i in range(k):
        i = i + 1 # start at 1
         
        genArr = [] # one row for tabulkaRes
 
        for n in range(k):
            n = n + 1 # start at 1
 
            if (n != 1 and i != 1):
                 
                if (math.gcd(n, i) > 1):
                    if (n == k):
                        genArr.append("x")
                    else:
                        genArr.append("x|")
                else:
                    if (n == k):
                        genArr.append(" ")
                    else:
                        genArr.append(" |") # res of comparison
            else:
                if (n == k):
                    genArr.append(" ")
                else:
                    genArr.append(" |") # res of comparison
             
            if (n == k): # add completed row
                tabulkaRes.append(genArr)
                tabulkaRes.append("-" * ((2 * k) - 1))
    for i in tabulkaRes[0:len(tabulkaRes)-1]:
        for n in i:
            print(n, end="")
        print()
 
 
 
tabulka(4)