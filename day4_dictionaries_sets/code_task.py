country_count = {}
unique_countries = set()

with open("cities.csv", "r") as file:
    next(file)  # Skip header
    for line in file:
        city, country = line.strip().split(",")

        if country in country_count:
            country_count[country] += 1
        else:
            country_count[country] = 1
            unique_countries.add(country)

for country, count in country_count.items():
    print(f"{country}: {count} cities")

print(f"Unique countries: {unique_countries}")
