# misto prvni radku se da prvni sloupec
# transpozice matice


matice = [[1,1,1],
          [2,2,2],
          [3,3,3],
          [4,4,4]]

def transpozice(matice):
    transponovana = []
    pocetRadku = len(matice)
    pocetSloupcu = len(matice[0])
    sloupceCounter = 0
    
    genSloupec = []
    while sloupceCounter != pocetSloupcu:
        for cisloRadku, radek in enumerate(matice):
            genSloupec.append(matice[cisloRadku][sloupceCounter])
        transponovana.append(genSloupec)
        genSloupec = []
        sloupceCounter += 1
    
            
    return transponovana


print(transpozice(matice))