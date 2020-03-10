# my_lambdata/mods.py
import string
import secrets


def return_hash():
    '''
    Generates a random string of alphanumeric characters of length 18
    '''
    hash_id = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(18))
    output_hash(hash_id)

def output_hash(hash_id):
    '''
    Outputs the generated hash into whatever pipe is needed
    '''
    print(hash_id)

def retrieve_hashes():
    '''
    Currently this is a static list but this will be a pipeline to retrieve
    hashes from the db of members to check for matches
    '''
    hashes = ['0xhO48RWRBv7CBaCt3','E4KaCetWk6yP6jy9E6','6o0IX5x3ToyI6Pqh5f']

def check_hash(hash_id):
    '''
    Makes a comparison between the new generated hash and the previously
    recorded hashes to ensure duplicates are not generated
    '''
    pass

