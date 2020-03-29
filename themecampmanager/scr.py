from themecampmanager.mods import return_hash
import pandas as pd


class User:
    '''
    Base camp membership class
    
    '''
    def __init__(self, fname, lname, email, id_hash, alpha_hash):
        self.fname = fname #first name
        self.lname = lname #last name
        self.email = email #checked against profile
        self.id_hash = id_hash #unique identifier
        self.alpha_hash = alpha_hash #concat name for url

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

def pull_data(): 
    '''
    Currently this is a placeholder. TODO this will pull from a db.
    ''' 
    url = "2020SC.csv"
    df = pd.read_csv(url)
    return(df)


def retrieve_hashes():
    '''
    Function employs 'User' class to instantiate individual users.
    These five parameters are considered base for every user:
    First Name, Last Name, Email Address, ID Hash, & ID Hash Lower
    '''
    users_dict = []
    for index, row in df.iterrows():
        user = User(row['Firstname'], row['Surname'], 
        row['E-mail'], row['ID-Hash'], row['ID-Hash-Lower'])
        users_dict.append(user)
#        print(user.fullname())
        
    for i in range(len(df)):    
        print("Hash", users_dict[i].id_hash) 

df = pull_data()  
#this is called from module on PyPi      
return_hash()
#this is called in script
retrieve_hashes()        