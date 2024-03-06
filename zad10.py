
element=5

lista=[1,'14','kra']

lista.extend([False,'yes',5])

lista2=[5,'tak','pi']

lista2.extend([True,'no',51])

tablica1=lista.count(element)
tablica2=lista2.count(element)
ilosc=tablica1+tablica2

if tablica1 >0 or tablica2 >0:
    print(f"element {element} wystepuje {ilosc} razy")
else:
    print(f"element {element} nie wystepuje wcale")

