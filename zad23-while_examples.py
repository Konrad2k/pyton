cargo=[40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()

print(cargo)

boxCapacity=90
box=[]
i=0


while  i<len(cargo) and (boxCapacity - sum(box)) >= min(cargo):
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1
    
print("the collected items sum is:",sum(box))
print("the elements are: ",box)

#-------

# number=1
# previousNumber=0

# while number<50:
#     print(f"{previousNumber} + {number} = ",previousNumber+number)
#     previousNumber=number
#     number+=1

#-------------

# import random
# my_number = random.randint(0,20)
# guess=-1
# trials = 0
 
# print("Guess my number!")
 
# while guess != my_number :
 
#     guess = int(input())
#     trials+=1
    
#     if guess == my_number:
#         print("You are right! It was:",my_number,"You needed",trials,"trials.")
#     elif guess>my_number:
#         print("Sorry- my number is smaller than", guess, "Try again!")
#     else:
#         print("Sorry- my number is greater than", guess, "Try again!")
 
 
 