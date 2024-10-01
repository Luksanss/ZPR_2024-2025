samohlasky = ["a", "e", "i", "o", "u", "y"]


word = "milan je smradlavej bezdomovec a mel by prestat pichat heroin"



def pocetSamohlasek(veta):
    numOfSamohlasky = 0
    for i in veta:
        if (i in samohlasky):
            numOfSamohlasky += 1
    return numOfSamohlasky
        
print(pocetSamohlasek(word))