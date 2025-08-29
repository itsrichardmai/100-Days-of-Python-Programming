# # Method 1: Using list comprehension with chr() and ord()
# alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# print("Method 1 - Using chr() and ord():")
# print(alphabet)
# print(f"Index 0: {alphabet[0]}")
# print(f"Length: {len(alphabet)}")

# # Method 2: Using string.ascii_lowercase
# import string
# alphabet2 = list(string.ascii_lowercase)
# print("\nMethod 2 - Using string.ascii_lowercase:")
# print(alphabet2)

# Method 3: Manual list creation
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == 'encode':
        encrypt(original_text, shift_amount)
    elif encode_or_decode == 'decode': 
        decrypt(original_text, shift_amount)
    else:
        print("You did not choose 'encode' or 'decode'.")
    
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet: 
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    cipher_text2 = ""
    for letter in original_text:
        if letter not in alphabet: 
            cipher_text2 += letter
        else:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            cipher_text2 += alphabet[shifted_position]
    print(f"Here is the decoded message {cipher_text2}")


should_continue = True
while should_continue:

    print("Welcome to the Caesar Cypher!")
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower()
    text = input("Type your message: (NO SPACES)\n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no' \n")
    if restart == "no":
        should_continue = False
        print("Goodbye!")


# make a main function that includes both functions 
# encrypt(original_text=text, shift_amount=shift)
# decrypt(original_text=text, shift_amount=shift)