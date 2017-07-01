print "\t\t\tFILL IN THE BLANKS QUIZ"   #quiz title tabs center it at top of page

player_name = raw_input("What is your name? ")  #asks players name and prints it
print "Hello, "'' + player_name + ''""

#quiz questions and answers their level of difficulty
easy_question = "A Python __1__ is a name used to identify a variable, __2__, __3__, module or other __4__ ."
medium_question = "__1__ that are defined inside a __2__ body have a __3__ scope, and those defined outside have a __4__ scope." 
hard_question = "As with most other languages, Python has a set of similar primitive data types such as __1__, __2__, __3__, and __4__."

easy_answers = ["identifier","function","class","object"]
medium_answers = ["Variables","function","local","global"]
hard_answers = ["string", "integer", "boolean", "float"]

blanks = ["__1__", "__2__", "__3__", "__4__"]   #blanks in question

def choose_level():
  """this function puts everything together to prompt the game, matches questions and answers with corresponding level""" 
  level = raw_input("\nChoose the level you wish to play. Enter easy, medium, hard:\n").lower()
  if level == "easy":
    print "\nYou chose level easy."
    return play_game(easy_question, easy_answers, blanks) 
  elif level == "medium":
    print "\nYou chose level medium."
    return play_game(medium_question, medium_answers, blanks)
  elif level == "hard":
    print "\nYou chose level hard."  
    return play_game(hard_question, hard_answers, blanks)
  else:
    return choose_level()

def play_game(questions, answers, blanks):
  """this is where users are asked to input their responses, where the responses are tested and blanks are filled"""
  index = 0
  attempts = 1  #allows a loop
  max_attempts = 3 #sets the  max number of incorrect attempts
  while index < len(blanks) and attempts <= max_attempts: #looks through the list of answers and checks if they are correct or proceeds to incorrect answer
    replaced = []   #creates a list to fill in quiz answers
    print questions
    user_input = raw_input("Enter your answer: " + blanks[index] + "").lower() #User inputs answer
    if user_input == answers[index]: # states answer is True
        print "\nThat is correct"
        questions = questions.replace(blanks[index], user_input) #replaces blanks with user input
        index += 1
    else:
        print "Sorry, that is incorrect. This was attempt number " + str(attempts) #shows user how many attempts are left
        attempts += 1
  if attempts > max_attempts:  #When user enters more than 3 incorrect answers the game ends
    print "No more tries, game over."
        
  if index == len(blanks):  #When user enters all right answers prints you win and prints the question with all blanks filled
    print questions
    print "Congratulations,you win!\n"
  
choose_level()

