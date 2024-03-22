age=20
isDrunk=0
isRestricted=False

if age <18:
    print("you are too young to buy alcohol")
else:
    if isDrunk:
        print("are you drunk? we cannot sell you alcohol")
    else:
        if isRestricted:
            print("restricted area, alcohol is forbidden")
        else:
            print("ok, you can buy alcohol")

print("---------")

if age <18:
        print("you are too young to buy alcohol")
elif isDrunk:
             print("are you drunk? we cannot sell you alcohol")
elif isRestricted:
        print("restricted area, alcohol is forbidden")
else:
        print("ok, you can buy alcohol")
        
print("---------")

like=500
share=50

if like<500:
    print("not enough likes :c")
elif share <100:
      print("not enough shares :c")
else:
      print("hooray, promotion starts!")