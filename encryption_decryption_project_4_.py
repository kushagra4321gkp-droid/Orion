continue1 = True
while continue1:
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    your_choice = input("Type 'encrypt' for Encryption of Type 'decrypt' for Decryption :\n")
    your_text = input("Type your text :\n")
    shift_key = int(input("Type your shift key :\n"))
    if your_choice == 'encrypt':
        def encryption(your_text, shift_key):
            # if shift_key < 0:
            #     shift_key += 26
            ciphertext = ''
            for x in your_text:
                if x in alphabet_list:
                    index = alphabet_list.index(x)
                    e = (index + shift_key) % 26
                    ciphertext += alphabet_list[e]
                else:
                    ciphertext += x
            print(ciphertext)
            #return ciphertext
        encrypt = encryption(your_text, shift_key)
    elif your_choice == 'decrypt':
        def decryption(your_text, shift_key):
            # if shift_key < 0:
            #     shift_key += 26
            plain_text = ''
            for x in your_text:
                if x in alphabet_list:
                    index = alphabet_list.index(x)
                    zz = index - shift_key
                    if zz < 0:
                        zz += 26
                    e = zz % 26
                    plain_text += alphabet_list[e]
                else:
                    plain_text += x
            print(plain_text)
            #return plain_text
        decrypt = decryption(your_text, shift_key)
    continue1 = input("Type 'yes' or 'no' to continue :\n")
    if continue1 == 'no':
        break

#This view is read-only
# if decrypt shift_key= shift_key * -1


