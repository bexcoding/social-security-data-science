# Social Security Data Science

This project makes use of government CSV records of Social Security applications for over 100 years. The data is a series of CSV files found at [SSA.gov](https://www.ssa.gov/oact/babynames/limits.html) that span the years 1880 - 2021. Each year has its own file name "yobYYYY.txt" where YYYY is the year of interest. Each row has the format "name,sex,number" and represents the number of individuals with a certain name in that year to apply for a Social Security card split by gender. For privacy, at least 5 occurrences of a specific name are needed to make the list as to not single out anyone with an extremely unusual name. The data is limited to U.S.A. and roughly approximates the number of babies in a certain year to be named a particular name. There are some exceptions as not everyone who applies for a Social Security card is an infant and not every parent applies for a Social Security card, especially in the early years of Social Security. This means that the data cannot be used to tell the exact population growth in the U.S.A. in a particular year but it can provide a close approximation given the size of the data set.

# Getting Started

**TODO** explain setup to try code for self

Data sized unpacked = 24 - 400 kb per file * 141 files = 26.6MB
zipped data size = 7MB

# Questions to Answer

**TODO** explain which questions this project seeks to answer

# Use Cases

**TODO** describe the applications of these functions
