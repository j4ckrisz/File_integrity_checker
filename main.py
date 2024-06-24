import hashlib
import os

def calculate_md5(file_path):

    if not os.path.isfile(file_path):

        raise FileNotFoundError(f"No such file: '{file_path}'")


    md5_hash = hashlib.md5()


    with open(file_path, "rb") as file:

        for chunk in iter(lambda: file.read(4096), b""):

            md5_hash.update(chunk)
    

    return md5_hash.hexdigest()


file_path = ""  
try:

    md5_digest = calculate_md5(file_path)
    
    print(f"MD5 Hash of the file '{file_path}' is: {md5_digest}")

except FileNotFoundError as e:
    print(e)
