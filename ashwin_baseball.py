'''
Program Name: ashwin_baseball.py
Programmer Name: Ashwin Mayurathan
Date: 2-23-2022
Description: This code takes all 9 players from the file known as
             player_statistics.txt (technically the code can accept more) and
             plays a 5 inning game of baseball using the statistics provided
             from the text file. During this game, the user must click enter
             before each player hits the ball, and then prints relevant
             information pertaining to the game. At the end of the game the
             final score is compared to another team's score (a randomly
             generated number from 0 to 10) and prints out who won the game.


START OF CODE:

IMPORT RANDOM LIBRARY:
imports the random library as it is necessary for this project
'''

import random

'''
DECLARE CONSTANTS:
most of these constants are just keys for a dictionary and strings to be
printed. Some are arrays with constants in them to make it easier to access
certain constants in a loop.
'''

ALL_BATS = 'all_bats'

FIRST_BASE = 'first base'

SECOND_BASE = 'second base'

THIRD_BASE = 'third base'

HOME_RUN = 'home run'

HIT_CHANCE = 'hit_chance'

DATA_ORDER = (ALL_BATS, SECOND_BASE, THIRD_BASE, HOME_RUN, HIT_CHANCE)

BASES = 'bases'

INNING = 'inning'

OUTS = 'outs'

RUNS = 'runs'

RUN_BASES = (FIRST_BASE,SECOND_BASE,THIRD_BASE)

HIT_BASES = (SECOND_BASE, THIRD_BASE, HOME_RUN)

HIT_TYPE = ("Single", "Double", "Triple", "HOME RUN!!")

'''
FUNCTION: input_loop
This function takes in a message, and options needed to be inputted, and loops
until the proper input is given. 
'''
def input_loop(message, options):

    #Prompts for user's input with a particular message.
    user_input = input(message)

    #Loops until user input is given, .upper() used to make input NOT
    #case sensitive.
    while (user_input.upper() not in options):

        #Lets user know they had an invalid input.
        print(f"'{user_input}' is not a valid input")

        #Reprompts if necessary.
        user_input = input(message)

    return user_input.upper()

'''
FUNCTION: file_to_dict
This functions takes a file name and then  reads a file and organizes the data
from the file into a dictionary.
'''
def file_to_dict(file_name):

    #Defines the dictionary player data.
    player_data = {}

    #Opens the file.
    input_file = open(file_name, "r")

    #Sets lineread to a list of terms from the first line of the file.
    line_read = input_file.readline().split()

    #Loops until all lines are read.
    while (line_read != []):
        #stores the data into a dictionary, with the key being the player name.
        #Player_data -> #player_data -> dict{str:dict{str:float}}
        player_data[line_read[0]] = store(DATA_ORDER, line_read[1:], True)

        #Reads the next line of the file.
        line_read = input_file.readline().split()

    #Closes the file.
    input_file.close()
                
    return player_data

'''
FUNCTION: store
This function takes in list of key values to be assigned, and data, as well as
an identifier variable called special. It them places the data into a dictionary
based on provided keys. If the data is special (based upon the identifier)
then it is turned into float and rounded before being stored.
'''
def store(micro_dict_assignment, raw_data, special):

    #Intializes micro_dict
    micro_dict = {}

    #loops for how many terms are there in micro_dict_assignment
    #(loops for the number of keys).
    for i in range(len(micro_dict_assignment)):

            #Adds the key and value into micro_dict.
            micro_dict[micro_dict_assignment[i]] = raw_data[i]

            #If the data is special (needs to be formatted differently).
            if (special):
                #adds the key and formatted output to the dictionary. 
                micro_dict[micro_dict_assignment[i]] = round(float(raw_data[i])
                                                             ,3)

    return micro_dict

'''
FUNCTION: calc
This function takes in the player, their info, and what the result are currently
and calculates if the user hits the ball, what type of hit they hit, and then
updates and returns the updated results.
'''
def calc(player, info, result_info):

    #Initializes variables.
    move = 0
    move_chance = 0

    #Sets the hit variable to a number from 0 to 999 to see if the player hits
    #the ball.
    #Note: This is done so there are 1000 different numbers to choose from
    hit_var = random.randrange(1000)

    #If the player should hit the ball (based upon the player's ODP value).
    if (hit_var < info[HIT_CHANCE]*1000):
        #Set hit variable to another number from 0 to 999 to see what type of
        #hit the batter strikes.
        hit_var = random.randrange(1000)

        #loops for the the types of hits, organized by what base the batter
        #lands on.
        for i in range(len(HIT_BASES)):
            #Sees the the batter hits a particular type of hit.
            if (hit_var < move_chance +round((info[HIT_BASES[i]]/
                                        info[ALL_BATS]),3)*1000):
                #If move hasn't been reassigned yet. This is done so
                #there is no need to set a lower limit.
                if move == 0:

                    #Sets move to be 1 less than how many bases the players.
                    #E.g bats to second base -> move is 1. (This is done
                    #temporarily to print the outcome with a list).
                    move = i+1

            #updates move_chance to have a new value to check where the type
            #of hit.
            move_chance += round((info[HIT_BASES[i]]/info[ALL_BATS]),3)*1000


        #Prints how much the player has moved
        print(f"Wow! {player} hit a {HIT_TYPE[move]}")

        #Increase move by one so it how many bases the players should move.
        #E.g bats to third base -> move used to be 2 -> now move is 3.
        move += 1

        #Loops for how many times the players moves.
        for i in range(move):

            #If there is a player at third base.
            if (result_info[BASES][THIRD_BASE] != ""):
                #Prints the player made it home.
                print(f"WOW {result_info[BASES][THIRD_BASE]} MADE IT HOME!")
                #Updates so there is no player at third base.
                result_info[BASES][THIRD_BASE] = ""
                #Increases the amounts of run by 1.
                result_info[RUNS] += 1

            #If there is a player at second base
            if (result_info[BASES][SECOND_BASE] != ""):
                #Updates the third base to have the second base's value.
                result_info[BASES][THIRD_BASE] = result_info[BASES][SECOND_BASE]
                #Updates so there is no player at second base.
                result_info[BASES][SECOND_BASE] = ""

            #If there is a player at first base.
            if (result_info[BASES][FIRST_BASE] != ""):
                #Updates the second base to have the first base's value.
                result_info[BASES][SECOND_BASE] = result_info[BASES][FIRST_BASE]
                #Updates so there is no player at first base.
                result_info[BASES][FIRST_BASE] = ""

        #If the player did not hit a home run (so players do not run 4 bases).
        if (move != 4):
            #Update the appropriate base to have the player who just batted.
            result_info[BASES][RUN_BASES[move-1]] = player

        #If the player hit a home run.
        else:
            #Increase the runs by 1.
            result_info[RUNS] += 1
            #Print the player made it home. 
            print(f"WOW {player} MADE IT HOME!")

    #If the player missed.
    else:
        #Add one to total outs.
        result_info[OUTS] += 1
        #Print the player struck out.
        print(f"Ooof {player} Struck Out :(")
        
    return result_info

'''
FUNCTION: graphic
This function prints out the current field as a graphic, with the location of
each player
'''
def graphic(players,batter):

    #All the neccesary print statements.
    print("The Current Field:")
    print()
    #Prints the player at second base the center of a 40 character space.
    print(" "*((40-len(players[SECOND_BASE]))//2)+players[SECOND_BASE])
    print("\n")
    print("\n")
    #Prints the player at third base left justified, and the player
    #at first base right justified. 
    print(players[THIRD_BASE]
          + " "*(40-(len(players[THIRD_BASE])+len(players[FIRST_BASE])))
          +players[FIRST_BASE])
    print("\n")
    print("\n")
    #Prints the current batter in the center.
    print(" "*((40-len(batter))//2)+batter)

'''
FUNCTION: output
This function controls the flow of the code, and prints the important
information like the batter, who's on deck, the batter's ODP, who's at what
base, innings, stikes, and runs.
'''   
def output(): 

    #Intializes Variables
    #Uses file_to_dict to store the data in a dictionary.
    #player_data -> dict{str:dict{str:float}}
    player_data = file_to_dict('player_statistics.txt')

    #Uses the store function to initialize the bases.
    #result_info -> dict{str:dict{str:str}, str:int, str:int, str:int}
    #Note: INNINGS has the value of 1 because we start at inning 1.
    result_info = {BASES:store(RUN_BASES, ["","",""], False),
                   INNING: 1, OUTS: 0, RUNS: 0} 

    #Creates a list called roster from the player names from player_data.
    #(the names were the keys)
    roster = list(player_data.keys())

    #While we have not reached inning 6 (supposed to have 5 innings in this
    #code so it ends when inning 5 is over).
    while (result_info[INNING] < 6):

        #For each player playing in the game.
        for player in player_data:

            #If you haven't reached inning 6 yet.
            if (result_info[INNING] < 6):
                #Print the relevant information.
                print("-----------------------------------------")
                #Prints a graphic of who's at what base.
                graphic(result_info[BASES],player)
                print("========================================")
                #Uses an input_loop to wait until the user inputs enter.
                #Does not run until the user clicks enter cleanly (no a's or
                #other letters, just click enter).
                input_loop("Press Enter to Start Batting: ",[""])
                print("========================================")
                print(f"{player} is currently batting")
                
                #Modulo is used so if the next player out of the player index
                #then the index would be cycled back to index 0 (the first
                #player in the roster)
                print(f"{roster[(roster.index(player)+1)%len(roster)]}"
                       +" is on deck")
                print(f"{player}'s OBP: {player_data[player][HIT_CHANCE]}")

                #Updates result_info using calc.
                result_info = calc(player,player_data[player], result_info)

                #Loops for how many bases there are.
                for base in RUN_BASES:
                    #Prints who's at what base.
                    print(f"At {base} we have: {result_info[BASES][base]}")

                print(f"Current Inning: {result_info[INNING]}")
                print(f"Current Number of Outs: {result_info[OUTS]}")
                print(f"Current Number of Runs: {result_info[RUNS]}")
                
                #If there are 3 or more outs.
                if (result_info[OUTS] >= 3):
                    #Lets the user know the inning ended.
                    print("-----------------------------------------")
                    print("That is the end of current inning")
                    #Changes the inning.
                    result_info[INNING] += 1
                    #Resets the number of outs, and resets the bases.
                    result_info[OUTS] = 0
                    result_info[BASES] = store(RUN_BASES, ["","",""], False)
    
    #Let the user know the game is over.
    print("The game is over")
    print("-----------------------------------------")
    winner(result_info[RUNS])

'''
FUNCTION: winner
This function takes the total runs scored throughout the game, and then
compares the score to a random number from 0 to 10 to determine a winner
''' 
def winner(score):

    #Determines the other team's score as a random number from 1 to 10.
    opponent_score = random.randrange(10)

    #Prints the score of your team and the opposing team.
    print(f"Your team scored a total {score} runs\n")
    print(f"The opposing team scored {opponent_score} runs\n")
     
    #Prints the result of the game depending on yours and the opposing
    #team's score.
    if (score>opponent_score):
        print("CONGRATS YOUR TEAM WON!")

    elif (score<opponent_score):
        print("YOUR TEAM LOSS, BETTER LUCK NEXT TIME :(")

    else:
        print("THE TEAMS BOTH TIED -_-")

    print()
     #Lets the user know the code is completed.
    print("Program Is Completed")
    print("-----------------------------------------")

'''
FUNCTION: main
This function starts the code when the user inputs Y
'''
def main():

    #If the user inputs "Y" continue the code.
    if (input_loop("Do you want to begin the program? Input Y to continue: "
                                                        ,["Y","N"]) == "Y"):
        #Call the output function
        output()

#Call the main function.
main()

#END OF CODE    
