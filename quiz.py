
'''quiz title tabs center it at top of page'''
print "\t\t\tFILL IN THE BLANKS QUIZ"
'''asks players name and prints it'''
player_name = raw_input("What is your name?")
print "Hello, """ + player_name + ''""

'''quiz questions and answers their level of difficulty'''
easy_question = "A Python __1__ is a name used to identify a variable, __2__, __3__, module or other __4__ ."
medium_question = "__1__ that are defined inside a __2__ body have a __3__ scope, and those defined outside have a __4__ scope." 
hard_question = "As with most other languages, Python has a set of similar primitive data types such as __1__, __2__, __3__, and __4__."

easy_answers = ["identifier","function","class","object"]
medium_answers = ["Variables","function","local","global"]
hard_answers = ["string", "integer)", "boolean", "float"]

'''blanks'''
blanks = ["__1__", "__2__", "__3__", "__4__"]

'''quiz question and answer corresponding to level displayed'''
'''this function puts everything together to prompt the game '''
def choose_level():
  level = raw_input("\nChoose the level you wish to play. Enter easy, medium, hard:\n")
  if level == "easy":
    print "\nYou chose level Easy."
    return play_game(easy_question, easy_answers, blanks) 
  elif level == "medium":
    print "\nYou chose level Medium."
    return play_game(medium_question, medium_answers, blanks)
  elif level == "hard":
    print "\nYou chose level Hard."  
    return play_game(hard_question, hard_answers, blanks)
  else:
    return choose_level()
'''this is where users are asked to input their responses, where the responses are tested and blanks are filled'''
def play_game(questions, answers, blanks):
  index = 0
  max_attempts = 3
  while index < len(blanks): #looks through the list of answers and checks if they are correct or proceeds to incorrect answer
    replaced = []   #creates a list to fill in quiz answers
    print questions
    user_input = raw_input("Enter your answer: " + blanks[index] + "")
    if user_input == answers[index]: # states answer is True
        print "Correct"
        questions = questions.replace(blanks[index], user_input) #replaces blanks with user input
        index += 1
    else:
        print "Incorrect, try again"
        max_attempts -= 1 #tracks incorrect attempts and lists remaining
        print "You have """ + str(max_attempts) + "attempts left." #prints remaining attempts
        index += 1
    if max_attempts == 0: #when all attempts are used ends game
        print"\nGame Over"
        break
  else:
      print questions #prints the question with all blanks filled
      print "\n" + player_name + ", You Win"
            
choose_level()


