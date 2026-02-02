names = ["math", "science", "history", "art"]
for name in names: #"in" in loop is a membership operator
    print(name)
print()

postal = {"delhi": 110001, "mumbai": 400001, "chennai": 600001}
for city in postal:
    print(city, postal[city])

for city in postal:
    if city not in postal: # it prints nothing as all cities are in postal if the city actually exists in postal
        print(city)