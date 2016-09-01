import os
<<<<<<< HEAD
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


def sign_file(f):
    # Generating a RSA key of length 2048 bits.
    pubkey = RSA.importKey(open('pubkey.der').read())
    # Generating the new hash to be added to the signature.
    h = SHA256.new(f)
    # Creating a new signature scheme which will be used to perform the signature verification.
    signer = PKCS1_v1_5.new(pubkey)
    # Signing the file using the signature scheme generated before.
    signature = signer.sign(h)
    return bytes(pubkey, "ascii") + f
=======
from Crypto.Signature import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def sign_file(f):
    # Generating a RSA key of length 2048 bits.
    new_key = RSA.generate(bits, e=65537)
    pubkey = new_key.publickey().exportKey("PEM")
    # Generating the new hash to be added to the signature.
    hash = SHA256.new(f)
    # Creating a new signature scheme which will be used to perform the signature verification.
    signer = PKCS1_OAEP.new(pubkey)
    # Signing the file using the signature scheme generated before.
    signature = signer.sign(h)
    return bytes(signature, "ascii") + f
>>>>>>> 9056611bf90d89db07755848d1523066728af783


if __name__ == "__main__":
    fn = input("Which file in pastebot.net should be signed? ")
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print("The given file doesn't exist on pastebot.net")
        os.exit(1)
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    signed_f = sign_file(f)
    signed_fn = os.path.join("pastebot.net", fn + ".signed")
    out = open(signed_fn, "wb")
    out.write(signed_f)
    out.close()
    print("Signed file written to", signed_fn)
