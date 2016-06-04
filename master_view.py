import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

def decrypt_valuables(f):
    #import private key half
    privkey = RSA.importKey(open('privkey.der').read())
    #use same scheme but with private key
    cipher = PKCS1_OAEP.new(privkey)
    #f is the ciphertext
    msg = cipher.decrypt(f)


if __name__ == "__main__":
    fn = input("Which file in pastebot.net does the botnet master want to view? ")
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print("The given file doesn't exist on pastebot.net")
        os.exit(1)
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    decrypt_valuables(f)
