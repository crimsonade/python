import json

file_name= 'fav_number.json'

def get_user_input():
    fav_number= input("What is your favourite number: ")
    fav_number= int(fav_number)

    with open(file_name,'w') as f:
        json.dump(fav_number,f)
        return fav_number

def get_stored_input():

    try:
        with open(file_name) as f:
            fav_number= json.load(f)
            return fav_number 

    except FileNotFoundError:
        return None

def fav_number_remembered():
    fav_number= get_stored_input()
    if fav_number is not None:
        print(f"Your favourite number is {fav_number}")

    else:
        fav_number= get_user_input()
        print(f"We will save {fav_number} as your favourite number.")
#get_user_input()
fav_number_remembered()


