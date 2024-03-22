itRains=True

if itRains:
    print("we stay at home")
else:
    print("we go out")

print("we stay at home" if itRains else "we go out")

print("------------")

musclePain=False
fever=True
weakness=True
isMan=True

if musclePain and fever and weakness:
    print("suspicion of influenza")
elif not (musclePain and fever) and weakness:
    print("just take a rest")
else:
    print("this may be a cold")

if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print("suspicion of influenza")
elif not (musclePain and fever) and weakness:
    print("just take a rest")
else:
    print("this may be a cold")


isCheckCompleted = True
 
print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")