# precission = 10000000
# 
# estimapedPI = 4
# 
# for (index, i) in enumerate(range(3, precission, 2)):
#     if (index % 2 == 0):
#         estimapedPI -= 4/i
#     else:
#         estimapedPI += 4/i




# solution without enumerate

# indexer = 0
# 
# for i in range(3, precission, 2):
#     if (indexer % 2 == 0):
#         estimapedPI -= 4/i
#     else:
#         estimapedPI += 4/i
#     indexer += 1
        
    
# print(estimapedPI)

def myFunc(a):
    if (a == 9):
        return 0
    return 1

returnVal = myFunc(7)
print(returnVal)
