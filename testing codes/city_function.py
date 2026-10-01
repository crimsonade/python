def get_city(citty,countryy,population=None):
    if population:
        location= f"{citty}, {countryy}-population= {population}"
    else:
        location= f"{citty}, {countryy}"
    return location.title()