"""
This is virtual song only for the  Dictonary Exercise
written by Eyal Lev
Date April 5th 2019
"""
MySongDictonary={'SongName':'My First Exercise','AuthorFirstName':'Jhon','AuthorLastName':'Martin',
                'Genre':'Eastern','SongNumbeOfWords':97,'NumberOfDifferentWords': 72,'SongPlayDuration':4.36,
                'AutorNumberOfKids':4,'AutorKidsName':['Gim', 'Shelly', 'Rebeca', 'Mark'],'AuthorWifeName':'Lisa'}
MySongKeyList=['SongName','AuthorFirstName','AuthorLastName','Genre','SongNumbeOfWords','NumberOfDifferentWords',
               'SongPlayDuration','AutorNumberOfKids','AutorKidsName','AuthorWifeName']


def exit_typed(guess1):                                  # Function that return True if Exit typed and False if not
    if str.lower(guess1)!= "exit":
        return False
    else:
        return True

correct_answers=0
for key in MySongKeyList:                                                   # going over all keys in Key List
    guess = input("Please enter "+key+'(type "exit" to Abort):--> ')        # ask the user for first guess
    if not exit_typed(guess):                                           # if the user didn't type exit
       for NumOfGuess in range(3):                                          # start counting 3 guesses
            if str.lower(str(guess)) == str.lower(str((MySongDictonary[key]))):         # if the value is equal to the value behind its key
                 print ("Correct Answer!!")
                 correct_answers+=1                                         # number of correct answers
                 break                                                      # stop guessing since the user has succeed
            elif NumOfGuess == 0:                                           # if the user wrong
                 guess = input('Incorrect ,Please try again , you have additional two time(type "exit" to Abort):--> ')
                 if not exit_typed(guess):                              # ask the user to second guess
                    continue                                                # if the user didn't type "exit
                 else:
                     exit()                                                  # if the user typed "exit
            elif NumOfGuess == 1:                                             # if the user wrong again
                 guess = input("Incorrect, Please try again , No Pressure but it's your last chance(type \"exit\" to Abort):-->")
                 if not exit_typed(guess):                                   # ask the user to last guess
                     continue                                                  # if the user didn't type "exit again
                 else:
                     exit()                                                     # if the user typed "exit
            else:
                 print("you failed to guess!!")                                 # if the user failed to guess all three guesses
                 print ("The "+key+ " is :  "+str(MySongDictonary[key]))        # print the correct   guess
    else:
        exit()

print (" you Guessed "+ str(correct_answers)+ " guesses out of "+str(len(MySongKeyList)))









