import string

# Inputs
plaintext = input("Enter your plaintext:")
cipher = input("Enter an encoding method:")
methods = ['Caesar', 'Binary', 'Base 4', 'Base 8', 'Base 10']

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

# Base 2 (binary)
if cipher == 'Binary':
    binary = " ".join(format(ord(ch), "b") for ch in plaintext)
    # Each character has a space between because of the .join function, and it converts to binary with "b"
    print(binary)

# Base 4 and Base 8
base = ('Base 4' , 'Base 8')
if cipher in base:
    ascii_list = []
    for char in plaintext:
        base4_val = ""
        ascii_val = ord(char)
        ascii_list.append(ord(char))         
        while ascii_val > 0:
            remainder = ascii_val % int(cipher[5])
            base4_val = str(remainder)+base4_val
            ascii_val //= int(cipher[5])
            base4_val=base4_val.zfill(1)
            if ascii_val == 0: 
                print(base4_val,"", end="")

# Base 10 
if cipher == "Base 10":
    for char in plaintext:
        print(ord(char) , end=" ")

# Else statement    
else:
    print('That method is not supported. Supported encoding includes:') 
    print(*methods, sep=", ")         
                
    


        
