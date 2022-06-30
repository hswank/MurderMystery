#importing time to allow the sleep function to work
import time

#function to print game intro
def printIntro(userName):
    print('''"Welcome to Storybrooke Inn" reads the sign as you
get out of the taxi.  You walk up the front steps into
the entrance and up to the front desk.''')
    print()
    #Pauses to keep the reader caught up with the dialogue
    time.sleep(4)
    
    print('"Hello, ' + userName + '. Welcome to the inn.  Your ')
    print('''room will be up the stairs behind me.
To the left is our lounge, to the right
is the dining area. My name is Mr. Donaldson,
let me know if you need anything" says the
man behind the front desk.''')
    print()
    time.sleep(4)

    print('''It is late and you are tired, so you head straight
up to your room and go to sleep for the night...''')
    print('____________________________________________________')
    print()
    print()
    time.sleep(3)

    print('''You awake the next morning to a scream.
You run downstairs and see a crowd of
people around what looks like a dead body.
"Call the police!" you yell, but Mr.
Donaldson tells you they can't because
the phone lines have been knocked out
due to the blizzard happening outside.''')
    print()
    time.sleep(5)

    print('''You look around at the unfamiliar faces
of the people standing around and begin
to wonder who could have done this.''')
    print()
    time.sleep(4)

    print('And will you be next?...')
    print()
    print()
    print()
    time.sleep(4)
    
#function for if player chooses to search the left wing of guest rooms
def searchLeftWing():
    #starting the room variable out with a value to enter upcoming while loop
    room = ''
    #input validation to make sure player chooses a guest room to search
    while room != 'g' and room != 'c' and room != 'b':
        #ask user for room choice
        print('''Whose room would you like to search?
Choose "g" for Giovanni, "c" for Cassandra, or "b" for Betty''')
        #assign room choice to variable
        room = input()
        print()

    #if operation to decide what info to give user
    #based on which room they choose to search
    if room == 'g':
        print('''You enter Giovanni's room.
In Giovanni's room you find a lot of muddy footprints.
There is an airline ticket on his dresser for next
week for Kyiv International Airport.''')
    elif room == 'c':
        print('''You search Cassandra's room.
In Cassandra's room you find a lot of clothes strewn about.
The bed is unmade and everything is messy.
You notice a wad of cash on her bedside table.''')
    else:
        print('''You search Betty's room.
In Betty's room you find burn cream on her table.
Everything is very orderly and smells
faintly of moth balls and ginger.''')


#function for if the player chooses to search the right wing of guest rooms
def searchRightWing():
    #starting the room variable out with a value to enter upcoming while loop
    room = ''
    #input validation to make sure  player chooses a guest room to search
    while room != 'j' and room != 'l' and room != 'm':
        print('''Whose room would you like to search?
choose "j" for jackson, "l" for leonardo, or "m" for Mary''')
        #assign room choice to variable
        room = input()
        print()

        #if operation to decide what info to give user
        #based on which room they choose to search
        if room == 'j':
            print('''You search Jackson's room.
In Jackson's room you find video games and food wrappers.
There is a pile of trash in the corner
with flies buzzing around.''')
        elif room == 'l':
            print('''You search Leonardo's room.
In Leonardo's room you find a case of cigars.
There are mink coats hanging over the shower curtain.
You also find a lock box on the counter.''')
        else:
            print('''You search Mary's room.
Right away you notice there are very little personal items.
However, in the bathroom you notice a strong bleach smell.
You find a mysterious bottle under the sink with the label wripped off.''')

#function for if the player chooses to search rooms
def searchRooms():
    #starting the wing variable out with a value to enter upcoming while loop
    wing = ''
    #input validation to make sure player chooses a wing to search
    while wing != 'left' and wing != 'right':
        print('Which wing of rooms would you like to search?')
        print('Choose "left" or "right"')
        #assign wing choice to variable
        wing = input()
    
    #if operation to enter into search wing functions based on user choice
    if wing == 'left':
        searchLeftWing()
    else:
        searchRightWing()

#function to interview guest 1
def interviewG():
    print('''You find Giovanni in the Lounge by the fireplace.
You notice his shoes are muddy.  You ask him where he's been.
He tells you he likes to walk in the forest around the Inn.
He says it reminds him of home.
Then he tells you to mind your own business.''')

#function to interview guest 2
def interviewC():
    print('''You see Cassandra in the dining room doorway to the kitchen.
She is yelling at Chef Patti about her coffee tasting old.
You ask her where she was before the body was found.
She tells you she's been in the housekeeping room with Tiffany.
She says Tiffany has been doing a lousy job of cleaning her room.
She also tells you she has been spending a lot of time with Mary.''')

#function to interview guest 3
def interviewB():
    print('''You notice Betty sitting alone in the Lounge reading a bible.
You ask her if she's doing okay.
She tells you all the excitement is tiresome for her heart.
She seems very distraught about the body.
She tells you the poor person is surely with the Lord now.
You leave her to her studies.''')

#function to interview guest 4
def interviewJ():
    print('''You find Jackson fidgeting on a chair in the dining room.
You ask him where he's been.
He tells you he was in his room until he heard the screaming.
He wants to get back to his MMORPG but he's afraid to be alone.
He asks you to find who the murderer is so he can get back to gaming.''')

#function to interview guest 5
def interviewL():
    print('''You see Leonardo sitting tensely on a sofa.
You ask him if he's worried about something.
He tells you he thinks the person was murdered for their money.
He thinks a lot of the people at the Inn look down on their luck.
He's worried he may be next.''')

#function to interview guest 6
def interviewM():
    print('''You happen to see Mary ducking out of the Dining area door into the hallway.
You ask her where she's going.
She tells you she is looking for Tiffany.
She says she needs towels to take a shower.
You notice white residue on her hands.''')

#function to interview the chef
def interviewP():
    print('''You head into the Kitchen to speak with Patti.
You ask her if she's noticed anything strange lately.
She tells you she noticed the lid to her chili was off the pot.
She also says she saw the ladel had been moved.
She noticed food splattering around the pot and a bowl missing.''')

#function to interview the housekeeper
def interviewT():
    print('''You knock on the housekeeping door to find Tiffany.
You ask her where she's been today.
She tells you she was looking for some extra
strength cleaning powder Mary had requested.
You ask her what Mary needed the cleaner for.
She tells you she doesn't know.''')

#function to move to the lounge for interviewing
def interviewLounge():
    #setting up the variable to enter the while loop
    guest = ''
    #input validation to ensure player chooses a guest to interview
    while guest != 'g' and guest != 'l' and guest != 'b':
        print('Which guest would you like to interview?')
        print('Choose "g" for Giovanni, "l" for Leonardo, or "b" for Betty')
        #assigning guest player chooses
        guest = input()
        print()

    #if operator to interview the guest the player chose
    if guest == 'g':
        interviewG()
    elif guest == 'l':
        interviewL()
    else:
        interviewB()

#function to move the player to the dining area for interviewing
def interviewDining():
    #setting up the variable to enter the while loop
    guest = ''
    #input validation to ensure player chooses a guest to interview
    while guest != 'c' and guest != 'j' and guest != 'm':
        print('Which guest would you like to interview?')
        print('Choose "c" for Cassandra, "j" for Jackson, or "m" for Mary')
        #assigning guest player chooses
        guest = input()
        print()

    #if operator to interview the guest the player chose
    if guest == 'c':
        interviewC()
    elif guest == 'j':
        interviewJ()
    else:
        interviewM()

#function to move the player to the back rooms for interviewing
def interviewBack():
    #setting up the variable to enter the while loop
    employee = ''
    #input validation to ensure player chooses an employee to interview
    while employee != 'p' and employee != 't':
        print('Which employee would you like to interview?')
        print('Choose "p" for Chef Patti, or "t" for Tiffany')
        #assigning employee player chose
        employee = input()
        print()

    #if operator to interview the employee the player chose
    if employee == 'p':
        interviewP()
    else:
        interviewT()

#function to move to front desk and interview Innkeeper
def interviewFront():
    print('''You find Mr. Donaldson at the front desk.
You ask him if he knows anything about the body.
He tells you the person had requested a bowl of chili.
He says he went looking for Patti,
but when he went in the kitchen,
there was already a bowl ready,
so he took it out to them.
Minutes later, they were dead.''')

#function to interview guests
def interview():
    #setting up the variable to enter the while loop
    area = ''
    #input validation to ensure player chooses and area to enter
    while area != 'lounge' and area != 'dining area' and area != 'back rooms' and area != 'front desk':
        print('Would you like to interview guests in the lounge, dining area, back rooms, or front desk?')
        print('Choose "lounge", "dining area", "back rooms", or "front desk"')
        #assigning area player chose
        area = input()
        print()
        
    #if operator to move into the area the player chose
    if area == 'lounge':
        interviewLounge()
    elif area == 'dining area':
        interviewDining()
    elif area == 'back rooms':
        interviewBack()
    elif area == 'front desk':
        interviewFront()

#function to enter into game play
def gameplay():
    #starting variables off with variables to enter into upcoming while loops
    answer = ''
    option = ''
    
    #while loop to keep player playing until they are ready to accuse someone of the murder
    while answer != 'yes' and answer != 'y':
        #input validation to make sure player chooses an action
        while option != 'search' and option != 'interview':
            print()
            print('''Would you like to search the inn or interview someone?
Choose "search" or "interview": ''')
            #assign action to variable
            option = input()

        #enter into search portion of game if user decides to
        if option == 'search':
            searchRooms()
        else:
            interview()
        option = ''

        #ask the player if they are ready to accuse a murderer and end the game
        print()
        print('''Are you ready to accuse someone of murder?
Choose yes or no: ''')
        #assigning players choice to variable to exit the while loop
        answer = input()
        print()
                    
#function to determine whether player's accusation was correct
def accusation(culprit):
    #assigning a variable to hold the murderer's name
    murderer = 'Mary'
    print('You accuse ' + culprit + ' of the murder.')

    #if operation to decide what to do based on who the player accuses
    if culprit == murderer:
        print('Just like magic, the blizzard clears up,')
        print('Mr. Donaldson calls the authorities and ')
        print('the police arrive, hauling ' + murderer + ' away')
        print()
        time.sleep(4)

        print('''Congratulations, you have have solved the
mystery and the murderer is behind bars.
Turns out Mary had poisoned the person
with cleaning solution to steal his money.
She tells you Mr. Leonardo would've been next
if you hadn't meddled in her affairs.
You win!!!''')

    else:
        print('''It is getting late and you go upstairs to your room.
Unfortunately, you are murdered in your sleep
and you never see the light of day again.
You lose!!!''')
    
#defining main function to bring together all functions
def main():
    #making the game personable by incorporating the player's name
    print('Welcome to my Murder Mystery game.  Please enter your name: ')
    userName = input()
    print()

    #calling introduction function to start game
    printIntro(userName)

    #calling gameplay function
    gameplay()
    
    #asking the player to accuse the guest they think committed the murder
    print('''Who do you think the murderer is?
Choose "Giovanni", "Cassandra", "Betty", "Jackson", "Leonardo", or "Mary"''')
    culprit = input()

    #entering the name of the player 
    accusation(culprit)

    time.sleep(60)

    
#Calling main to run program
main()
