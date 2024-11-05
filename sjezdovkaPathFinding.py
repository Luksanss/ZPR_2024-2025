sjezdovka = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]


def findLongestPathJump(path):
    numOfPaths = 1
    pathNow = 0
    Max = 0
    tempMax = 0
    
    pathFindingIndexes = []
    
    for _ in range(len(path)):
        pathFindingIndexes.append(0)
    
    for i in path:
        numOfPaths *= len(i)
    
    while pathNow != numOfPaths:
        for index, i in enumerate(path):
            tempMax += i[pathFindingIndexes[index]]
        if tempMax > Max:
            Max = tempMax
        
        # reset tempMax and add one searched path
        tempMax = 0
        pathNow += 1
        
        # increase indexes
        
        startIncreaseOnIndex = len(pathFindingIndexes) - 1
        
        while True:
            try:
                path[startIncreaseOnIndex][pathFindingIndexes[startIncreaseOnIndex] + 1]
                pathFindingIndexes[startIncreaseOnIndex] += 1
                break
            except:
                pathFindingIndexes[startIncreaseOnIndex] = 0
                startIncreaseOnIndex -= 1
                if (startIncreaseOnIndex == -1):
                    return(Max)

def findLongestPath(path):
    revesedPath = path[::-1]
    pathTemp = []
    
    newFirstRow = []
    
    while len(pathTemp) != 1:
        pathTemp = []
        newFirstRow = []
        for i in range(len(revesedPath[0]) - 1):
            newFirstRow.append(max(revesedPath[0][i], revesedPath[0][i + 1]) + revesedPath[1][i])
        pathTemp.append(newFirstRow)
        for i in revesedPath[2:]:
            pathTemp.append(i)
        revesedPath = pathTemp
    return pathTemp[0][0]
    
print(findLongestPath(sjezdovka))