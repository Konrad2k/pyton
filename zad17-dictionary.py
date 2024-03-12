CountryLeaders={'PL':'Duda','US':'Biden'}
CountryLeaders['DE']='Merkel'
print(CountryLeaders['US'])

#print(CountryLeaders.keys())
#print(CountryLeaders.values())
#print(CountryLeaders.items())
print(CountryLeaders.popitem())

print(CountryLeaders.setdefault('FR','Macron'))

NewLeaders={'RU':'Putin','DE':'Scholz'}
print(NewLeaders)

CountryLeaders.update(NewLeaders)

print(CountryLeaders)

#exercises
#1
channels={'Google':1480,'Email':300,'natural traffic':440,'TV sport':700}
#2
print(channels['Email'])
#3
channelsUpdate={'natural traffic':520,'News':600}
#4
channels.update(channelsUpdate)
#5
print(channels.keys())
#6
print(channels.pop('Email'))
print(channels)