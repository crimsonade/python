import json

file_name= 'fav_number.json'

fav_number= input("What is your favourite number: ")
fav_number=int(fav_number)

with open(file_name,'w') as f:
    json.dump(fav_number,f)

