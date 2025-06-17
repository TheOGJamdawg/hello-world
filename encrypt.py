"""
File: encrypt.py
Encypts an input string of lowercase letters and prints
the result.  The other input is the distance value.
"""
import string

plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""
characters = string.printable
length = len(characters)
for ch in plainText:
    ordValue = characters.index(ch)
    cipherValue = (ordValue + distance) % length
    code +=  characters[cipherValue]
print(code)
