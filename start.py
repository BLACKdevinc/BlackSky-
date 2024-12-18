

from timeline import Timeline




print("====BlackSky==== TEST DEMO")
print("Set player name : ")
playerName = input()
print("Welcome, base year is : ")
print("1.Select Mission")
print("2.Exit")

choice = 0


while choice != "1" and "2":
    choice = input()
    if choice == "1":
        tml = Timeline()
        tml.generateMission()
    elif choice == "2":
        exit()        
    else:
        print("Incorrect input")
        
        
