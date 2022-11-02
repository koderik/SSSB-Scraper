# import dataframe library
import pandas as pd
#import sssbdata function from listings.py
from sssbdata import sssbdata
import json

# open sssb.csv to dataframe ignore index
def scan():
    old_df = pd.read_csv("sssb.csv")
    new_df = sssbdata()
    #remove index from new dataframe
    new_df = new_df.reset_index(drop=True)
    old_df = old_df.reset_index(drop=True)


    # add new dataframe to old dataframe
    df = pd.concat([old_df, new_df], ignore_index=True)
    # save merged dataframe to csv
    return df

