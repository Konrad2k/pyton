# values=[10,43,12,48,12,11,18,98,57,28,19,27,29,19,74]

# i=0
# max = len(values)-2

# while i<max:
#     print(i,values[i],values[i+1],values[i+2])

#     if values[i]<values[i+1]<values[i+2]:
#         print('\tFound: ',values[i],values[i+1],values[i+2] )
#     i+=1

#-----------------------------

# numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

# i=0
# max = len(numbers)-1

# while i<max:
#     if numbers[i]**2==numbers[i+1]:
#         print('/tFound: ', numbers[i], numbers[i+1])
#     i+=1

#-----------------

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i=0
max=len(texts)-1

while i<max:
    if len(texts[i])==len(texts[i+1]):
        print('found!: ',texts[i],texts[i+1])
    i+=1