def tabulka(num):
    if (num <= 0 or num > 99):
        print("ERROR")
        return -1 
    
    tabulkaRes = []
    
    
    for i in range(num):
        i = i + 1 # start at 1
        
        genArr = [] # one row for tabulkaRes

        for n in range(num):
            n = n + 1 # start at 1

            if (n != 1 and i != 1):
                
                if (n % i == 0):
                    if (n == num):
                        genArr.append("x")
                    else:
                        genArr.append("x|")
                else:
                    if (n == num):
                        genArr.append(" ")
                    else:
                        genArr.append(" |") # res of comparison
            else:
                if (n == num):
                    genArr.append(" ")
                else:
                    genArr.append(" |") # res of comparison
            
            if (n == num): # add completed row
                tabulkaRes.append(genArr)
                tabulkaRes.append("-" * (num + 3))
    for i in tabulkaRes:
        for n in i:
            print(n, end="")
        print()



tabulka(4)
