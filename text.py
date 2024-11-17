def historogram(text, scale = 0, case_sensitive = False):
    if (not case_sensitive):
        text = text.lower()
    
    # cleanup the string of whitespace and commas
    to_clean = [",", ".", " ", ";", "-"]
    
    cleanText = ""
    
    for i in text:
        if (i not in to_clean):
            cleanText += i
    
    text = cleanText
    # sort letters
    text = sorted(text)
    
    # find freq of letters
    historogramDict = {}
    
    for i in text:
        if i not in historogramDict:
            historogramDict[i] = 1
        else:
            historogramDict[i] += 1
    
    # convert to arr with touples (required output format), 
    # also get letter with max freq (used later in code)
    historogramArr = []
    max_freq = 0
    
    for i in historogramDict:
        historogramArr.append(tuple((i, historogramDict[i])))
        
        if (historogramDict[i] > max_freq):
            max_freq = historogramDict[i]
        
    # draw the historogram
    onCurScale = scale
    for i in historogramDict:
        print(f"{i}: ", end="")
        if (scale != 0):
            onCurScale = int((historogramDict[i]/max_freq)*scale)
            for _ in range(onCurScale):
                print("*", end="")
        else:
            for _ in range(historogramDict[i]):
                print("*", end="")
        print()
    
    return historogramArr


def serad(text, metoda, case_sensitive = False):
    # text cleanup
    to_clean = [",", ".", ";", "-"]
    cleanText = ""
    for i in text:
        if (i not in to_clean):
            cleanText += i
    
    # split to an array
    text = cleanText.split(" ")
    
    # keep only words of len 3 or above and lower if not case sentivie
    longWords = []
    
    for word in text:
        if (len(word) >= 3):
            if (not case_sensitive):
                word = word.lower()
            longWords.append(word)
            
    text = longWords
    
    # sort by length of words
    if (metoda == 0):
        sortedWords = []
        wordLen = {}
        
        for word in text:
            wordLen[word] = len(word)
            
        wordLen = sorted(wordLen, reverse=True)
        
        for word in wordLen:
            sortedWords.append(word)
        return sortedWords
    # pocet souhlasek
    if (metoda == 1):
        souhlasky = ["a", "e", "i", "o", "u"]
        souhlaskyCount = {}
        
        for word in text:
            souhlaskyCount[word] = 0
            for letter in word:
                if (letter in souhlasky):
                    souhlaskyCount[word] += 1
                    
        souhlaskyCount = sorted(souhlaskyCount, reverse=True)
        # sort alphabetically if words have the same length
        
        souhlaskyCount = sorted(souhlaskyCount, reverse=True, key=lambda word: (len(word), word))
        
        #s = sorted(words, key=lambda word: (len(word), word))
        
        return souhlaskyCount
    # cetnost nejcastejsiho pismenka
    if (metoda == 2):
        countOfLetters = {}
        
        for word in text:
            for letter in word:
                if (letter not in countOfLetters):
                    countOfLetters[letter] = 1
                else:
                    countOfLetters[letter] += 1
        
        mostFreqLetter = ""
        mostFreqNum = 0
        
        for letter in countOfLetters:
            if (countOfLetters[letter] > mostFreqNum):
                mostFreqNum = countOfLetters[letter]
                mostFreqLetter = letter
                
        # count number of most freq letter in each word
        countOfMostFreqLetterInWords = {}
        
        for word in text:
            countOfMostFreqLetterInWords[word] = word.count(mostFreqLetter)
            
        text = dict(sorted(countOfMostFreqLetterInWords.items(), reverse=True))
        textArr = []
        for i in text:
            textArr.append(i)
        
        textArr = sorted(textArr, reverse=True, key=lambda word: (len(word), word))
        print(text)
        
        return textArr

# ret = historogram('Aaaach, to je kraaasa', 4)
ret = serad('Aaaach, to je kraaasa', 0, True)
print(ret)
ret = serad('Aaaach, to je kraaasa', 1, False)
print(ret)
ret = serad('Aaaach, to je kraaasa', 2, True)
print(ret)
ret = serad('Aaaach, to je kraaasa', 2, False)
print(ret)

