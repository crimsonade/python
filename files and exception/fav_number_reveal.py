import json
file_name= 'fav_number.json'

with open(file_name) as f: 
    fav_number= json.load(f)
    print(f"Your favourite number is {fav_number}.")

