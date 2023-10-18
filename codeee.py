inventorylist=["apple"]
currentplace=13 # xy = (x,y) coordinate

fleshdiscovered=0

def CommandV(): 
    check=0
    while check==0: 
        CommandInput=input("\n>")
        CommandSplit=CommandInput.split()
        if len(CommandInput)>0: 
            FirstCmd=CommandSplit[0]
            if FirstCmd in ["look", "l", "examine", "x", "inventory", "inv", "i", "use", "u", "north", "n", "east", "e", "south", "s", "west", "w", "get", "help", "h", "interact", "t"]: 
                check=1
                return CommandInput
            else: 
                print("Invalid command. Type 'help' for a list of valid commands...")
        else: 
            print("An empty void... Are you lost? \nType 'help' for a list of valid commands...")
    
    # commands left to code:
    ### use/u
    ### get?
    ### interact/e + add people in x
            
            
def BoldText(Input): 
    Input="\033[1m"+Input+"\033[0m"
    return Input
def UnderlineText(Input): 
    Input="\033[4m"+Input+"\033[0m"
    return Input

print("\n\n"+BoldText("The Murder Of James Brown"))
print("It is currently the year of 1983, and as a well-renowned chief detective of the police department, you have recently been given an unusual case to investigate on the murder of a 12 year old boy taking place in the suburbs of a farmland. You arrive at the crime scene, with hopes of finding clues and hopefully find the murderer. \n\nYou are currently at (1,3), type 'help' to check your current location or view a list of all possible commands whenever you need to...")

game=0
while game==0: 
    commandinput=CommandV() 
    commandl=commandinput.split()
    commanddd=commandl[0]
    # commandinput = entire input from user
    # commanddd = first command / cmd category
    
    
    
    
    
    if  commanddd in ["help", "h"]: 
        xCoOrd=currentplace//10
        yCoOrd=currentplace%10
        print("Your current location is ("+str(xCoOrd)+", "+str(yCoOrd)+")...")
        print("\n'north'/'n': go north \n'east'/'e': go east \n'south'/'s': go south \n'west'/'w': go west")
        print("'look'/'l': look at your surroundings \n'examine'/'x': examine an object \n''inventory'/'inv'/'i': check your inventory")
        print("'use'/'u': use an object \n'get': get an object \n'interact'/'t': interact with a character")





    if commanddd in ["inventory", "inv", "i"]: 
        print(*inventorylist,sep=", ")
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
            print("Towering "+UnderlineText("trees")+" surround you depriving any entry of light, trembling against the harsh wind, casting "+UnderlineText("shadows")+" in an engulfing abyss...")
        elif currentplace in [13]: 
            print(BoldText("A Crashed Car"))
            print("A pungent smell of burning rises from the catastrophe - a barely recognisable "+UnderlineText("car")+", jammed into the trunks of a rotting tree.")
        elif currentplace in [21, 22, 24]: 
            print(BoldText("A Narrow Road"))
            print("A pavement of concrete, striped systematically in white, stretches as far as the eye can see - twisting and turning through the trees,  eventually disappearing into the darkness of the woods.")
        elif currentplace in [23]: 
            print(BoldText("A Narrow Blood-Stained Road"))
            print("Large pools of "+UnderlineText("blood")+" stain the rough, rocky road, dyeing the concrete scarlet red.")
        elif currentplace in [33, 43]: 
            print(BoldText("A Bloody Trail within The Woods"))
            print("A faded - but indisputable "+UnderlineText("trail")+" of blood, lay contrastingly against the now contaminated ground.")
        elif currentplace in [51, 52, 53, 61, 63]: 
            print(BoldText("The River"))
            print("A flowing stream of pristine, crystal clear "+UnderlineText("water")+" flows in a smooth - perfectly linear line, segregating woods from farmland.")
        elif currentplace in [62]: 
            print(BoldText("The Blood-Smeared Water Wheel"))
            print("A circle of wood spins in an infinite cycle of clockwise motion - accompanying the river's flow, almost hypnotising to the human eye. At a closer glance, the wood appeared to be smeared with a deep, red, sticky substance, and what appeared to be chunks of torn "+UnderlineText("flesh")+".")
        elif currentplace in [54, 64]: 
            print(BoldText("A Fragile Bridge"))
            print("A pile of wooden "+UnderlineText("planks")+", clumsily nailed together, form an unstable pathway from the roadside to the farmland.")
        elif currentplace in [71, 81]: 
            print(BoldText("A Noisy Pig Pen"))
            print("The constant, never-ending noise of grunts and squeals rose from a self-built pen, encapsulating over a dozen of fat, spoiled "+UnderlineText("pigs")+", lying lethargically in the mud.")
        elif currentplace in [72, 82]: 
            print(BoldText("The Cozy Farmhouse"))
            print("Although the abode is visibly not the most luxurious nor sanitary in comparison to those in the city, its simplicity has a comfortable, pleasant air, and is unquestionably more than adequate to house the farmer's family of four.")
        elif currentplace in [84]: 
            print(BoldText("A Half-Empty Horse Stable"))
            print("A large, rectangular, wooden structure stands firmly, sheathing a diversified variety of "+UnderlineText("horses")+".")
    
    
    
    
    
    if commanddd in ["examine", "x"] and len(commandl)>1: 
        item=commandl[1]
        
        if currentplace in [11, 12, 14, 31, 32, 34, 41, 42, 44, 73, 74, 83]: 
            if item in ["trees", "shadows"]: 
                if item=="trees": 
                    print("It's just a stereotypical tall tree, green leaves and all.")
                elif item=="shadows": 
                    print("Raven-black figures cover the floor...")
            else: 
                print("Object not found...")
                
        elif currentplace in [13]: 
            if item in ["car"]: 
                print("A Toyota AE86, nothing out of the ordinary, just the regular, four wheel drive, you could spot anywhere on the road.")
            else: 
                print("Object not found...")
                
        elif currentplace in [23]: 
            if item in ["blood"]: 
                print("The easily distinguishable velvety-red of thick liquid, a symbol of injury and death.")
            else: 
                print("Object not found...")
            
        elif currentplace in [33, 43]: 
            if item in ["trail"]: 
                print("The droplets of blood form what seemed to be a continuous pathway - a trail, leading to someplace unknown.")
            else: 
                print("Object not found...")
                
        elif currentplace in [51, 52, 53, 61, 63]: 
            if item in ["water"]: 
                print("Unlike water sources back in the city, the water here is pure and refreshing, pure enough to be drunk straight from the river, as if it had been filtered since the start. You get a quiack glimpse of your reflection.")
            else: 
                print("Object not found...")
        
        elif currentplace in [54, 64]: 
            if item in ["planks"]: 
                print("Rectangular pieces of wood, likely to have been chopped and shaped from trees surrounding the land.")
            else: 
                print("Object not found...")

        elif currentplace in [62]: 
            if item in ["flesh"]: 
                print("Stripped pieces of meat rotting away, producing an abominable smell of the dead, attracting a swarm of hungry flies.")
                if fleshdiscovered==0: 
                    print("\nIt must have been a dark night and chilly night, except darker than most and colder. The night held reign upon the world, watching - in its full, white roundness. The trees sway against the wind, imitating the living, feeding the eerie atmosphere. James Brown stood at the tip of the river, voice course from screaming, blood dripping down from the wounds he gained from the accident that just occurred. Looking into the abyssal woods with little to no light to support his vision, a silhouette of a person could be barely made out in the distance. Before he could comprehend the situation, he was pushed into the ravenous river. Being a farm boy all his life, no one had taught him to swim and so struggling to keep afloat, all he could do was to get carried away by the current. And down he went, until he was plunged into a wooden, circular structure, and left to be torn apart inescapably...")
                    print("\nSpeculation has been added to inventory.")
                    fleshdiscovered=1
                    inventorylist.append("speculation")
            else: 
                print("Object not found...")
        
        elif currentplace in [71, 81]: 
            if item in ["pigs"]: 
                print("Oink oink. OINK.")
            else: 
                print("Object not found...")
                
        elif currentplace in [84]: 
            if item in ["horses"]: 
                print("Large, muscular, creatures stood, head held high and peaking over the fence - in anticipation for grazing time.")
            else: 
                print("Object not found...")
                
        else: 
            print("Nothing to examine here.")
            
    elif commanddd in ["examine", "x"] and len(commandl)<2:
        print("No object was given...")
        
    
    
    
    
    if commanddd in ["use", "u"] and len(commandl)>1: 
        item=commandl[1]
        if item in inventorylist: 
            if item=="apple": 
                print("You take a bite into the scrumptious apple, and then place it back into your bag.")
            elif item=="speculation": 
                print("It must have been a dark night and chilly night, except darker than most and colder. The night held reign upon the world, watching - in its full, white roundness. The trees sway against the wind, imitating the living, feeding the eerie atmosphere. James Brown stood at the tip of the river, voice course from screaming, blood dripping down from the wounds he gained from the accident that just occurred. Looking into the abyssal woods with little to no light to support his vision, a silhouette of a person could be barely made out in the distance. Before he could comprehend the situation, he was pushed into the ravenous river. Being a farm boy all his life, no one had taught him to swim and so struggling to keep afloat, all he could do was to get carried away by the current. And down he went, until he was plunged into a wooden, circular structure, and left to be torn apart inescapably...")
        else: 
            print("Object is not in inventory...")
    elif commanddd in ["use", "u"] and len(commandl)<2: 
        print("No object was given...")
        



print("\nBrought to you by Ru Ying, Camelia and Dora...")