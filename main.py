print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
    |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

input("Press any button to continue...")

way1 = int(input("You find yourself at a crossroads with 3 paths. You must choose: \n(1) Go through the dark and creepy forest; \n(2) Jump off a cliff (there's a sea below); \n(3) Walk through a city path.\nWhats is your choice? \n"))
if way1 == 1:
    print("A *dark and creepy* forest? Alright...")
    input()
    print("As you walk through this unpleasant forest, you are attacked by a wolf.")
    input()
    print("You were his dinner.")
    input()
    print("GAME OVER")
    exit()
elif way1 == 2:
    print("You decide to jump, with great momentum and excitement...")
    input()
    print("Despite the great height, you manage to sink into the water smoothly, but what scares you is the movement behind you...")
    input()
    print("You see a large great white shark swimming near you. It looks hungry.")
    shark1 = int(input("What do you do?\n(1) Flee from the shark, swimming as fast as you can;\n(2) You confront the shark, going towards it, trying to strike the hardest blow you can.\nWhat is your choice?\n"))
    if shark1 == 1:
        print("You put in your best effort, avoiding that ravenous beast as much as possible...")
        input()
        print("As expected, your movement attracts the shark, which swims toward you with a bloodthirsty look.")
        input()
        print("You are devoured in a monstrous fashion.")
        print("GAME OVER")
        exit()
    elif shark1 == 2:
        print("You muster the courage and confront the massive creature, preparing to deliver the strongest punch of your life.")
        input()
        print("Then, as you approach the shark, you realize that delivering an upward punch is not so smart...")
        input()
        print("Your last sight is a golden hue in the water and the shark's enormous mouth wide open.")
        input()
        print("GAME OVER")
        exit()
elif way1 == 3:
    city1 = int(input("You arrive at a peaceful town with a massive pink castle in front and a dark alley to your right. Knowing about the treasure,\nwill you:\n(1) Seek help from the queen of the pink castle;\n(2) Seek help from a possible dealer in the dark alley.\nWhat is your choice?\n "))
    if city1 == 1:
        print("You go to the queen to ask for help and inform her about the magnificent treasure you are seeking.")
        input()
        print("The greedy queen is intrigued by the potential magnificence of this treasure, orders her guards to capture you and go after the treasure.")
        input()
        print("You are surrounded by dozens of guards who imprison you in a cell.")
        input()
        print("You are imprisoned for 60 years, living a miserable life with no contact with humanity. You never found out what happened to the treasure.")
        input("GAME OVER")
        exit()
    elif city1 == 2:
        print("You go to the dark alley...")
        input()
        print("Eyes in the dark are watching you. You feel that you shouldn't be here.")
        input()
        print('A large figure with a black hat and two companions stops you and, with a sinister voice, says, "What are you doing here?"')
        input()
        response = int(input("You will respond about the treasure, asking for his help, with:\n (1) A firm and strong voice\n (2) An insecure and trembling voice\n"))
        if response == 2:
            print('The large man says, "Why are you groaning while speaking? AAnd what the f*** does Onii-chan mean?"')
            input()
            print("He takes a golden gun from his pocket and shoots you, finishing you off.")
            input()
            print("GAME OVER")
            exit()
        elif response == 1:
            print("Well, it seems that you are after something really interesting... Maybe I can help you.")
            input()
            print('He gives you a golden gun with one bullet and says, "Find your treasure, use this weapon to assist you. After you find it, come back here so we can share it."')
            input()
    path1 = int(input("Now, you must decide:\n(1) Go to the pink castle\n(2) Return to the starting paths\n"))
    if path1 == 1:
        print("You go to the majestic pink castle, where you find a princess on her throne.")
        input()
        print("You approach the princess asking for more help with your treasure hunt, explaining how magnificent it is.")
        print("The greedy queen is intrigued by the potential magnificence of this treasure and orders her guards to capture you and go after the treasure.")
        input()
        princess2 = int(input("You:\n(1) Accept your fate\n(2) Finish off the princess with your gun\n"))
        if princess2 == 1:
            print("You are surrounded by dozens of guards who imprison you in a cell.")
            input()
            print("You are imprisoned for 60 years, living a miserable life with no contact with humanity. You never found out what happened to the treasure.")
            input("GAME OVER")
            exit()
        elif princess2 == 2:
                print("With a quick swipe, you finish off the princess.")
                input()
                print("The guards stop.")
                input()
                print("They throw their weapons on the ground.")
                input()
                print("They bow to you and declare you the new owner of the throne.")
                input()
                print("You live a life of excellence, with all possible privileges.")
                print(
                    "However, one day, due to your poor public management and debt with the dealer, the population storms your castle.")
                input()
                print(
                    "And after all your guards are defeated by the angry mob, you find yourself facing that large man with the hat.")
                input()
                print(
                    'With a look of contempt, he aims a gun at you and says, "I thought I could trust you..."')
                print("GAME OVER")
                exit()
    elif path1 == 2:
            print("You return to the beginning.\n")
            path2 = int(input("Which path will you choose:\n(1) Dark and frightening forest\n(2) Jump off the cliff (there's a sea below)"))
            if path2 == 1:
                print("As you walk through this unpleasant forest, you are attacked by a wolf.")
                wolf = int(input("What do you do?\n(1) Accept your fate and try to be tender meat for it.\n(2) Shoot the wolf\n"))
                if wolf == 1:
                    print("The wolf seems grateful for you being such an easy prey. It makes sure to enjoy every piece of you.")
                    input()
                    print('The wolf starts to speak and says, "Since you were so kind to be my dinner, I will tell you something about that treasure..."')
                    input()
                    print('"The password to open it is 1907. Maybe in another life this information will be useful to you."')
                    input()
                    print("You are devoured with immense delicacy.")
                    print("GAME OVER")
                    exit()
                elif wolf == 2:
                    print("You make a precise shot at the wolf, which finishes it off instantly.")
                    print("After a few hours of walking in the forest, you find nothing about the treasure and decide to return to your starting point.")
                    cliff = int(input("In front of the cliff, you finally find your last chance to find the treasure. You:\n(1) Decide not to jump off the cliff\n(2) Jump off the cliff"))
                    if cliff == 1:
                        print("You finally reconsider and realize how foolish it is to search for a treasure...\n")
                        input()
                        print('Well, I hope you’re happy with this decision because you kind of ruined the experience of this "game"...')
                        input()
                        print("Your only goal was to explore enough to find out about the treasure. But that’s it, I’ll give you what you wanted.")
                        input()
                        print('The treasure? Of course not. I’ll give you an ending that isn’t "GAME OVER". I hope you’ve """enjoyed""" it.')
                        input()
                        print("BORING ENDING")
                        exit()
                    elif cliff == 2:
                        print("You decide to jump, with great momentum and excitement...")
                        print(
                            "Despite the great height, you manage to sink into the water smoothly, but what scares you is the movement behind you...")
                        input()
                        print("You see a large great white shark swimming near you. It looks hungry.\n")
                        shark1 = int(input("What do you do?\n(1) Flee from the shark, swimming as fast as you can;\n(2) You confront the shark, going towards it, trying to strike the hardest blow you can.\nWhat is your choice?"))
                        if shark1 == 1:
                            print("You put in your best effort, avoiding that ravenous beast as much as possible...")
                            input()
                            print("As expected, your movement attracts the shark, which swims toward you with a bloodthirsty look.")
                            input()
                            print("You are devoured in a monstrous fashion.")
                            print("GAME OVER")
                            exit()
                        elif shark1 == 2:
                            print("You muster the courage and confront the massive creature, preparing to deliver the strongest punch of your life.")
                            input()
                            print("Then, as you approach the shark, you realize that delivering an upward punch is not so smart...")
                            print("Your last sight is a golden hue in the water and the shark's enormous mouth wide open.")
                            input()
                            print("GAME OVER")
                            exit()
            elif path2 == 2:
                print("You decide to jump, with great momentum and excitement...")
                print("Despite the great height, you manage to sink into the water smoothly, but what scares you is the movement behind you...")
                input()
                print("You see a large great white shark swimming near you. It looks hungry.")
                input()
                shark2 = int(input("What do you do? \n(1) Try to swim as fast as possible to escape the shark\n(2) Draw your weapon and try to finish off that carnivorous beast\n"))
                if shark2 == 1:
                    print("You put in your best effort, avoiding that ravenous beast as much as possible...")
                    input()
                    print("As expected, your movement attracts the shark, which swims toward you with a bloodthirsty look.")
                    input()
                    print("You are devoured in a monstrous fashion.")
                    print("GAME OVER")
                    exit()
                elif shark2 == 2:
                    print("With your greatest agility and concentration, you draw that golden weapon.")
                    input()
                    print("And as impossible as the situation seems, the dealer's weapon appears different, it seems to be a unique pistol.")
                    input()
                    print("As soon as you aim at the shark, you quickly pull the trigger.")
                    input()
                    print("The bullet was able to overcome the resistance of the water, reaching an impressive speed, hitting the shark dead-on.")
                    input()
                    print("You managed to take down the shark, probably critically affecting the biodiversity of this place, but you succeeded.")
                    input()
                    print("Looking more closely, you notice there's a chest underwater, a chest that catches your attention.")
                    input()
                    print("You swim towards the chest, holding your breath as long as you can.")
                    input()
                    print("You realize the chest has a lock, requiring a 4-digit password.")
                    password = int(input("What numbers do you select?\n"))
                    if password != 1907:
                        print(f"As you try entering the password {password}, you hear a noise.")
                        input()
                        print("In the blink of an eye, the chest explodes with an extremely powerful blast.")
                        input()
                        print("You couldn't withstand the explosion, and you soon became a memory for your family.")
                        input()
                        print("GAME OVER")
                        exit()
                    if password == 1907:
                        print('You hear a "click", the chest opens, and your eyes are dazzled by what they see.')
                        input()
                        print("Embroidered on a cloth, you see")
                        input()
                        print("🐒")
                        input()
                        print("It's perfect, it's beautiful, it's valuable.")
                        input()
                        print("You remember that you need to share with the dealer")
                        last = int(input("What do you do?\n(1) Run away with this cloth with a monkey embroidered on it as far as possible\n(2) Go back to the dealer and share it with him\n"))
                        if last == 1:
                            print("You think carefully and decide that this is the most valuable thing in your life, and that you must live and die for it.")
                            input()
                            print("You flee, go to the farthest place possible, restart your life, and ignore everything that has happened.")
                            input()
                            print("You live happily, live until the end of your life with your cloth with a monkey embroidered on it.")
                            input()
                            print('You lived what we can call a "perfect life".')
                            input()
                            print("Happy Ending 🐒")
                            exit()
                        elif last == 2:
                            print("You return to the dark alley.")
                            input()
                            print("Again, those stares directed at you from all sides.")
                            input()
                            print("You reach the dealer and show him your great achievement.")
                            input()
                            print('He widens his eyes in amazement and says, "You did it! You really did it!"')
                            input()
                            print("He removes his human disguise and hat, revealing himself to be a monkey.")
                            input()
                            print("He draws a gun, points it at you.")
                            input()
                            print('He says, "I do not do business with humans"')
                            input()
                            print("He finishes you off, taking away your chance to enjoy that incredible piece of cloth.")
                            input()
                            print('With your last breath, you say,')
                            input()
                            print('I was a monkey too.')
                            input()
                            print("GAME OVER")
                            exit()






