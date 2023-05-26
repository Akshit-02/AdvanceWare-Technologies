# Assignment-1 (A)
import pandas as pd
import csv
data=pd.read_csv("users.csv")

print("Data before sorting: ")
print(data)

data.sort_values("FirstName",inplace=True)

print("Data after sorting: ")
print(data)

data.to_csv("users-sorted.csv")
