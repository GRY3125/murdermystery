inventorylist=["apple"]
currentplace=13 # xy = (x,y) coordinate

def CommandV(): 
    check=0
    while check==0: 
        CommandInput=input("\n>")
        CommandSplit=CommandInput.split()
        if len(CommandInput)>0: 
            FirstCmd=CommandSplit[0]
            if FirstCmd in ["look", "l", "examine", "x", "inventory", "inv", "i", "use", "u", "north", "n", "east", "e", "south", "s", "west", "w", "get", "help", "h", "interact", "e"]: 
                check=1
                return CommandInput
            else: 
                print("Invalid command. Type 'help' for a list of valid commands...")
        else: 
            print("An empty void... Are you lost? \nType 'help' for a list of valid commands...")
            
            
def BoldText(Input): 
    Input="\033[1m"+Input+"\033[0m"
    return Input
def UnderlineText(Input): 
    Input="\033[4m"+Input+"\033[0m"
    return Input

print("\n\n"+BoldText("The Murder Of James Brown"))
print("It is currently the year of 1983, and as a well-renowned chief detective of the Malaysian police department, you have recently been given an unusual case to investigate on the murder of a 12 year old boy taking place in the suburbs of a farmland. You arrive at the crime scene, with hopes of finding clues and hopefully find the murderer. \n\nYou are currently at (1,3), type 'help' to check your current location or view a list of all possible commands whenever you need to...")

game=0
while game==0: 
    commandinput=CommandV() 
    commanddd=commandinput.split()
    commanddd=commanddd[0]
    # commandinput = entire input from user
    # commanddd = first command / cmd category
    
    
    if  commanddd in ["help", "h"]: 
        xCoOrd=currentplace//10
        yCoOrd=currentplace%10
        print("Your current location is ("+str(xCoOrd)+", "+str(yCoOrd)+")...")
        print("\n'north'/'n': go north \n'east'/'e': go east \n'south'/'s': go south \n'west'/'w': go west")
        print("'look'/'l': look at your surroundings \n'examine'/'x': examine an object \n''inventory'/'inv'/'i': check your inventory")
        print("'use'/'u': use an object \n'get': get an object \n'interact'/'e': interact with a character")


    if commanddd in ["inventory", "inv", "i"]: 
        print(*inventorylist)
        if commanddd!=commandinput: 
            print("Everything behind "+commanddd+" is ignored...")
    
    
    
    if commanddd in ["north", "n", "east", "e", "south", "s", "west", "w"]: 
        if commanddd in ["east", "e"] and currentplace in [51, 52, 53]: 
            print("You stand at the edge of the riverbank, and after careful consideration, you decide that going into the river is not wise. Perhaps there is a bridge somewhere?")
        elif commanddd in ["west", "w"] and currentplace in [61, 63]: 
            print("You stand at the edge of the riverbank, and after careful consideration, you decide that going into the river is not wise. Perhaps there is a bridge somewhere?")
        elif commanddd in ["west", "w"] and currentplace in [62]: 
            print("You stare at the water wheel... Did you just think of running into it and killing yourself?")
        elif commanddd in ["north", "n"]: 
            if currentplace%10<4: 
                currentplace+=1
                print("You walk north...")
            else: 
                print("Can't go north any further...")
        elif commanddd in ["south", "s"]: 
            if currentplace%10>1: 
                currentplace-=1
                print("You walk south...")
            else: 
                print("Can't go south any further...")
        elif commanddd in ["east", "e"]: 
            if currentplace<80: 
                currentplace+=10
                print("You walk east...")
            else: 
                print("Can't go east any further...")
        elif commanddd in ["west", "w"]: 
            if currentplace>20: 
                currentplace-=10
                print("You walk west...")
            else: 
                print("Can't go west any further...")
                
        
    if commanddd in ["look", "l"]: 
        if currentplace in [11, 12, 14, 31, 32, 34, 41, 42, 44, 73, 74, 83]: 
            print(BoldText("The Woods"))
            print("Towering trees surround you depriving any entry of light, trembling against the harsh wind, casting shadows in an engulfing abyss...")
        elif currentplace in [13]: 
            print(BoldText("A Crashed Car"))
        elif currentplace in [21, 22, 24]: 
            print(BoldText("A Narrow Road"))
        elif currentplace in [23]: 
            print(BoldText("A Narrow Blood-Stained Road"))
            print("Large pools of blood stained the rough, rocky road, dyeing the concrete scarlet red.")
        elif currentplace in [33, 43]: 
            print(BoldText("A Bloody Trail within The Woods"))
            print("A faded - but indisputable trail of blood, lay contrastingly against the now contaminated ground.")
        elif currentplace in [51, 52, 53, 61, 63]: 
            print(BoldText("The River"))
        elif currentplace in [62]: 
            print(BoldText("The Blood-Smeared Water Wheel"))
        elif currentplace in [54, 64]: 
            print(BoldText("A Fragile Bridge"))
        elif currentplace in [71, 81]: 
            print(BoldText("A Noisy Pig Pen"))
        elif currentplace in [72, 82]: 
            print(BoldText("The Cozy Farmhouse"))
        elif currentplace in [84]: 
            print(BoldText("A Half-Empty Horse Stable"))