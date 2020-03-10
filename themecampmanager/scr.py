from themecampmanager.mods import return_hash
import pandas as pd

#return_hash()


url = "2020SC.csv"
#import_sheet(url)
df = pd.read_csv(url)
print(df['Firstname'][0], df['Surname'][0], df['E-mail'][0], 
      df['ID-Hash'][0], df['ID-Hash-Lower'][0])