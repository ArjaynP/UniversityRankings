import pandas as pd

TopUni = pd.read_csv("TopUni.csv")
Capitals = pd.read_csv("Capitals.csv")

#print(TopUni["World Rank"])
print()
counter = 0
for cap in Capitals["Continent"]:
    print(Capitals["Continent"][counter])
    counter += 1

selectedCountry = "Japan"
country_counter = 0
country_counter_rank = 1

print()

for country in TopUni["Country"]:
    if country == selectedCountry:
        print("At international rank =>", country_counter_rank, "the university name is =>", TopUni["Institution name"][country_counter])  # PART 4
    country_counter += 1
    country_counter_rank += 1

print()

selectedCountry = "Japan"
country_counter = 0
country_national_counter_rank = 1

print()

for country in TopUni["Country"]:
    if country == selectedCountry:
        print("At national rank =>", country_national_counter_rank, "the university name is =>", TopUni["Institution name"][country_counter])
        country_national_counter_rank += 1
    country_counter += 1
