# IsWeekend=False
# print("is weekend=",IsWeekend)
# Temperature=5
# print("Temperature =", Temperature)

# toDoList='SHOPPING'
# print("ToDoList =",toDoList)

# IsHappy=not IsWeekend and Temperature >20 and toDoList==''\
# or not IsWeekend and Temperature <20 and toDoList!=''
# print("IsHappy=",IsHappy)

isAutomaticMode=1
print("Automatic mode:   ",isAutomaticMode)
is80PercentLight=1
print("Is the light good:",is80PercentLight)
isDirectLignt=0
print("Is sun low:       ",isDirectLignt)
isRainy=1
print("Is it rainy:      ",isRainy)

turnLightsOn=isAutomaticMode and( not is80PercentLight or isDirectLignt or isRainy )
print("TURN LIGHTS ON:   ",turnLightsOn)

