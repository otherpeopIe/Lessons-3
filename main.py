#function -- just a chunk of code that you can rerun, can take inputs but doesn't have to, 
#            can return stuff but doesn't have to 

from player import *
#* is a programming thing meaning all -- but it also means multiplication a lot of times

from fileservice import *

#Start function, launches our game
def Start(): 
    flservice = FileService("savedata.txt")
    print("Hello World!") #intro message
    newPlayer = CreatePlayer()
    newPlayer.displaystats()
    return "bye" #returns exit message

#Create Player function handles player creation


def CreatePlayer():
    name = input("Enter your name: ") #built in input takes string and returns input string
    print("Based. Welcome " + name) #print welcome message with player name
    faction = SelectFaction()
    print("Indeed. Welcome " + name + ", a wise " + faction)
    health = 100
    defense = 100
    createdPlayer = Player(name, faction, health, defense)
    return createdPlayer
   

#Exception Handling 

def isnumber(s):
    try:
        int(s)
        return True 
    
    except:
        return False
    

def getelement(i, arr):
    try:
        return arr[i]
    
    except:
        return None
    





#Handles validating players class selection
def SelectFaction():
    exit = False #bool to use to exit loop -- (Bool is True or False)

    factions = ["Knight", "Mage", "Druid", "Shaman"] 

    while(exit == False): #if bool 'exit' is true, exit loop
                          #while exit is false, run loop code
        exit = False

        numfactions = len(factions)

        for i in range(numfactions):
            print(str(i + 1) + ". " + factions[i]) #1. Knight -- example of what the end result is doing


        classChoice = input() #input without prompt (no string input) 
                              #string is any text
                              #reading input suspends the thread

    
        if isnumber(classChoice):
            selection = getelement(int(classChoice) - 1, factions)
            if selection != None: 
                classChoice = selection
                exit = True
        
        if exit == False:
            print("Not valid selection")
        

        #end of while loop, jump back to top and check if exit is true

    return classChoice 


#entry point
byeMessage = Start() #variable, most languages you need to write var or string or something
print(byeMessage)

