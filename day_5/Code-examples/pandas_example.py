'''Pandas is a Python library used for working with data sets. It is often used to work with data stored in csv files.'''

# This was broken during class because I broke a cardinal rule of python naming conventions. I named a file pandas.py and then tried to import pandas.
# In doing so I overwrote the pandas module with my own file. This is why I had to rename the file to pandas_example.py

import pandas as pd
import datetime
import random


# # Create a dataframe
df = pd.DataFrame(columns=["Full Name", "Age", "Birthdate"])
list_of_abcs = [chr(i) for i in range(65, 91)]

# Create a function to generate random data for the name and birthdate columns
# Then get the age from the birthdate

def generate_data():
    '''Generate random data for the dataframe'''
    name = ''
    name = name.join(random.choices(list_of_abcs, k=5))
    birthdate = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365*100))
    age = datetime.datetime.now().year - birthdate.year
    return name, age, birthdate
# output the dataframe to a csv file

for i in range(10):
    name, age, birthdate = generate_data()
    df.loc[i] = [name, age, birthdate]

df.to_csv('data.csv', index=False)

df.head()
df.eval('Age > 30', inplace=True)




