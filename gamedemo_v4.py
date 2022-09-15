import random

def main():
    title()
    while True:
        print("\nGreetings, traveller. What is your name?")
        # Get player name
        while True:
            try:
                name = input("Name: ")
            except ValueError:
                print("Sorry, I didn't get that.")
                continue
            else:
                break

        # Select type of questions
        print("\nWelcome, " + name + "! What kind of adventure do you seek?\n")
        problemType = get_problemType()

        # Select difficulty for HP and end bonus (TODO - endless mode? stronger monsters?)
        print("\nWhat difficulty setting do you want?\n")
        difficulty = get_difficulty()
        playerHP = get_playerHP(difficulty)
        
        print("\nYou enter a mysterious dungeon searching for challenges and treasures. Be on your guard!\n")
        print("HOW TO PLAY: Balance the equation to attack and defend.")
        print("Deal bonus damage by correctly solving all 3 equations on your turn.")
        print("Regain a little HP by correctly solving all 3 equations on your opponent's turn.\n")
        input("Press Enter to continue...")
        # Flag for active game:
        gameover = 0
        # Upper limit for questions per level
        cap = 10
        # Track right answers
        correctTotal = 0
        # Track number of questions
        questionTotal = 0
        # TODO - Track best streak
        streak = 0
        bestStreak= 0 
        # Determine attack bonus and get next monster from index
        playerLevel = 0
        # Gameplay loop while player has HP and not at max level
        while playerHP > 0 and playerLevel < 10: 
            monster = get_monster(playerLevel)
            monsterHP = int(monster["hp"])
            print("An angry ", monster["name"], " approaches!\n")
            # while playerHP > 0 and monsterHP > 0:
            while monsterHP > 0:
                if playerHP > 0:
                    battlestatus(name, playerHP, monster["name"], monsterHP)
                    # Attack phase quiz
                    print(name, "'s turn to attack.\n")
                    if problemType == 1 or problemType == 2:
                        correctAnswers = addsubtractQuiz(cap, problemType, streak, bestStreak)
                    elif problemType == 3 or problemType == 4:
                        correctAnswers = multiplydivideQuiz(cap, problemType, streak, bestStreak)
                    correctTotal += correctAnswers[0]
                    streak = correctAnswers[1]
                    bestStreak = correctAnswers[2]
                    questionTotal += 3
                    # Bonus for perfect answer - TODO add ascii art  
                    if correctAnswers[0] == 3:
                        crit()
                        playerDamage = correctAnswers[0] + playerLevel
                    else:
                        playerDamage = correctAnswers[0]
                    print("You deal ", playerDamage, " damage!\n")
                    monsterHP -= playerDamage
                else:
                    print("You are force to retreat...\n")
                    gameover = 1
                    break
                
                # Defense phase quiz
                if monsterHP > 1:
                    # print(name, "HP: ", playerHP, " | ", monster["name"], "HP: ", monsterHP)
                    battlestatus(name, playerHP, monster["name"], monsterHP)
                    print(monster["name"], " prepares to ", monster["attack"], "!\n")
                    if problemType == 1 or problemType == 2:
                        correctAnswers = addsubtractQuiz(cap, problemType - 2, streak, bestStreak)
                    elif problemType == 3 or problemType == 4:
                        correctAnswers = multiplydivideQuiz(cap, problemType - 2, streak, bestStreak)
                    correctTotal += correctAnswers[0]
                    streak = correctAnswers[1]
                    bestStreak = correctAnswers[2]
                    questionTotal += 3
                    monsterDamage = 3 - correctAnswers[0]
                    if monsterDamage == 0:
                        perfect()
                        print("You gain 1 HP!\n")
                        playerHP += 1
                    else:
                        print(monster["name"], " deals ", monsterDamage, " damage!\n")
                        playerHP -= monsterDamage
                # Produce results of battle
                else:
                    print(monster["name"], " defeated!\n")
                    playerLevel += 1
                    cap += 10
                    print(name, "rises to Level ", playerLevel, "\n")
                    input("Press Enter to continue...")
                    print("You walk further into the dungeon. You turn a corner and...\n")            
                    break
                    

        # End game / Final results
        if gameover == 0:
            print("Find a trove of fabulous treasures!")
            if difficulty == 1:
                print("It looks like 100 gold. Maybe a harder challenge will have a bigger reward...\n")
            elif difficulty == 2:
                print("It looks like 500 gold. Not bad, but maybe there's more in a harder dungeon...\n")
            else:
                print("I looks like 1000 gold! This is a reward for a true adventurer!\n")
        else:
            gameoverscreen()
            print("You failed, but you can always try again...\n")
        # TODO - give score, difficulty bonus, best streak   
        print("***FINAL RESULTS***")  
        print(correctTotal, " out of ", questionTotal, "correct!\n")  
        print("x best streak ", bestStreak)
        if gameover == 0:
            print("Difficulty complete bonus: " )
            if difficulty == 1:
                bonus = 100
            elif difficulty == 2:
                bonus = 500
            else:
                bonus = 1000
            print("+", bonus)
        else:
            bonus = 0
        print("\nFinal Score: ", correctTotal * bestStreak + bonus)
        print("*******************\n")
        # Ask user to play again 
        print("Play again? ")
        while True:
            try:
                print("1 - New Game")
                print("2 - Quit")
                newGame = int(input("Select 1 or 2: "))
            except ValueError:
                print("Please enter a number.\n")
                continue
            if not 0 < newGame < 3:
                print("Select 1 or 2.\n")
                continue
            else:
                break
        if newGame == 1:
            continue
        else: 
            print("See you next time!")
            return


def get_problemType():
    while True:
        try:
            print("1 - Addition")
            print("2 - Subtraction")
            print("3 - Multiplication")
            print("4 - Division")
            type = int(input("Select 1-4: "))
        except ValueError:
            print("Please enter a number.\n")
            continue
        if  type < 1 or type > 4:
            print("Invalid answer\n")
            continue
        else:
            break
    return type


def get_difficulty():
    while True:
        try:
            print("1 - Easy (15 HP)")
            print("2 - Medium (10 HP)")
            print("3 - Hard (5 HP)")
            difficulty = int(input("Select 1-3: "))
        except ValueError:
            print("Please enter a number.\n")
            continue
        if difficulty < 1 or difficulty > 3:
            print("Number must be between 1 and 3.\n")
            continue
        else:
            break
    return difficulty


def get_playerHP(difficulty):
    if difficulty == 1:
        playerHP = 15
    elif difficulty == 2:
        playerHP = 10
    else:
        playerHP = 5
    return playerHP


def battlestatus(name, playerHP, monstername, monsterHP):
    print("***STATUS***")
    print(name, "HP: ", playerHP, " | ", monstername, "HP: ", monsterHP, "\n")
    return

def answerValidator():
    while True:
        try:
            answer = int(input("Answer: "))
        except ValueError:
            print("Integers only!")
            continue 
        else:
            break
    return answer    


def addsubtractQuiz(cap, type, streak, bestStreak):
    correctCounter = 0
    i = 3
    while i > 0:
        z = random.randint(cap-10, cap)
        x = z - random.randint(0,z)
        y = z - x
        # Addition attack, solve for z
        if type == 1:
            print(x, " + ", y, " = __")
        # Subtraction attack, solve for y   
        elif type == 2:
            print(z, " - ", x, " = __")
        # Addition defense, solve for y
        elif type == -1:
            print(x, " + __ = ", z)
        # Subtraction defense, solve for y
        elif type == 0:
            print(z, " - __ = ", x)   
        answer = answerValidator()
        if (type == 1 and int(answer) == z) or ((type == 2 or type == -1 or type == 0) and  int(answer) == y):
            print("Correct!\n")
            correctCounter += 1
            streak += 1
            bestStreak = streakUpdate(streak, bestStreak)
        else:
            print("Miss!\n")
            streak = 0
        i -= 1
    return correctCounter, streak, bestStreak


def multiplydivideQuiz(cap, type, streak, bestStreak):
    correctCounter = 0
    i = 3
    while i > 0:
        x = random.randint(1, cap / 10)
        y = random.randint(1,10)
        z = x * y  
        # Multiplication attack, solve for z
        if type == 3:
            print(x, " x ", y, " = __")
        # Division attack, solve for y   
        elif type == 4:
            print(z, " % ", x, " = __")
        # Multiplication defense, solve for y
        elif type == 1:
            print(x, " x __ = ", z)
        # Division defense, solve for y
        elif type == 2:
            print(z, " % __ = ", x)   
        answer = answerValidator() 
        if (type == 3 and int(answer) == z) or ((type == 4 or type == 1 or type == 2) and  int(answer) == y):
            print("Correct!\n")
            correctCounter += 1
            streak += 1
            bestStreak = streakUpdate(streak, bestStreak)
        else:
            print("Miss!\n")
            streak = 0
        i -= 1
    return correctCounter, streak, bestStreak


def streakUpdate(streak, bestStreak):
    if streak > bestStreak:
        bestStreak = streak
    return bestStreak


def get_monster(playerLevel):
    monsters = [
        {"name": "Giant Rat", "attack" : "bite", "hp" : "5"},
        {"name": "Slime", "attack" : "bounce", "hp" : "10"},
        {"name": "Mimic", "attack" : "chomp", "hp" : "15"},
        {"name": "Skeleton", "attack" : "swing its sword", "hp" : "20"},
        {"name": "Goblin", "attack" : "shoot an arrow", "hp" : "25"},
        {"name": "Mummy", "attack" : "take a swipe", "hp" : "30"},
        {"name": "Automaton", "attack" : "electrify itself", "hp" : "35"},
        {"name": "Troll", "attack" : "swing its club", "hp" : "40"},
        {"name": "Lich", "attack" : "cast a spell", "hp" : "45"},
        {"name": "Dragon", "attack" : "breathe fire", "hp" : "50"},
    ]
    encounter = monsters[playerLevel]
    return encounter


def title():
    print("\n")
    print("d8888b. d888888b  d888b  d888888b d888888b                  ")
    print("88  `8D   `88'   88' Y8b   `88'   `~~88~~'                  ")
    print("88   88    88    88         88       88                     ")
    print("88   88    88    88  ooo    88       88                     ")
    print("88  .8D   .88.   88. ~8~   .88.      88                     ")
    print("Y8888D' Y888888P  Y888P  Y888888P    YP                     ")
    print("\n")                                                           
    print("d8888b. db    db d8b   db  d888b  d88888b  .d88b.  d8b   db ")
    print("88  `8D 88    88 888o  88 88' Y8b 88'     .8P  Y8. 888o  88 ")
    print("88   88 88    88 88V8o 88 88      88ooooo 88    88 88V8o 88 ")
    print("88   88 88    88 88 V8o88 88  ooo 88~~~~~ 88    88 88 V8o88 ")
    print("88  .8D 88b  d88 88  V888 88. ~8~ 88.     `8b  d8' 88  V888 ")
    print("Y8888D' ~Y8888P' VP   V8P  Y888P  Y88888P  `Y88P'  VP   V8P ") 
    print("\nFinal Project for Harvard's CS50x") 
    print("© Jake Browning, 2022")
    return


def perfect():
    print("     ____            ____          __  __")
    print("    / __ \___  _____/ __/__  _____/ /_/ /")
    print("   / /_/ / _ \/ ___/ /_/ _ \/ ___/ __/ / ")
    print("  / ____/  __/ /  / __/  __/ /__/ /_/_/  ")
    print(" /_/    \___/_/  /_/  \___/\___/\__(_)   ")
    return 


def crit():
    print("   ______     _ __  _            __   __  ___ __     __")
    print("  / ____/____(_) /_(_)________ _/ /  / / / (_) /_   / /")
    print(" / /   / ___/ / __/ / ___/ __ `/ /  / /_/ / / __/  / / ")
    print("/ /___/ /  / / /_/ / /__/ /_/ / /  / __  / / /_   /_/  ")
    print("\____/_/  /_/\__/_/\___/\__,_/_/  /_/ /_/_/\__/  (_)   ")
    return


def gameoverscreen():
    print("   ______                        ____                 ")
    print("  / ____/___ _____ ___  ___     / __ \_   _____  _____")
    print(" / / __/ __ `/ __ `__ \/ _ \   / / / / | / / _ \/ ___/")
    print("/ /_/ / /_/ / / / / / /  __/  / /_/ /| |/ /  __/ /    ")
    print("\____/\__,_/_/ /_/ /_/\___/   \____/ |___/\___/_/     ")
    return


main()