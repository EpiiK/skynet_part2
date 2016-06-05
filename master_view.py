import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA

def decrypt_valuables(f):
    #Get the privte key
    new_key = RSA.generate(bits, e=65537)
    private_key = new_key.exportKey("PEM")
    #Make cipher with the private key
    cipher = PKCS1_OAEP.new(private_key)
    #Decrypt the file to plaintext
    message = cipher.decrypt(f)
    #print the message
    print(message)
    

if __name__ == "__main__":
    fn = input("Which file in pastebot.net does the botnet master want to view? ")
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print("The given file doesn't exist on pastebot.net")
        os.exit(1)
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    decrypt_valuables(f)
