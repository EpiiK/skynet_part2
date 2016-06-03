import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

#function to generate and return public key
def pubkey_gen():
    
#function to generate and return private key
def privkey_gen():
    
    
#encrypt the msg which takes the public key and returns ciphertext
def encrypt_valuables(m):
    #hash the msg to fix length
    h = SHA256.new(m)
    #imports public key half encoded in standard form
    pubkey = RSA.importKey(open('pubkey.der').read())
    #using the public key to encrypt the hashed msg
    cipher = PKCS1_OAEP.new(pubkey)
    ciphertext = cipher.encrypt(h.digest())

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
