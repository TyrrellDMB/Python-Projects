def encrypt(plain_text, s):
    encrypted_text = ''
    for i in range(len(plain_text)):
        if plain_text[i] == '': encrypted_text = encrypted_text + plain_text[i] 
        elif plain_text[i].isupper(): encrypted_text = encrypted_text + chr((ord(plain_text[i]) + s-65)%26+65)
        else: encrypted_text = encrypted_text + chr((ord(plain_text[i])+s-97)%26+97)
    
    return encrypted_text

def decrypt(encrypted_text, s):
    decrypted_text = ''
    for i in range(len(encrypted_text)):
        if  encrypt_text == '': decrypted_text = decrypted_text + encrypt_text[i]
        elif encrypt_text[i].isupper(): decrypted_text = decrypted_text + chr((ord(encrypt_text[i])-s-65)%26+65)
        else: decrypted_text = decrypted_text + chr((ord(encrypt_text[i])-s-97)%26+97)
    return decrypted_text

plain_text = input("Input the phrase you would like encrypted: ")
s = int (input("Enter shift: "))
encrypt_text = encrypt(plain_text, s)
print("Encrypted text: {}".format(encrypt_text))
print("Decrypted text: {}".format(decrypt(encrypt_text, s)))