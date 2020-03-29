# my_lambdata/mods.py
import string
import secrets


def return_hash():
    '''
    Generates a random string of alphanumeric characters of length 18
    '''
    hash_id = ''.join(secrets.choice(
        string.ascii_letters + string.digits) for i in range(18))
    output_hash(hash_id)


def output_hash(hash_id):
    '''
    Outputs the generated hash into whatever pipe is needed
    '''
    print(hash_id)



