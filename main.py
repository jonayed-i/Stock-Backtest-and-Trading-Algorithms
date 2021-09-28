# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import simfin as sf
import os
import pandas as pd
cwd = os.getcwd()
print(cwd)
# Set your API-key for downloading data. This key gets the free data.
sf.set_api_key('U0pyI7zneRqnU2qyY1GLrTxEuDsEqx3H')

# Set the local directory where data-files are stored.
# The directory will be created if it does not already exist.
sf.set_data_dir('C:/Users/joisl/PycharmProjects\pythonProject3/simfin_data/')

# Download the data from the SimFin server and load into a Pandas DataFrame.
df = sf.load_income(variant='quarterly', market='us')
df1 = sf.load_companies(market='us')
df2 = sf.load_balance(variant='quarterly', market='us')
df3 = sf.load_cashflow(variant='quarterly', market='us')

#df4 = sf.load_derived(variant='quarterly', market='us')
#df5 = sf.load_shareprices(variant='daily', market='us')
#df6 = sf.load_derived_shareprices(variant='daily', market='us')
#df7 = sf.load_industries()
# Print the first rows of the data.
df = pd.DataFrame.copy(df2)


print(df.head())