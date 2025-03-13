def get_countries_starting_with(countries, letter):
    result = []
    for country in countries:
        if country[0] == letter:
            result.append(country)

    return result

countries = ["Berlin", "USA", "Mexico","Nepal"]

for country in countries:
    print(country)
print("-----------------------")
countries.append("Brazil")
for country in countries:
    print(country)

print("-----------------------")
countriesWithU = get_countries_starting_with(countries, "U")

print(countriesWithU)