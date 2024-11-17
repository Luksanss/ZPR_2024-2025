import re

def dekoduj(sifrovany, odposlechnuty):
    pattern = r"[a-zA-Z]+"
    
    # check if there are only allowed letters AND ff encoded and overheared text have the same length
    if (len(sifrovany) != len(odposlechnuty) and not bool(re.fullmatch(pattern, sifrovany)) or not bool(re.fullmatch(pattern, sifrovany))):
        print("Error: Chybny vstup!")
        return None
    
    # check if there are only allowed letters (encoded and overheared text)
    if (not bool(re.fullmatch(pattern, sifrovany)) or not bool(re.fullmatch(pattern, sifrovany))):
        print("Error: Chybny vstup!")
        return None
    # check if encoded and overheared text have the same length
    if (len(sifrovany) != len(odposlechnuty)):
        print("Error: Chybna delka vstupu!")
        return None
    
    # alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    
    shiftTracker = {}
    
    for i, encodedLetter in enumerate(sifrovany):
        # find distance between encoded and overheared letter
        shiftFound = abs(alphabet.index(odposlechnuty[i]) - alphabet.index(encodedLetter))
        # if this shift doesnt exist add
        if (shiftFound not in shiftTracker):
            shiftTracker[shiftFound] = 1
        else:
            shiftTracker[shiftFound] += 1
    
    # find the most common shift
    shift = max(shiftTracker, key=shiftTracker.get)
    
    decodedWord = ""
    
    # decode the message
    for i, encodedLetter in enumerate(sifrovany):
        # modulo in case of overflow (- return to the beginning of the alphabet)
        decodedLetter = alphabet[(alphabet.index(encodedLetter) + shift) % len(alphabet)]
        decodedWord += decodedLetter
    
    return decodedWord