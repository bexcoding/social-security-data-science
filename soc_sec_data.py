"""
Title: Social Security Data - Baby Names
Description: Work with 140 years of baby names in the US.
Last Updated: April 12, 2023
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


def find_name(df, search_name):
    # can find name in men and women; isolate by passing one gender
    return df[df["name"] == search_name]

def find_my_name(df, search_year, gender, name):
    #indexing of men is affected by women
    if gender == "F":
        return find_name(get_gender(create_df(search_year), gender), name).index[0]
    elif gender == "M":
        pass

# TODO questions to answer
# What are the top ten most common boy or girl names in a particular year?
# top_ten(create_df(search_year), gender))

# how popular was your name on your birth year?
# find_name(get_gender(create_df(search_year), gender), search_name)
print(find_my_name(create_df(1997), 1997, "M", "Alex"))

# 2. Across all years, are there any boys or girls names that remain in the top x number of entries the whole time?
#    input: number of entries (10 = top ten names)
#    output: true/false OR a name?

# 4. given a name, how has that names popularity increased or decreased over time?
#    in: name
#    out: series of ranks for each data set, maybe graph
# 5. for each gender, what percentage did the most popular name represent out of all names in that gender?
#    in:
#    out: percent of total share of males that had the most popular name, same for females
# 6. how many names are shared for each gender over time?
#    in:
#    out: number of shared names over time, increasing or decreasing
# 7. how many different names are in each gender, do they increase or decrease over time?
#    in:
#    out: number of names shared between gender per year
# 8. assign super spy identity:
#    in: year, gender, common vs non common name
#    out: dob, name * 10
