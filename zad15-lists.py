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

#1
hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
print(hitsTitles)
#2
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
print(hitsTitles)
#3
hitsTitles.insert(2,"HOTEL CALIFORNIA")
print(hitsTitles)
#4
hitsTitles.insert(0,'THE SOUND OF SILENCE')
print(hitsTitles)
#5
print(hitsTitles.index('HOTEL CALIFORNIA'))
#6
hitsTitles.remove("HOTEL CALIFORNIA")
print(hitsTitles)
#7
hitsTitles[0]='ENJOY THE SILENCE'
print(hitsTitles)
#8
hitsToRead=hitsTitles.copy()
#9
print(hitsToRead.reverse())
#10
print(hitsToRead.sort())
#11
print(hitsToRead.pop(0))
print(hitsToRead.pop(0))
print(hitsToRead)
#12
additionalSongs=['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
print(additionalSongs)
#13
hitsToRead.extend(additionalSongs)
#14
print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('NOTHING COMPARES 2 U'))
#15
hitsToRead.clear()