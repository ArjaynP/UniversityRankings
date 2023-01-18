import pandas as pd


"""
available_countries = 0
Capitals = pd.read_csv("Capitals.csv")
countries_lst = []
countries = ""

for country in Capitals["Country Name"]:
    if country not in countries_lst:
        countries_lst.append(country)
    available_countries += 1

for country in countries_lst:
    if countries == "":
        countries = countries + country
    else:
        countries = countries + ", " + country


print("Available countries =>", countries)                                                                                    # PART 2
"""

def calculateRelativeScore(rankingFileName, selectedCountry):
    number_of_universities = 0
    university_score = 0
    TopUni = pd.read_csv(rankingFileName)
    highestScore = 0
    counter1 = 0
    counter2 = 0
    asia = ["Jordan", "Palestine", "China", "Israel", "Japan", "Singapore", "South Korea", "Taiwan"]
    australia = ["Australia"]
    north_america = ["Canada", "USA"]
    europe = ["Denmark", "France", "Germany", "Netherlands", "Norway","Sweden", "Switzerland", "United Kingdom"]
    africa = ["Egypt"]


    for country in TopUni["Country"]:
        if selectedCountry == country:
            university_score += TopUni["Score"][counter1]
            number_of_universities += 1
        counter1 += 1

    averageScore = university_score / number_of_universities

    for continentScore in TopUni["Score"]:
        if (selectedCountry == TopUni["Country"][counter2]) or (TopUni["Country"][counter2] in asia):
            if continentScore > highestScore:
                highestScore = continentScore
        elif (selectedCountry == TopUni["Country"][counter2]) or (TopUni["Country"][counter2] in australia):
            if continentScore > highestScore:
                highestScore = continentScore
        elif (selectedCountry == TopUni["Country"][counter2]) or (TopUni["Country"][counter2] in north_america):
            if continentScore > highestScore:
                highestScore = continentScore
        elif (selectedCountry == TopUni["Country"][counter2]) or (TopUni["Country"][counter2] in europe):
            if continentScore > highestScore:
                highestScore = continentScore
        elif (selectedCountry == TopUni["Country"][counter2]) or (TopUni["Country"][counter2] in africa):
            if continentScore > highestScore:
                highestScore = continentScore
        counter2 += 1

    relativeScore = averageScore / highestScore
    print(relativeScore)


file1 = input("Input the file of the Top Universities: ")
file2 = input("Input the file of the capitals: ")
country = input("input the country you want to look at: ")
calculateRelativeScore(file1, country)
