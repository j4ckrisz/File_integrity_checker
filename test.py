import hashlib

file_to_check = input("[+] Write the file path to check the integrity of the file: ")

md5 = hashlib.md5()

BUF_SIZE = 65536

with open(file_to_check, 'rb') as f :

    fb = f.read(BUF_SIZE)

    while True:

        md5.update(fb)
        
        fb = f.read(BUF_SIZE)

print( md5.hexdigest() )