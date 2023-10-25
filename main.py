import string
import base64

# Inputs
plaintext = input("Enter your plaintext:")
cipher = input("Enter an encoding method:")
methods = ['Caesar' , 'ROT13' , 'Binary' , 'Base4' , 'Base8' , 'Base10' , 'Base12' , 'Base16' , 'Base32' , 'Base64']

# Caesar Cipher code
if cipher == "Caesar":
    
    def caesar(text, shift, alphabets):
        def shifted(alphabet):
            return alphabet[int(shift):] + alphabet[:int(shift)]

        shifted_alphabets = tuple(map(shifted, alphabets))
        final_alphabet = ''.join(alphabets)
        final_shifted = ''.join(shifted_alphabets)
        table = str.maketrans(final_alphabet, final_shifted)

        return text.translate(table)
    
    # ASCII stands for American Standard Code for Information Interchange
    print(caesar(plaintext, input("Enter a shift value:"),
                 [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))

# ROT13 code (Caesar cipher with a shift of 13)
if cipher == "ROT13":
    def caesar(text, shift, alphabets):
        def shifted(alphabet):
            return alphabet[int(shift):] + alphabet[:int(shift)]

        shifted_alphabets = tuple(map(shifted, alphabets))
        final_alphabet = ''.join(alphabets)
        final_shifted = ''.join(shifted_alphabets)
        table = str.maketrans(final_alphabet, final_shifted)

        return text.translate(table)
    
    print(caesar(plaintext, 13,
                [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))

# Base2 (binary)
if cipher == "Binary":
    binary = " ".join(format(ord(ch), "b") for ch in plaintext)
    # Each character has a space between because of the .join function, and it converts to binary with "b"
    print(binary)

# Base4 (Quarternary) and Base8 (Octal)
base = ("Base4" , "Base8")
if cipher in base:
    ascii_list = []
    for char in plaintext:
        base4_val = ""
        ascii_val = ord(char)
        ascii_list.append(ord(char))         
        while ascii_val > 0:
            remainder = ascii_val % int(cipher[4])
            base4_val = str(remainder)+base4_val
            ascii_val //= int(cipher[4])
            base4_val=base4_val.zfill(1)
            if ascii_val == 0: 
                print(base4_val,"", end="")

# Base10 (Decimal) 
if cipher == "Base10":
    for char in plaintext:
        print(ord(char) , end=" ")

# Base12 (Duodecimal/Dozenal)
if cipher == "Base12":
    ascii_list = []
    for char in plaintext:
        base12_val = ""
        ascii_val = ord(char)
        ascii_list.append(ord(char))
        while ascii_val > 0:
            remainder = ascii_val % 12
            if remainder == 10:
                    remainder = 'a' 
            if remainder == 11:
                remainder = 'b'
            base12_val = str(remainder)+base12_val
            ascii_val //= 12
            base12_val = base12_val.zfill(1)
            if ascii_val == 0:
                print(base12_val,"", end="")

# Base16
if cipher == "Base16":
    plaintext_bytes = plaintext.encode("ascii") 
    base16_bytes = base64.b16encode(plaintext_bytes) 
    base16_string = base16_bytes.decode("ascii") 
    print(base16_string)

# Base32
if cipher == "Base32":
    plaintext_bytes = plaintext.encode("ascii") 
    base32_bytes = base64.b32encode(plaintext_bytes) 
    base32_string = base32_bytes.decode("ascii") 
    print(base32_string)

# Base64
if cipher == "Base64":
    plaintext_bytes = plaintext.encode("ascii") 
    base64_bytes = base64.b64encode(plaintext_bytes) 
    base64_string = base64_bytes.decode("ascii") 
    print(base64_string)

# Else statement    
if cipher not in methods:
    print('That method is not supported. Supported encoding includes:') 
    print(*methods, sep=", ")        
                
    
   
                
    


