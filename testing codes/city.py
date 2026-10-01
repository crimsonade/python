from city_function import get_city

print("Please enter 'q' to quit at any time.")

while True:
    city= input("\nPlease enter your city name: ")
    if city == 'q':
        break
    country= input("Please enter your country name: ")
    if country == 'q':
        break
    f_city= get_city(city, country)
    print(f"\tNeatly formatted location details: {f_city}")
    