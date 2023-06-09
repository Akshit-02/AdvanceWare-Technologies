# Assignment-1
# Importing libraries
import requests
import time
import csv

# Creating/Opening the csv file
with open('users.csv', 'a', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["id", "FirstName", "LastName", "Username", "Email", "Avatar", "Gender", "DoB", "Address"])
  
  counter=0
  
  while counter < 10:
#   Making get request to the random api
    response = requests.get("https://random-data-api.com/api/v2/users")
    print(response.json())
    
#   Appending the users data fetched from random api in csv file  
    data=response.json()
    add_dict=data['address']
    address=add_dict['street_name']+","+add_dict['street_address']+","+add_dict['city']+","+add_dict['state']+","+add_dict['country']+","+add_dict['zip_code']
    writer.writerow([data['id'],data['first_name'],data['last_name'],data['username'],data['email'],data['avatar'],data['gender'],data['date_of_birth'],address])

    counter=counter+1
    
#   Making get request every 1 sec
    time.sleep(1)
