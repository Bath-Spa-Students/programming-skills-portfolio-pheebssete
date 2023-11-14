def describe_city(city, country='Philippines'):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Manila')
print()
describe_city('San Francisco', 'America')
print()
describe_city('Bicol City')
