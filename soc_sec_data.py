"""
Title: Social Security Data - Baby Names
Description: Work with 140 years of baby names in the US.
Last Updated: April 11, 2023
Developer: Alexander Beck
Email: beckhv2@gmail.com
Github: https://github.com/bexcoding
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def create_df(search_year):
    # creates data frame
    # replace file directory with correct local directory
    return pd.read_csv(f"/home/nova/Downloads/names/yob{search_year}.txt", 
                     names=["name", "sex", "number"])

def get_gender(df, gender):
    # return either male or female half of df
    if gender == "M":
        return df[df["sex"] == "M"]
    elif gender == "F":
        return df[df["sex"] == "F"]
    
def add_number_total(df):
    # add number column
    return df["number"].sum()

def top_ten(df, gender):
    # create df and get top ten names for men or women
    top_ten_df = get_gender(df, gender).iloc[:10]
    return np.array(top_ten_df["name"])




#print(add_number_total(get_gender(create_df(1880), "F")))
