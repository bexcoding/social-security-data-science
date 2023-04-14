"""
Title: Social Security Data - Baby Names
Description: Work with 140 years of baby names in the US.
Last Updated: April 13, 2023
Developer: Alexander Beck
Email: beckhv2@gmail.com
Github: https://github.com/bexcoding
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ALL_YEARS = np.array(range(1880, 2022))
WOMENS_OLD_TOP_FIVE= ["Mary", "Anna", "Emma", "Elizabeth", "Minnie"]
MENS_OLD_TOP_FIVE = ["John", "William", "James", "Charles", "George"]


def create_df(search_year):
    """
    Description
    ----------
    Creates a Pandas dataframe for a specific year using local csv files.

    Parameters
    ----------
    search_year: int
        Int in range of [1880, 2021]
    """

    # replace file directory below with correct local directory
    return pd.read_csv(f"/home/nova/Downloads/names/yob{search_year}.txt", 
                     names=["name", "sex", "number"])


def get_gender(df, gender):
    """
    Description
    ----------
    Takes a dataframe and returns a dataframe with only male or female entries

    Parameters
    ----------
    df: Pandas dataframe
        A dataframe with "name,sex,number" categories.
    gender: string
        Either "M" for male or "F" for female.
    """

    if gender == "M":
        return df[df["sex"] == "M"]
    elif gender == "F":
        return df[df["sex"] == "F"]
    

def add_number_total(df):
    """
    Description
    ----------
    Takes a dataframe and sums up the numbers category. If given a single gender
    dataframe, returns total number of males or females.

    Parameters
    ----------
    df: Pandas dataframe
        A dataframe with "name,sex,number" categories.
    """

    return df["number"].sum()


def top_ten(df, gender, search_year, to_string=False):
    """
    Description
    ----------
    Takes an existing dataframe and returns the top ten names for men or women.
    If to_string is True, returns a string of the names, else returns np.array.

    Parameters
    ----------
    df: Pandas dataframe
        A dataframe with "name,sex,number" categories.
    gender: string
        Either "M" for male or "F" for female.
    search_year: int
        Int in range of [1880, 2021].
    to_string: bool
        Determines if result of function is list or string. Default is False.
    """

    def top_ten_string():
        return f"The most popular names in {search_year} were " + \
                ", ".join(names[:-1]) + f", and {names[-1]}."
    
    top_ten_df = get_gender(df, gender).iloc[:10]
    names = np.array(top_ten_df["name"])
    if to_string == True:
        return top_ten_string()
    else:
        return names


def find_name(df, name):
    """
    Description
    ----------
    Returns dataframe rows with a matching name. If only one gender is passed in
    then will return one name. If both genders included, can return two names.

    Parameters
    ----------
    df: Pandas dataframe
        A dataframe with "name,sex,number" categories.
    name: string
        A valid name it title case with no extra characters or whitespace.
    """

    return df[df["name"] == name]


def find_my_name(df, gender, name):
    """
    Description
    ----------
    Returns a numeric rank  for a specific name in a specific gender. For
    example, a return value of 1 indicates that the name was the number 1 name
    in that year for that gender.

    Parameters
    ----------
    df: Pandas dataframe
        A dataframe with "name,sex,number" categories.
    gender: string
        Either "M" for male or "F" for female.
    name: string
        A valid name it title case with no extra characters or whitespace.
    """

    if gender == "F":
        rank = (find_name(get_gender(df, "F"), name).index[0]) + 1
        return rank
    elif gender == "M":
        men = get_gender(df, "M")
        # men's indexing is affected by all women's indexing beforehand
        first_male_index = men.index[0]
        rank = (find_name(men, name).index[0] - first_male_index) + 1
        return rank
    
    
def find_name_over_time(gender, name):
    """
    Description
    ----------
    Returs a list of the rank of a name from 1880 to 2021. Separated by gender.

    Parameters
    ----------
    gender: string
        Either "M" for male or "F" for female.
    name: string
        A valid name it title case with no extra characters or whitespace.
    """

    result_list = []
    for y in ALL_YEARS:
        print(f"Checking year: {y}")
        result_list.append(find_my_name(create_df(y), gender, name))
    return result_list


def name_count(df, gender):
    """
    Description
    ----------
    Returns the total number of names a gender has in a dataframe.

    Parameters
    ----------
    df: Pandas dataframe
        A dataframe with "name,sex,number" categories.
    gender: string
        Either "M" for male or "F" for female.
    """

    if gender == "F":
        return get_gender(df, "F").last_valid_index()
    elif gender == "M":
        men = get_gender(df, "M")
        return (men.last_valid_index() - men.index[0])
    
    
def name_counts_over_time(gender):
    """
    Description
    ----------
    Returns a list of the number of different names that a gender had from 1880
    to 2021.

    Parameters
    ----------
    gender: string
        Either "M" for male or "F" for female.
    """

    result_list = []
    for y in ALL_YEARS:
        print(f"Checking year: {y}")
        result_list.append(name_count(create_df(y), gender))
    return result_list


def plot_name_over_time(gender, name):
    """
    Description
    ----------
    Returns a line plot of a name's popularity over time in a given gender.

    Parameters
    ----------
    gender: string
        Either "M" for male or "F" for female.
    name: string
        A valid name it title case with no extra characters or whitespace.
    """

    y = find_name_over_time(gender, name)
    plt.title("Rank (Popularity) of Name Over Time")
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.plot(ALL_YEARS, y)
    plt.ylim((max(y) * 1.25) ,0)
    plt.xlim(1880, 2021)
    plt.show()


def plot_women_top_five():
    """
    Description
    ----------
    Returns a line plot of the change in popularity of the top five most popular
    women's names from 1880.
    """

    for name in WOMENS_OLD_TOP_FIVE:
        y = find_name_over_time("F", name)
        plt.plot(ALL_YEARS, y, label=name)
    plt.title("Rank (Popularity) of Name Over Time")
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.ylim(300 ,0)
    plt.xlim(1880, 2021)
    plt.legend()
    plt.show()


def plot_men_top_five():
    """
    Description
    ----------
    Returns a line plot of the change in popularity of the top five most popular
    men's names from 1880.
    """

    for name in MENS_OLD_TOP_FIVE:
        y = find_name_over_time("M", name)
        plt.plot(ALL_YEARS, y, label=name)
    plt.title("Rank (Popularity) of Name Over Time")
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.ylim(200 ,0)
    plt.xlim(1880, 2021)
    plt.legend()
    plt.show()


def plot_name_counts():
    """
    Description
    ----------
    Returns a line plot of the change in the number of different names each
    gender had over time.
    """

    plt.plot(ALL_YEARS, name_counts_over_time("M"), label="Male Names")
    plt.plot(ALL_YEARS, name_counts_over_time("F"), label="Female Names")
    plt.title("Number of Different Names Over Time \n By Gender")
    plt.xlabel("Year")
    plt.ylabel("Number of Different Names")
    plt.grid()
    plt.legend()
    plt.show()