def presypaciHodiny(n):
    if (n <= 3 or n > 20 or n % 2 == 0):
        return 1
    
    print("$" + "-" * (n-2) + "$")
    
    curNum = n - 2
    whiteSpace = 1
    reachedEnd = False
    
    while True:
        print(whiteSpace * " " + curNum * "-")
        if (curNum == 1 or reachedEnd):
            reachedEnd = True
            curNum += 2
            whiteSpace -= 1
            if (curNum >= n - 2):
                print(whiteSpace * " " + curNum * "-")
                print("$" + "-" * (n-2) + "$")
                return 0
        else:
            whiteSpace += 1
            if (curNum > 2):
                curNum -= 2
            else:
                curNum -= 1
    
presypaciHodiny(19)