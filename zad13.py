ciag=input("podaj ciag o dowolnej dlugosci ")

samogloski={'a':0,'e':0,'i':0,'o':0,'u':0,'y':0}

for i in ciag:
    if i in samogloski:
        samogloski[i]+=1

for slowo,ilosc in samogloski.items():
    print(f"{slowo}: {ilosc}")