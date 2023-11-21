import csv 

uefa_file = open("uefa.csv")

csvreader = csv.DictReader(uefa_file)

teams = {}
countries = {}

for row in csvreader:
    code = row['code']
    league = row['league']
    if code in teams:
        teams[code] += 1
    else:
        teams[code] = 1
    if league in countries:
        countries[league] += 1
    else:
        countries[league] = 1

print("TEAMS")
print(teams)

print("COUNTRIES")
print(countries)