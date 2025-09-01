countries = {
    "Pakistan": 2300000,
    "India": 15000000,
    "Bangladesh": 2800000,
    "China": 16000000,
    "Japan": 150000
}

top3 = []

for i in range(3):
    max_country = None
    #taking value of smallest population as reference
    max_pop = 150000
    for c in countries:
        if c not in top3 and countries[c] > max_pop:
            max_country = c
            max_pop = countries[c]
    top3.append(max_country)

for c in top3:
    print(c, countries[c])