# Assignment-1 (A)
# Importing libraries
import pandas as pd
import csv

# Opening the csv file
data=pd.read_csv("users.csv")

print("Data before sorting: ")
print(data)

# Sorting the users.csv file data according to FirstName
data.sort_values("FirstName",inplace=True)

print("Data after sorting: ")
print(data)

# Writing sorted data to users-sorted.csv file
data.to_csv("users-sorted.csv")
