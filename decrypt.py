"""
File: decrypt.py
Decypts an input string of lowercase letters and prints
the result.  The other input is the distance value.
"""
import string

code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ''
characters = string.printable
length = len(characters)
for ch in code:
    ordValue = characters.index(ch)
    cipherValue = (ordValue - distance) % length
    plainText +=  characters[cipherValue]
print(plainText)
