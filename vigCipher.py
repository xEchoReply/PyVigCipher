import string

def VigCipher(inputString, inputKey, encryptDecrypt="e"):
    #Check if third argument is "e" or "d"
    #If neither, default to encrypt
    encryptDecrypt=encryptDecrypt.lower()
    if encryptDecrypt!="e" and encryptDecrypt!="d":
        print("Invalid argument, defaulting to encrypt.")
        encryptDecrypt="e"

    #Make inputString lowercase alpha characters only, store in alphaString
    alphaString=""
    for i in inputString:
        if i.isalpha():
            alphaString+=i.lower()

    #Make inputKey lowercase alpha characters only, store in alphaKey
    alphaKey=""
    for i in inputKey:
        if i.isalpha():
            alphaKey+=i.lower()

    #Generate long key, repeating alphaKey to length of alphaString
    longKey=""
    c=0
    while len(longKey)!=len(alphaString):
        if c>len(alphaKey)-1:
            c=0
        longKey+=alphaKey[c]
        c+=1

    #Encrypt or decrypt alphaString with longKey
    abcRange=string.ascii_lowercase
    encryptedString=""
    for i in range(len(alphaString)):
        stringIndex=abcRange.index(alphaString[i])
        keyIndex=abcRange.index(longKey[i])
        if encryptDecrypt=="e":
            total=stringIndex+keyIndex
            if total>25:
                total-=26
        if encryptDecrypt=="d":
            total=stringIndex-keyIndex
            if total<0:
                total+=26
        encryptedString+=abcRange[total]

    #Format alphaString to match case, whitespace, and punctuation of original inputString
    c=0
    finalString=""
    for i in inputString:
        if i.isalpha():
            if i.isupper():
                finalString+=encryptedString[c].upper()
            if i.islower():
                finalString+=encryptedString[c].lower()
            c+=1
        else:
            finalString+=i
    return finalString

if __name__=="__main__":
    my_message=input("Please enter a message: ")
    my_key=input("Please enter a word as a key: ")
    encryptOrDecrypt=input("Do you want to (e)ncrypt or (d)ecrypt?: ")
    print("Message: "+VigCipher(my_message,my_key,encryptOrDecrypt)+"\n")
