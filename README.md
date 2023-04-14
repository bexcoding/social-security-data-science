# Social Security Data Science

This project makes use of government CSV records of Social Security applications for over 100 years. The data is a series of CSV files found at [SSA.gov](https://www.ssa.gov/oact/babynames/limits.html) that span the years 1880 - 2021. Each year has its own file name "yobYYYY.txt" where YYYY is the year of interest. Each row has the format "name,sex,number" and represents the number of individuals with a certain name in that year to apply for a Social Security card split by gender. For privacy, at least 5 occurrences of a specific name are needed to make the list as to not single out anyone with an extremely unusual name. The data is limited to U.S.A. and roughly approximates the number of babies in a certain year to be named a particular name. There are some exceptions as not everyone who applies for a Social Security card is an infant and not every parent applies for a Social Security card, especially in the early years of Social Security. This means that the data cannot be used to tell the exact population growth in the U.S.A. in a particular year but it can provide a close approximation given the size of the data set.

# Getting Started

To be able to run the code in `soc_sec_data.py`, follow these steps:

1. Make sure that you have a python interpreter downloaded on your computer.
1. Install `pandas`, `numpy`, and `matplotlib` modules if not already installed.
1. Download the CSV files from the SSA.gov website listed above. They could not be hosted here because of size. When zipped, they take up 7MB of memory but unzipped, they take up 26.6MB. When on the website, just click the link labeled `National data (7Mb)`. When downloaded, unzip the files in a location that you want.
1. Clone this `social-security-data-science` repository either on the GitHub website or in the terminal.
1. Change the directory for the CSV files in the `soc_sec_data.py` file in the `create_df()` function. The directory that I included will only work on my system. My directory is "/home/nova/Downloads/names/yob{search_year}.txt". Replace the section "/home/nova/Downloads/names" with the directory for the folder that holds the unzipped CSV files.

After following each of these steps, you should be able to run any of the functions in this code.

# Questions to Answer

This project was meant to answer some general questions about names and how they have changed in the past century and a half in this country. I have attempted to create a series of functions capable of searching for the answers in this data set. Many more questions and answers could be formulated with this data set.

1. What are the top ten most common boy or girl names in a particular year?
   Example usage: `top_ten(create_df(1960), "M", 1960, to_string=True)` returns the string 'The most popular names in 1960 were David, Michael, James, John, Robert, Mark, William, Richard, Thomas, and Steven.'
1. How popular was my name on my birth year? 
   Example usage: `find_my_name(create_df(1990), "M", "Tom")` returns 696. This means if my name were Tom and I was born in 1990, my name would have been the 696th most popular name for boys in that year. Not very popular after all!
1. How has a given name's popularity increased or decreased over time?
   Example usage: `find_name_over_time("M", "Samuel")` returns an array of 141 values, 1 value for every year in the data set. Like `find_my_name()`, each value represents the popularity of that name in that year.
1. How many different names are in each gender in a given year?
   Example usage: `name_count(create_df(1950), "F")` returns 6109. This means that there were 6,109 different girl's baby names in 1950 (counting names with at least 5 people having that name).
1. How many different names are there in every year, by gender?
   Example usage: `name_counts_over_time("F")` returns an array of values that represent the total number of women's names that year. The first value is 941 and the last value is 17,543. 
   
# Example Usage of Graphs

Here are example uses of the plotting functions that I wrote along with potential questions that the graphs answer and questions that the graphs raise:

### Name Popularity 

Question: How does the popularity of the name Joseph change over time?

Code: `plot_name_over_time("M", "Joseph")` 

![Plotting name Joseph over time](https://github.com/bexcoding/social-security-data-science/blob/main/example-graphs/plot-name-joseph.png)

Observations: The name Joseph has had ups and downs over time and was originally a very popular name. Since the year 2000, it has been in sharp decline and is trending to become a more unpopular name.

New Questions raised: Is the name becoming less popular because people prefer shorter, more casual versions like Joe?

---

Question: How does the popularity of the name Rebecca change over time?

Code: `plot_name_over_time("F", "Rebecca")`

![Plotting name Rebecca over time](https://github.com/bexcoding/social-security-data-science/blob/main/example-graphs/plot-name-rebecca.png)

Observations: The name Rebecca was very popular for women between 1940 and 2000. Before and after that time period, the name experienced decreasing popularity.

New Questions raised: What cultural event prompted 60 years of increased popularity of this name?

### Classic Men's and Women's Names

Question: How did the popularity of the five most popular women's names in 1880 change over time?

Code: `plot_women_top_five()` 

![Plotting five women's names](https://github.com/bexcoding/social-security-data-science/blob/main/example-graphs/plot-top-women.png)

Observations: The name Mary remained one of the most popular women's names for almost 80 years. The name Minnie almost immediately became unpopular and never seemed to become popular again. The name Emma had a drastic decline in popularity and returned to popularity nearly 100 years later.

New Questions raised: Are there other, more stable female names or do female names change frequently in popularity? Why does the popularity of women's names change so frequently?

---

Question: How did the popularity of the five most popular men's names in 1880 change over time?

Code: `plot_men_top_five()`

![Plotting five men's names](https://github.com/bexcoding/social-security-data-science/blob/main/example-graphs/plot-top-men.png)

Observations: The top five men's names seem more stable than the top women's names. It takes almost 80 years for any of the five names to make a significant change in popularity. When they do change in popularity, the change less drastically than the women's names. The top four of five men's names end up ranked in the top 50 while the top four women's names end up spread out over the top 125 ranks.

New Questions raised: Is there a selection of women's names where the results are similarly stable when compared to the men's names?

### Number of Different Names

Question: How did the total number of men's and women's names change over time? Are there more female or male names?

Code: `plot_name_counts()`

![Plotting name counts](https://github.com/bexcoding/social-security-data-science/blob/main/example-graphs/plot-different-names.png)

Observations: In nearly every single year, women have more names to choose from than men. There has been an overall trend of increasing name diversity in the U.S.A. over time. There are about ten times as many different names now as there were in 1880.

New Questions raised: Is the increase in different names over time because of the increase in the number of people from different cultures coming to the U.S.A.? Is the increase because of non-conventional/non-traditional names or because of changes in spellings of certain names (Sierra vs Siera or Sara vs Sarah)?

# Improvements

This project has been very fun but it is not perfect. Here are some changes that I think would be beneficial:

1. Type checking: The types for the inputs are not checked. This means that someone could enter the wrong type of argument for the various functions and the program would crash. I think this is generally acceptable for now because it is a series of functions that need to be called by a user experienced with calling functions. You can't just press start and expect the file to run top to bottom. These functions would be imported and their documentation would need to be referenced regardless.
1. Solving for missing names: Not all names will work when searched for. Currently, they make the program crash because there is no default response that the function has built in for the situation in which the given name is absent from the data.
1. Binary nature of the data: This data set is binary. It only has male and female options. This was appropriate for the majority of the time span for this data, but it makes this data not as complete these days. There are gender subtleties now that may affect the results of the data because some people do not consider themselves to fit into either a male or female group.
