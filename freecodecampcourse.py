text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        
        if char == " ":
            #print("space!")
            encrypted_text += char
        else:
            #print()
            index = int(char) 
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
            
        print('char:', char, 'encrypted text:', encrypted_text)
    print("original text:", message)
    print('encrypted text:', encrypted_text)
caesar(text, shift)
# caesar(text, 10)
#print(bin(ord('B')))
# print("%.2f" % 1.7346128365138764)
