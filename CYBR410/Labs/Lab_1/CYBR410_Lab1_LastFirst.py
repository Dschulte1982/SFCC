# CYBR 410 Lab 1 Fall 2024
# Modified by Dustin Schulte on 09/26/2024
#
# Adapted from Ashutosh Kumar
# This program illustrates a Caesar Cipher Technique

# defining the cipher function
def cipher(mode,text,shift):
    result = ""

    # loop to traverse text
    for i in range(len(text)):
        char = text[i]

        # Add whitespace if the text includes it
        if char.isspace():
            result += " "

        # Encrypt uppercase characters
        if (char.isupper() and mode == "encrypt"):
            # ASCII 0-31 contains control characters used in text control
            # ASCII 32-64 contains punctuation symbols, spaces, and digits 0-9
            # ASCII 65-91 contains uppercase letters ABCD etc. in order
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Decrypt uppercase characters
        elif (char.isupper() and mode == "decrypt"):
            result += chr((ord(char) - shift - 65) % 26 + 65)


        # Encrypt lowercase characters
        if (char.islower() and mode == "encrypt"):
            result += chr((ord(char) + shift - 97) % 26 + 97)
            # ASCII 92-96 contains non-alphabetic symbols such as [,\,],^,_,`
            # ASCII 97-122 contains lowercase letters abcd etc. in order
        # Decrypt lowercase characters
        elif (char.islower() and mode == "decrypt"):
            result += chr((ord(char) - shift - 97) % 26 + 97)

    return result

# Prompt the user for the mode (encrypt or decrypt)
mode = input("Do you want to encrypt or decrypt the text? (Enter 'encrypt' or 'decrypt'): ")
# Prompt the user for the text to encrypt or decrypt
text = input("Enter the text: ")
# Prompt the user for the shift value
shift = int(input("Enter the shift value (integer): "))

# Print output of the user prompts to display the original text, shift value, and end result
print ("Original Text : " + text)
print ("Shift : " + str(shift))
print ("Result (%sED TEXT) : " % mode.upper() + cipher(mode,text,shift))
