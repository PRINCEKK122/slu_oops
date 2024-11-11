
def readFile(fileInput):
    file = open(fileInput)
    
    vowelsCount = 0
    consonantsCount = 0
    specialChars = 0
    s = file.read()

    numberOfWords = len(s.split())
    numberOfLines = len(s.split("\n"))
    for letter in s:
            if letter.isalpha():
                if letter.lower() in "aeiou":
                    vowelsCount += 1
                else:
                    consonantsCount += 1
            else:
                specialChars += 1
    file.close()


    return (vowelsCount, consonantsCount, specialChars, numberOfLines, numberOfWords)

vowels, consonants, specialChars, numberOfLines, numberOfWords = readFile("labs/Lab 6 Test File.txt")

print(f"Vowels: {vowels:20}\nConsonants: {consonants:16}\nSpecial Characters: {specialChars:8}\n", end="") 
print(f"Number of Lines: {numberOfLines:11}\nNumber of words: {numberOfWords:11}")
