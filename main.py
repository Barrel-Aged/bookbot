def main():

    bookPath = "books/frankenstein.txt"
    text = getBookPath(bookPath)
    wordCount = getWordCount(text)
    charCount = getCharacterCount(text)
    reportHeader = f"--- Begin report of {bookPath} ---"
    reportFooter = "-- End report --"
    alphasList = reportCharData(charCount)
    buildReport(reportHeader, reportFooter, alphasList, wordCount)

def getBookPath(path):
    with open(path) as f:
        return f.read()

def getWordCount(text):
    words = text.split()
    return len(words)
        
def getCharacterCount(text):
    charCount = {}
    lowerWords = [x.lower() for x in text]
    for word in lowerWords:
        characters = list(word)
        for char in characters:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
    return charCount

def reportCharData(charCount):
    alphaCount = {}
    for char in charCount:
        if char.isalpha():
            alphaCount[char] = charCount[char]
    sortedAlphas = dict(sorted(alphaCount.items(), key=lambda item: int(item[1]), reverse=True))
    alphasList = []
    for alpha in sortedAlphas:
        alphasList.append(f"The '{alpha}' character was found {sortedAlphas[alpha]} times")
    return alphasList

def buildReport(reportHeader, reportFooter, alphasList, wordCount):
    print(reportHeader)
    print(f"{wordCount} words found in the document")
    print(" ")
    for alpha in alphasList:
        print(alpha)
    print(reportFooter)

main()