# Assignment-1 (B)
# Importing libraries
import csv

# Taking id no. as input 
id=input("Enter id to search: ")

# Reading the users.csv file
file=csv.reader(open("users.csv","r"),delimiter=',')

# Searching id no. in the file
for i in file:
  if i[0]==id:
    print("Id: ",i[0])
    print("First Name: ",i[1])
    print("Last Name: ",i[2])
    print("Username: ",i[3])
    print("Email: ",i[4])
    print("Avatar: ",i[5])
    print("Gender: ",i[6])
    print("Date of birth: ",i[7])
    print("Address: ",i[8])
  
