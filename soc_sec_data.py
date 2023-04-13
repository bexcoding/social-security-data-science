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
def find_my_name(df, gender, name):
    #indexing of men is affected by women
    # returns rank in gender
    # covert index to rank
    if gender == "F":
        return (find_name(get_gender(df, "F"), name).index[0]) + 1
    elif gender == "M":
        men = get_gender(df, "M")
        first_male_index = men.index[0]
        return (find_name(men, name).index[0] - first_male_index) + 1
def find_name_over_time(gender, name):
    # gets rank of a name for all years
    all_years = np.array(range(1880, 2022))
    result_list = []
    for y in all_years:
        print(f"Checking year: {y}")
        result_list.append(find_my_name(create_df(y), gender, name))
    return result_list
def name_count(df, gender):
    # get number of different names per gender
    if gender == "F":
        return get_gender(df, "F").last_valid_index()
    elif gender == "M":
        men = get_gender(df, "M")
        return (men.last_valid_index() - men.index[0])
def name_counts_over_time(gender):
    # get number of different names per gender for all years
    all_years = np.array(range(1880, 2022))
    result_list = []
    for y in all_years:
        print(f"Checking year: {y}")
        result_list.append(name_count(create_df(y), gender))
    return result_list

# TODO questions to answer
# What are the top ten most common boy or girl names in a particular year?
# top_ten(create_df(search_year), gender)) -> list of names

# how popular was your name on your birth year?
# find_my_name(df, gender, name) -> int

# how has a given name's popularity increased or decreased over time?
# find_name_over_time(gender, name) -> list of ranks

# how many different names are in each gender in a given year?
# name_count(df, gender)

# how many different names are there in every year?
# name_counts_over_time(gender)



# how many different names are there in a given year?

# how does the most common name compare to others?

# Across all years, are there any boys or girls names that remain in the top x number of entries the whole time?

# for each gender, what percentage did the most popular name represent out of all names in that gender?

# how many names are shared for each gender over time?

# assign super spy identity