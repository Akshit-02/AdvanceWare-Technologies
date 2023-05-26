# Assignment-1
import requests
import time
import csv

with open('users.csv', 'a', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["id", "FirstName", "LastName", "Username", "Email", "Avatar", "Gender", "DoB", "Address"])
  
  counter=0
  
  while counter < 10:
    response = requests.get("https://random-data-api.com/api/v2/users")
    print(response.json())
    
    data=response.json()
    add_dict=data['address']
    address=add_dict['street_name']+","+add_dict['street_address']+","+add_dict['city']+","+add_dict['state']+","+add_dict['country']+","+add_dict['zip_code']
    writer.writerow([data['id'],data['first_name'],data['last_name'],data['username'],data['email'],data['avatar'],data['gender'],data['date_of_birth'],address])

    counter=counter+1
    
    time.sleep(1)
