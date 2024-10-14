import re

def funkce_1(width):
    if (type(width) is not int or width < 3 or width >= 20 or width % 2 == 0):
        return 1
    
    print("$" + "-" * (width-2) + "$")
    
    curWidth = width
    whiteSpace = 0
    
    for i in range(width - 2):
        # descending
        if (i < int(width - 1) / 2):
            curWidth -= 2
            whiteSpace += 1
            print(" " * whiteSpace + "x" * curWidth)
        # descending
        else:
            curWidth += 2
            whiteSpace -= 1
            print(" " * whiteSpace + "x" * curWidth)

    print("$" + "-" * (width-2) + "$")
    return 0


def funkce_2(width, heigth):
    if (type(width) is not int or width % 2 == 0 or width < 3 or width >= 20):
        return 1
    if (heigth >= width):
        return 2
    
    whiteSpace = int((width - 1) / 2)
    
    print(" " * whiteSpace + "o")
    
    curWidth = 3
    curHeigth = 0
    
    while True:
        if (curWidth <= width):
            whiteSpace -= 1
            print(" " * whiteSpace + "@" * curWidth)
            curWidth += 2
        else:
            while curHeigth < heigth:
                print("@" + "x" * (width - 2) + "@")
                curHeigth += 1
            # done generating mid-section
            break
    
    
    while True:
        curWidth -= 2
        if (curWidth > 2):
            print(" " * whiteSpace + "@" * curWidth)
            whiteSpace += 1
        else:
            print(" " * whiteSpace + "o")
            break
        
    return 0

def funkce_3(width, heigth, char):
    
    if (type(width) is not int or width % 2 == 0 or width < 3 or width >= 20):
        return 1
    if (heigth >= width):
        return 2
    if (len(char) != 1 or re.search("[a-z]", char) is None):
        return 3
    
    roofTiles = 1
    
    for _ in range(int((width - 1) / 2) + 1):
        print((roofTiles * "^").center(width))
        roofTiles += 2
    for _ in range(heigth):
        print(f"|{char * (width - 2)}|")
        
    return 0

# funkce_1(19)
# funkce_2(9, 3) 
# funkce_3(9, 4, "a")