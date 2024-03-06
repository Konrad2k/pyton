countries = ['FR','US','DE','PL']
print(countries[1])
countries[1]='GB'
print(countries[1])

countries.append('IT')
countries.insert(2,'ES')
countries.remove('DE')
countries.sort()
countries.reverse()
print(countries.pop(2))
print(countries.index('PL'))
print(countries.count('PL'))

newList=['FI','SE']
countries.extend(newList)
countriesCopy=countries.copy()
countriesCopy.clear()
print(countries)
print(countriesCopy)