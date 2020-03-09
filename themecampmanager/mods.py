# my_lambdata/mods.py
import string
import secrets


def return_hash():
    hash_id = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(18))
    output_hash(hash_id)

def output_hash(hash_id):
    print(hash_id)