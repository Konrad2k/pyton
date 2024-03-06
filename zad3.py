import random

def obliczaniePi(liczbaProbek):
    punkty=0

    for i in range(liczbaProbek):
        x=random.uniform(0,1)
        y=random.uniform(0,1)

        if x*x +y*y<=1:
            punkty+=1
    stosunek = punkty/liczbaProbek
    pi=stosunek*4
    return pi

print(obliczaniePi(10000))
