inventorylist=["apple"]

def CommandV(): 
    check=0
    while check==0: 
        CommandInput=input("\n>")
        CommandSplit=CommandInput.split()
        FirstCmd=CommandSplit[0]
        if FirstCmd in ["look", "l", "examine", "x", "inventory", "inv", "i", "use", "u", "north", "n", "east", "e", "south", "s", "west", "w", "get"]: 
            check=1
            return CommandInput
        else: 
            print("Invalid command. Type 'help' for a list of valid commands...")

print("- - - - - - - - - - - - -")
print("........backstory")

game=0
while game==0: 
    commandinput=CommandV() 
    commanddd=commandinput.split()
    commanddd=commanddd[0]
    # commandinput = entire input from user
    # commanddd = first command / cmd category

    if commanddd in ["inventory", "inv", "i"]: 
        print(*inventorylist)
        if commanddd!=commandinput: 
            print("Everything behind "+commanddd+" is ignored...")
    
    # if commanddd in ["north", "n", "east", "e", "south", "s", "west", "w"]: 
        #
