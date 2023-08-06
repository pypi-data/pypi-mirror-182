print("1")
"""
def encrypt(text,s):
    result=""

    for i in range(len(text)):
        char=text[i]

        if(char.isupper()):
            result+=chr((ord(char)+s-65)%26+65)

        else:
            result +=chr((ord(char)+s-97)%26+97)

    return result
def decrypt(text,s):
    result=""

    for i in range(len(text)):
        char=text[i]

        if(char.isupper()):
            result+=chr((ord(char)-s-65)%26+65)

        else:
            result+=chr((ord(char)-s-97)%26+97)

    return result

text ="INDIRA"
s=4
print("text:"+text)
print("shift:"+str(s))
print("cipher:"+encrypt(text,s))
str1=encrypt(text,s)
print("Decipher :"+decrypt(str1,s))
"""

