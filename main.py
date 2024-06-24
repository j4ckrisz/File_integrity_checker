import hashlib
import os
from colorama import Fore, Back, Style

def compare_hash(md5_digest, hash_to_compare):

    if md5_digest != hash_to_compare:

        return "\n" + Fore.RED + "[-] File has been modified, the hashes are not the same :(, {} != {}".format(md5_digest, hash_to_compare) + Fore.RESET

    else:

        return "\n" + Fore.GREEN + "[+] You are good, hashes are the same :)"+Fore.RESET


def calculate_md5(file_path):

    if not os.path.isfile(file_path):

        raise FileNotFoundError(f"No such file: '{file_path}'")

    md5_hash = hashlib.md5()

    with open(file_path, "rb") as file:

        for chunk in iter(lambda: file.read(4096), b""):

            md5_hash.update(chunk)


    return md5_hash.hexdigest()


file_path = input("[>] Write the file full path: ")
hash_to_compare = input("[>] Write the hash to compare: ")

try:

    md5_digest = calculate_md5(file_path)
    comp_hashes = compare_hash(md5_digest, hash_to_compare)


    print(f"[+] MD5 Hash of the file '{file_path}' is: {md5_digest}")
    print(comp_hashes)


except FileNotFoundError as e:
    print(e)
