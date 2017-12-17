from Crypto.PublicKey import RSA
from Crypto import Random
random_generator = Random.new().read


def generate(size_in_bits =4096):
    key = RSA.generate(size_in_bits,random_generator)
    return key


key = generate()
print("Key can encrypt?\n%s\nKey Can Sign?\n%s\nKey has private?\n%s\n" % (key.can_encrypt(),key.can_sign(),key.has_private()))
message = 500
encrypted = key.publickey().encrypt(message,32)
decrypted = key.decrypt(encrypted)
print("Message is %d\n" % message)
print("Encrypted message is %d\n" % encrypted)
print("Decrypted message is %d\n" % decrypted)



