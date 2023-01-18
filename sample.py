infileCaptials = open("capitals.csv", "r")
infileTopUni = open("TopUni.csv", "r")
readfile1 = infileCaptials.readlines()
readfileTopUni = infileTopUni.readlines()

for line in readfile1:
    print(line[0])

infileCaptials.close()

print()
print()

number_of_countries = 0


"""
for line in range(1, len(readfileTopUni)):
    number_of_countries += 1

for line in readfileTopUni:
    print(line)

counter = 0

for line in range(len(readfileTopUni)):
    counter += 1

print(counter)

# print(number_of_countries)

infileTopUni.close()
"""

countries_lst = ["canada", "germany", "us"]

countries = ""
for i in countries_lst:
    if countries == "":
        countries = countries + i
    else:
        countries = countries + ", " + i

print(countries)
