alpha = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

de_key = [
    "£", "*", "%", "&", ">", "<", "!", ")", "\"", "(", "@", "a",
    "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"
]


de_dict = dict(zip(alpha, de_key))


def unencrypted_file(file_name):
    with open(file_name, "r") as unenc_file:
        unenc = unenc_file.read().lower()
    return unenc

def enced_data(enc_file):
    with open("enc_file.txt", "w") as enc:
        enc.write(enc_data)
    return enc   

def enced_data(enc_file):
    with open("enc_file.txt", "r") as enced:
        enced.read()
    return enced


def encrypt(unencrypted_item):
    result = ""
    for i in unencrypted_item:
        if i not in de_dict:
            result+=i
        else:    
            result+=de_dict[i]
    return result




username = input("Write your name: ")
print("\n")



while True:
    choice = input("press 1 to encrypt or 2 to decrypt: ")
    print("\n")
    if choice == "1":
        print("Note: To encrypt a file the file must be in the same folder as the python file.\nAnd must bear the name 'story.txt' (note the case of the file name)\n")
        enc_path = input(username + ", there are two options, If you want to encrypt a file, enter 1 or\nFor a message inputed by you to be encrypted, enter 2: ")
        print("\n")
        
        if enc_path == "1":
            unenc_data = unencrypted_file("story.txt")
            enc_data = encrypt(unenc_data)
            enced_data(enc_data)
            print("\n\n")
            break
        elif enc_path == "2":
            unenc_text = input(username + ", write a text to be encrypted: ").lower()
            enc_data = encrypt(unenc_text)
            print("\n\n")
            print(enc_data)
            break
    
    if choice == "2":
        print("Note: To decrypt a file the file must be in the same folder as the python file.\nAnd must bear the name 'enc_file.txt' (note the case of the file name)\n")
        dec_path = input("if you want to decrypt a saved file, enter 1 while for an encrypted text inputed by you, enter 2: ")
        print("\n")
        
            
            



