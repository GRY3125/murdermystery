evidencechecked=[] 
noofevidence=0
suscmd=0

inventorylist=["apple", "autopsy report"]
currentplace=13 # xy = (x,y) coordinate

fleshdiscovered=0
allevidencediscovered=0 

def CommandV(): 
    check=0
    while check==0: 
        CommandInput=input("\n>")
        CommandSplit=CommandInput.split()
        if len(CommandInput)>0: 
            FirstCmd=CommandSplit[0]
            if FirstCmd in ["look", "l", "examine", "x", "inventory", "inv", "i", "use", "u", "north", "n", "east", "e", "south", "s", "west", "w", "help", "h", "interact", "t", "suspect"]: 
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
def CyanText(Input): 
    Input="\033[96m"+Input+"\033[0m"
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
        print("\n'north'/'n': go north \n'east'/'e': go east \n'south'/'s': go south \n'west'/'w': go west \n'look'/'l': look at your surroundings \n'examine'/'x': examine an object \n'inventory'/'inv'/'i': check your inventory \n'use'/'u': use an object \n'interact'/'t': interact with a character")





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
        elif commanddd in ["south", "s"] and currentplace in [54, 64]: 
            print("You look downwards at the river flowing under the bridge. Maybe jumping in is not a good idea.")
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
            print("A pungent smell of burning rises from the catastrophe - a barely recognisable "+UnderlineText("car")+", jammed into the trunks of a rotting tree. There is a "+CyanText("driver")+" nearby.")
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
            print("Although the abode is visibly not the most luxurious nor sanitary in comparison to those in the city, its simplicity has a comfortable, pleasant air, and is unquestionably more than adequate to house the farmer's family of four. There is a table with a cheap antique "+UnderlineText("telephone")+" sitting on it. Underneath it, you can see a yellowed, wrinkled piece of "+UnderlineText("paper")+", with fading words gently written across it.")
            print("The "+CyanText("farmer")+" stands awkwardly by the door, while his "+CyanText("wife")+" leans on the wall by the stairs.")
        elif currentplace in [84]: 
            print(BoldText("A Half-Empty Horse Stable"))
            print("A large, rectangular, wooden structure stands firmly, sheathing a diversified variety of "+UnderlineText("horses")+". There is a "+CyanText("stableboy")+" at a corner of the stable.")
        if currentplace in [74]: 
            print("There is a little "+CyanText("kid")+" sobbing in a corner.")
    
    
    
    
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
                print("Right on the front hood of the car, there was a rather unusual smear of blood. It seemed improbable that it was Bobbylee's blood, but the presence of this mysterious stain left you wondering whether it had any link to the blood on the ground.")
                if "xcar" not in evidencechecked: 
                    evidencechecked.append("xcar")
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
                print("Unlike water sources back in the city, the water here is pure and refreshing, pure enough to be drunk straight from the river, as if it had been filtered since the start. You get a quick glimpse of your reflection.")
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
                if "speculation" not in inventorylist: 
                    print("\nIt must have been a dark night and chilly night, except darker than most and colder. The night held reign upon the world, watching - in its full, white roundness. The trees sway against the wind, imitating the living, feeding the eerie atmosphere. James Brown stood at the tip of the river, voice course from screaming, blood dripping down from the wounds he gained from the accident that just occurred. Looking into the abyssal woods with little to no light to support his vision, a silhouette of a person could be barely made out in the distance. Before he could comprehend the situation, he was pushed into the ravenous river. Being a farm boy all his life, no one had taught him to swim and so struggling to keep afloat, all he could do was to get carried away by the current. And down he went, until he was plunged into a wooden, circular structure, and left to be torn apart inescapably...")
                    print("\nSpeculation has been added to inventory.")
                    inventorylist.append("speculation")
                if "xflesh" not in evidencechecked: 
                    evidencechecked.append("xflesh")
            else: 
                print("Object not found...")
        
        elif currentplace in [71, 81]: 
            if item in ["pigs"]: 
                print("Oink oink. OINK.")
                if "xpigs" not in evidencechecked: 
                    evidencechecked.append("xpigs") 
            else: 
                print("Object not found...")
                
        elif currentplace in [72, 82]: 
            if item in ["telephone", "paper"]: 
                if item=="telephone": 
                    if "call record" not in inventorylist: 
                        print("You examine the telephone and find some call logs from this morning. It has been added into your inventory.")
                        inventorylist.append("call record")
                    else: 
                        print("You examine the telephone again, and then realise you already have the call logs in your inventory.")
                    if "xtelephone" not in evidencechecked: 
                        evidencechecked.append("xtelephone")
                if item=="paper": 
                    if "paper" not in inventorylist: 
                        print("Through careful inspection, you realise that one of the pages is a diary entry. It has been added into your inventory.")
                        inventorylist.append("paper")
                    else: 
                        print("Blank pages.")
                    if "xpaper" not in evidencechecked: 
                        evidencechecked.append("xpaper")
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
        
        
        
        
        
    if commanddd in ["interact", "t"] and len(commandl)>1: 
        person=commandl[1]
        
        if currentplace in [13]: 
            if person in ["driver"]: 
                print("Bobbylee Jones was discovered leaning against a gnarled tree in a barely recognizable wreck of a car. His face was ruined by a dreadful wound that left visible evidence of the peril he had been in. Blood flowed from his forehead, staining his once-white shirt a deep crimson, and mirroring the horror of the scene. Fortunately, he made it through and awoke till the police rescued him right away. \nWith a keen eye, you noticed something peculiar about Bobbylee's clothing. His shoes and trousers were full of mud, an anomaly considering that there was no reasonable explanation for mud stains unless he had recently traversed soil or a similarly muddy surface. ")
                print("\nPress enter to continue the dialogue. \n")
                dialogueyn=input()
                if dialogueyn=="": 
                    dialogueee=1
                else: 
                    dialogueee=0
                dialoguenumber=0
                dialoguelist=["What is your full name? \n>>> Bobbylee Jones", 
                              "What is your occupation? \n>>> College student", 
                              "Can you provide details about your activities on the night of the crime? \n>>> I was driving on the road as usual, but a little boy suddenly rushed out from the woods. It's unbelievable, really, how some parents can't be bothered to keep an eye on their children, even letting them run on a highway! \n>>> I swerved my car to avoid hitting the child, but it ended up colliding with a tree. The sound of the impact... it's something I won't forget. Oh, my new car... I've just bought it for 1 week, and with my own pocket money! \n>>> Anyways, I tried to get help; however, the pain in my head was getting unbearable, and all I could think of was that I might not make it out of this ordeal alive.", 
                              "What is your reason for driving on this road? \n>>> I was simply on my way back from college; it's part of my weekly routine.", 
                              "When do you crash the car? \n>>> It's in the evening, I guess it's around 10 o'clock.", 
                              "What is the last time you saw the boy? \n>>> On the road before the car crash... after that, all I could see was the tree I had crashed into, and smoke rising from my car's trunk.", 
                              "Can you describe the boy? \n>>> I couldn't see him really clearly due to there not being any street lamps around here, but he definitely was no adult judging from his small size... \nBobbylee scratched his head. \n>>> and if I'm not mistaken he was wearing a black shirt.", 
                              "Did you hurt the boy? \n>>> No... I don't think so... my car and I got hurt instead :(", 
                              "Did you see anyone else other than the boy? \n>>> Nope"]
                while dialogueee==1 and dialoguenumber<len(dialoguelist): 
                    print(dialoguelist[dialoguenumber])
                    dialogueyn=input()
                    if dialogueyn=="": 
                        dialoguenumber+=1
                    else: 
                        dialogueee=0
                        print("Dialogue ended.")
                if "sbb" not in evidencechecked: 
                    evidencechecked.append("sbb")
            else: 
                print("Person not found...")
                
        elif currentplace in [72, 82]: 
            if person in ["wife", "farmer"]: 
                if person=="wife": 
                    print("She stood at the staircase,  anxiously waited for the police to come. Her swollen, reddened eyes showed the tears that had flowed. her trembling hand shook uncontrollably, fingers interlocked in a tight and desperate grip, as if they were seeking solace and strength from one another.")
                    print("Press enter to continue the dialogue. \n")
                    dialogueyn=input()
                    if dialogueyn=="": 
                        dialogueee=1
                    else: 
                        dialogueee=0
                    dialoguenumber=0
                    dialoguelist=["What is your full name? \n>>> Bar...bara Will...liam Bene...dict", 
                                  "What is your occupation? \n>>> I'm the... wife of the farmer... who owns this land...", 
                                  "Can you provide details about your activities and what happened? \n>>> As usual, I woke up early in the morning to wash the entire family's clothes... by the river... However, I found out that the waterwheel was not spinning as usual... Then I noticed the... \nShe inhales deeply and exhales wobbly. \n>>> body pieces... of my dear boy... stuck in the wheel. Blood splashed up the wheel. I wasted no time; and I immediately called the police. \n>>> Oh, I remember hearing a loud noise... akin to a scream, before I went to sleep... At the time, I dismissed it because I believed it was the pigs' cry... I regret not checking on James... \n>>> James was afraid of water, and it's impossible for him to go near the water... It cannot be an accident for him to slip into the wheel! It's glaringly apparent that someone malevolently took his life! It's a gruesome murder!!!"
                                  "Did you go out after you heard the scream? \n>>> No, I stayed with Luke all night... He was afraid to be alone in the house.",
                                  "When did you hear the noise/scream? \n>>> Approximately 10:30pm I think...", 
                                  "Did you see anyone near the wheel this morning? \n>>> No", 
                                  "Is that boy your son? \n>>> Yes, he is our son... I can't bear to hear the news of his... death...", 
                                  "How is your relationship with the boy? \n>>> We have a good relationship... it's truly puzzling why anyone would harbour ill will towards such a sweet and gentle child...", 
                                  "Was Bobylee ever inclined to commit suicide? \n>>> No, never! How would that lively boy ever wish for his own demise."]
                    while dialogueee==1 and dialoguenumber<len(dialoguelist): 
                        print(dialoguelist[dialoguenumber])
                        dialogueyn=input()
                        if dialogueyn=="": 
                            dialoguenumber+=1
                        else: 
                            dialogueee=0
                            print("Dialogue ended.")
                    if "sw" not in evidencechecked: 
                        evidencechecked.append("sw")
                if person=="farmer":
                    print("After two hours of the police starting their investigation into the murder, Hubert finally arrived at the scene with a sense of happiness and enjoyment. As he took in the grim reality before him, shock and disbelief washed over his joy, making him speechless. His wrinkled face looked increasingly old.")
                    print("Press enter to continue the dialogue. \n")
                    dialogueyn=input()
                    if dialogueyn=="": 
                        dialogueee=1
                    else: 
                        dialogueee=0
                    dialoguenumber=0
                    dialoguelist=["What is your full name? \n>>> Hubert James Benedict", 
                                  "What is your occupation? \n>>> Farmer, the owner of this farmland", 
                                  "Can you provide details about your activities yesterday? \n>>> I headed into the city yesterday to sell the corn at the street market since we harvested the wheat for this autumn. It's been the most profitable season I've ever experienced. BUT, but.. James cannot enjoy it... \n>>> The farm is quite far from the city, making it a half-day round trip. So, I thought it best to stay at a small hotel near the market.", 
                                  "When did you leave the farm? \n>>> Yesterday morning, about 6 o'clock", 
                                  "What is your relationship with the boy? \n>>> He is my son, we adopted this young fellow when we found him being abandoned near our farm. His life has been filled with hardship and tragedy, poor boy.", 
                                  "How is your relationship with the boy? \n>>> Of course we have a good relationship! James is a part of our family. We've always treated James with kindness, offering him a warm and welcoming home. James is also helpful with farm work, he is so favourable."]
                    while dialogueee==1 and dialoguenumber<len(dialoguelist): 
                        print(dialoguelist[dialoguenumber])
                        dialogueyn=input()
                        if dialogueyn=="": 
                            dialoguenumber+=1
                        else: 
                            dialogueee=0
                            print("Dialogue ended.")
                    if "sf" not in evidencechecked: 
                        evidencechecked.append("sf")
            else: 
                print("Person not found...")
                
        elif currentplace in [84]: 
            if person in ["stableboy"]: 
                print("Logan had just woken up after the police arrived. As they shared the sad news of James' death, Logan was stricken with a profound sense of disbelief as if the world had shifted beneath him. His eyes welled up as he grappled with the heavy reality of losing his dear friend. \nLogan walked straight to the innermost of the stable, where an attractive horse stood. He claimed that this was the horse who was James' favourite, and accompanied him throughout his life. In a quiet tone, Logan shared the tragic news with the horse.")
                print("Press enter to continue the dialogue. \n")
                dialogueyn=input()
                if dialogueyn=="": 
                    dialogueee=1
                else: 
                    dialogueee=0
                dialoguenumber=0
                dialoguelist=["What is your full name? \n>>> Logan Alexander", 
                              "What is your occupation? \n>>> I work for the stable.", 
                              "Can you provide details about your activities yesterday? \n>>> Last night, I went to bed as usual after I visited my horses for the last time. \n>>> But later in the night, I suddenly woke up because I was thirsty, so I went to collect some fresh water along the river. But the water tasted a little abnormal, as if there was a pinch of iron?", 
                              "When do you go to bed? \n>>> Around 9:00 pm", 
                              "When do you go to collect the water? \n>>> I didn't check the clock, but it's probably about 10-11pm because the stars were not visible.", 
                              "Did you see anyone when you went out? \n>>> No, I don't think so.", 
                              "Did you hear any noise last night? \n>>> Noise? What noise? Not really, I'm a deep sleeper.", 
                              "What is your relationship with the boy? \n>>> Of course, we are close friends with each other! I treated him as my little brother. James is such a kind soul, and he willingly helped me with the tough tasks in the stable. \n>>> I'm so so sorry to hear about his... death. \nTears start to well up in Logan's eyes. \n>>> It must have been because of his family, you know... you know how they treated James every day? It's just inhumane. They gave all of their love to their own kid."]
                while dialogueee==1 and dialoguenumber<len(dialoguelist): 
                    print(dialoguelist[dialoguenumber])
                    dialogueyn=input()
                    if dialogueyn=="": 
                        dialoguenumber+=1
                    else: 
                        dialogueee=0
                        print("Dialogue ended.")
                if "ssb" not in evidencechecked: 
                    evidencechecked.append("ssb")
            else: 
                print("Person not found...")
                
        elif currentplace in [74]: 
            if person in ["kid"]: 
                print("The little boy is curled up into a ball on the ground, his face burried in his body while he hugs his trembling legs.")
                print(">>> I don't know what happened!! There was a loud shout at night. Mama said she should check what happened. I said no. I was scared to be alone. And mama said someone died this morning. I've been hiding here since. Don't tell mama.")
                print("He gets up and scurries off, but your guts tell you that he will return to this spot as he has no where else to go.")
                if "sk" not in evidencechecked: 
                    evidencechecked.append("sk")
        else: 
            print("No one to talk to here.")
            
    elif commanddd in ["interact", "t"] and len(commandl)<2:
        print("No person was named...")
        
    
    
    
    
    if commanddd in ["use", "u"] and len(commandl)>1: 
        item=commandl[1:]
        itemmm=""
        for x in range(len(item)): 
            itemmm=itemmm+" "+str(item[x])
        itemmm=itemmm[1:]
        if itemmm in inventorylist: 
            if itemmm=="apple": 
                print("You take a bite into the scrumptious apple, and then place it back into your bag.")
            elif itemmm=="speculation": 
                print("It must have been a dark night and chilly night, except darker than most and colder. The night held reign upon the world, watching - in its full, white roundness. The trees sway against the wind, imitating the living, feeding the eerie atmosphere. James Brown stood at the tip of the river, voice course from screaming, blood dripping down from the wounds he gained from the accident that just occurred. Looking into the abyssal woods with little to no light to support his vision, a silhouette of a person could be barely made out in the distance. Before he could comprehend the situation, he was pushed into the ravenous river. Being a farm boy all his life, no one had taught him to swim and so struggling to keep afloat, all he could do was to get carried away by the current. And down he went, until he was plunged into a wooden, circular structure, and left to be torn apart inescapably...")
            elif itemmm=="autopsy report": 
                print("\n"+BoldText("AUTOPSY REPORT"))
                print(BoldText("Name: ")+"James Brown")
                print(BoldText("Case Number: ")+"[198308031]")
                print(BoldText("Date of Autopsy: ")+"[1983.08.03]")
                print(BoldText("Identification: ")+"\nClothing - black shirt, jeans")
                print(BoldText("Time of Death: ")+"\nAround 10pm, 1983.08.02")
                print(BoldText("Cause of Death: ")+"\n1. Immediate Cause: excessive loss of blood and concussion \n2. Underlying Causes: cerebral concussion, fracture, organ failure \n3. Manner of Death: [Undetermined]")
            elif itemmm=="call record": 
                print("\n"+BoldText("TELEPHONE CALL RECORD"))
                print(BoldText("Date: ")+"[1983.08.03]")
                print(BoldText("Time: ")+"[6:15am]")
                print(BoldText("Caller's Name: ")+"[Barbara William Benedict]")
                print(BoldText("Receiver's Name: ")+"[Hubert James Benedict]")
                print(BoldText("Call Duration: ")+"[3min48s]")
                print(BoldText("Notes:"))
                print("Barbara: Hubert! Oh dear... It's James! He... He's gone. I saw him, I saw him die!")
                print("Hubert: James? No, it can't be...")
                print("Barbara: James, the boy we adopted, he's gone, Hubert. Smashed by that waterwheel piece by piece.")
                print("Hubert: Oh God... I... I need to go back and check on this, Barbara.")
                print("Barbara: Don't rush, Hubert. As you know, be careful not to get involved in this tragedy too.")
                print("Hubert: We won't have to prepare one more dish for dinner anymore. Ha! We are finally free from looking after that naughty boy!")
            elif itemmm=="paper":
                print('\nDear dary,')
                print("\nIm so sO so sad today. I did what daddy wantid, even betterer! 3 'ole miles of land under the supper supper hot sun. But, mommy an' daddy di-en' gimme dinner 'gain… This es the sec'nd day ! Y???!!! Im supper-duper hungry.")
                print("They say Im not theyre real kid, and they got Luke now. They lov Luke more, I gess. It hurts, dary. I wish I cud have a hug, like they give theyre own kid.")
                print("\nJames")
        else: 
            print("Object is not in inventory...")
            print(itemmm)
    elif commanddd in ["use", "u"] and len(commandl)<2: 
        print("No object was given...")
        
        
    
    
    
    if commanddd in ["suspect"] and len(commandl)>1 and allevidencediscovered==1: 
        if commandinput in ["suspect 1", "suspect 2", "suspect 3", "suspect 4"]: 
            game=1
        else: 
            print("Invalid suspect. Please type 'suspect x', where x is a number from 1 to 4.")
            print("\n1: Logan Alexander \n2: Bobbylee Jones \n3: Hubert James Benedict \n4: Barbara William Benedict")
    elif commanddd in ["suspect"] and len(commandl)<2 and allevidencediscovered==1: 
        print("No suspect given.")
    elif commanddd in ["suspect"] and allevidencediscovered==0:
        print("You have to examine every single object and obtain every single piece of evidence before finalising a suspect. You should've known that, aren't you a detective?")
        
    
    
    
    
    
    
    
    
    noofevidence=len(evidencechecked)
    if noofevidence==10: 
        allevidencediscovered=1
        if suscmd==0: 
            print("\n\n\n[ANNOUNCEMENT!!!] \nAll clues and evidence have been viewed at or collected. \nYou may now use the command 'suspect'.")
            suscmd=1
        
        

if commandinput=="suspect 2": 
    print("\nReturning back from the crime scene, you receive a call from the police station that the suspect has been brought in, and you must be present to conduct further interrogation. You ask questions and collect further information on the events, and use certain techniques to intimidate the suspect into confessing. After a few hours of going back and forth, you realise that the suspect starts to get increasingly nervous - constantly tapping on the table, scratching behind his ear, and providing more mismatched information. Until finally, he confesses...")
    print("\nBobbylee Jones : Fine, I'm the one who did it! But believe me, it really was an accident. The road was dark and I could barely see anything, and there this kid came running onto the road. What do you expect me to do! I can't just magically fly over him and so yea, I ended up running into him okay! But guess what, he was still alive, and I admit I did see him get up and run over the river but I swear after that it had nothing to do with me! It really was all an accident, I didn't murder him!")
    print("\nAfter a year, Bobbylee Jones was sentenced to life in prison for the murder of 12 year boy, James Brown. It was later found out that Bobbylee had pushed James into the river - after finding he was still alive following the car crash - with the intention of drowning him.")
else: 
    print("\nReturning back from the crime scene, you receive a call from the police station that the suspect has been brought in, and you must be present to conduct further interrogation. You ask questions and collect further information on the events, and use certain techniques to intimidate the suspect into confessing. After a few hours of going back and forth, you realise that the suspect has no intentions of confessing, staying firm on innocence. You can only hold the suspect for interrogation up to 24 hours, and therefore is forced to let him go with no substantial statements received. A court trial was then conducted, but with the little amount of solid evidence collected, the case was lost and the suspect was proved innocent. With the murderer still on the loose, you have failed your job as a detective...")
    print("\nTwo decades later, you sat comfortably on the soft couch in drowsy fashion, with the sun spilling through the windows, and the air conditioner buzzing away, you decide to turn on the news. On the screen was a middle aged, oddly familiar man in handcuffs, being shoved roughly into a cop car.")
    print("\nNews reporter: Good morning everyone, I am glad to inform you that the murderer responsible for the string of killings of children for the past 20 decades, has been caught. 40 year old Bobbylee Jone has confessed to be responsible for the infamous case of the murder of 12 year old boy James Brown, as well as many more. Although the murder of James Brown was an accident, he soon became accustomed to killing and started murdering intentionally for his own pleasure. We will be providing more information in the evening news, but for now a 30 minute break will commence. Thank you for watching CCB news, and make sure to stay safe.")




print("\nBrought to you by Ru Ying, Camelia and Dora... <3")