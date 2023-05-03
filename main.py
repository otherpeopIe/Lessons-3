#function -- just a chunk of code that you can rerun, can take inputs but doesn't have to, 
#            can return stuff but doesn't have to 

#Start function, launches our game
def Start(): 
    print("Hello World!") #intro message
    CreatePlayer()
    return "bye" #returns exit message

#Create Player function handles player creation
def CreatePlayer():
    name = input("Enter your name: ") #built in input takes string and returns input string
    print("Based. Welcome " + name) #print welcome message with player name
    SelectClass() 

   
#Handles validating players class selection
def SelectClass():
    exit = False #bool to use to exit loop -- (Bool is True or False)
    while(exit == False): #if bool 'exit' is true, exit loop
                          #while exit is false, run loop code
        exit = True
        print("Select class")
        print("a: Knight")
        print("b: Mage")
        print("c. Druid")
        print("d. Shaman")
        
        classChoice = input() #input without prompt (no string input) 
                              #string is any text
        
        if (classChoice == "a"): # == is saying is it equal to (like a question, does this equal this?), = is an assignment (this now equals this)
            classChoice = "Knight"
        elif (classChoice == "b"):
            classChoice = "Mage"
        elif (classChoice == "c"):
            classChoice = "Druid"
        elif (classChoice == "d"):
            classChoice = "Shaman"
        else:
            print("Not valid selection")
            exit = False #wasnt given valid selection, you cannot exit)

        #end of while loop, jump back to top and check if exit is true

    print("Exited while loop")

   


#entry point
byeMessage = Start() #variable, most languages you need to write var or string or something
print(byeMessage)

