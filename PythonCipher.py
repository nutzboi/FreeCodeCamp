custom_key = "anything"

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        
        # Append any non-letter character to the message.        
        if not char.isalpha(): # if char == " ":
            final_message += char
        else:
            # Find the right character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            
            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char) 
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
            
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    #pass
    
def decrypt(message, key):
    return vigenere(message, key, -1)

message = str(input("Enter message: "))
custom_key = str(input("Enter key: "))
operation = str(input("Decrypt (1) or Encrypt (2)?"))
if(operation.lower() == 'decrypt' or operation == '1'):
    print(decrypt(message, custom_key))
else:
    print(encrypt(message, custom_key))
