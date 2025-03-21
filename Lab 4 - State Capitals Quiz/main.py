# Paige Moua, Melina Hourai, Leilani Grimaldo
# Group 3
# 2/20/2025
# Purpose: Create a program that quizzes the user on state capitals.

import random

def read_file_to_dict(file):
    '''Passes file name as string and opens file, reading and separating each state and capital.
        The state and capital are stored as a key:value pair in the diction. Returns the filled dictionary.'''
    file = open(file)
    dictionary = {}
    for i in range(50): # Runs through all 50 states
        state_capital = file.readline() #reads lines in text file
        state_capital = state_capital.strip() #gets rid of spaces
        state_capital = state_capital.split(',') #gets rid of comma
        dictionary.update({state_capital[0]: state_capital[1]})
    return dictionary

def get_random_state(dictionary):
    '''Pass the states dictionary, converts dictionary to list and returns a randomly chosen value
    used as the correct state and pairs it with the correct capital'''
    #randomly chooses key & value (state & capital) in list of state_capitals file
    list_states_capitals = list(dictionary.items())
    correct_pair_index = random.randint(0, 49)
    return list_states_capitals[correct_pair_index]


def get_random_choices(dictionary, correct_capital):
    '''Passes in the states dictionary and the capital of the correct answer.
    Converts dictionary to list and chooses 3 incorrect choices. Then places 3 inccorect and 1 correct
    and shuffles and returns the list'''
    capitals = list(dictionary.values()) #Returns a list of all the values in the dictionary,
    list_of_capital_options = [] #Initializes list of possible capital options
    for i in range(3): #range of incorrect choices
        incorrect = random.randint(0, 49)
        while capitals[incorrect] == correct_capital or capitals[incorrect] in list_of_capital_options:
            incorrect = random.randint(0, 49)
        list_of_capital_options.append(capitals[incorrect]) #adds incorrect capital to the list
    list_of_capital_options.append(correct_capital) #adds correct capital to list of answer options
    random.shuffle(list_of_capital_options) #shuffles options
    return list_of_capital_options


def ask_question(correct_state, possible_answers):
    '''Passes in the correct state as a string and list of choices, prompts the user for a valid input of A-D.
        Returns user input.'''
    print(f'What is the capital of {correct_state}?') # Asks the question of the correct state corresponding to correct
                                                      # ...capital
    print(f"     A. {possible_answers[0]}  B. {possible_answers[1]}   C. {possible_answers[2]}   D.{possible_answers[3]}")
    user_input = input("Enter selection: ")
    while user_input.lower() not in ('a', 'b', 'c', 'd'): # Validates the user input A-D, repeated asking until valid
        print("Invalid input. Input choice A-D.")
        user_input = input("Enter selection: ")
    if user_input.upper() == 'A': #assigns 'A' with 0
        user_input = 0
    elif user_input.upper() == 'B': # assigns 'B' with 1
        user_input = 1
    elif user_input.upper() == 'C': # assigns 'C' with 2
        user_input = 2
    else:
        user_input = 3
    return user_input

def main():
    file = 'statecapitals.txt'
    dictionary = read_file_to_dict(file)
    loop = 0
    correct_answers = 0 #later counts correct answers
    print('- State Capitals Quiz -')
    while loop < 10: # loops based on number of questions
        correct_pair = get_random_state(dictionary)
        correct_capital = correct_pair[1]
        correct_state = correct_pair[0]
        possible_answers = get_random_choices(dictionary, correct_capital)
        print(f'{loop + 1}.', end=' ') #assigns correct question number
        user_input = ask_question(correct_state, possible_answers)
        if possible_answers[user_input] == correct_capital: #checks for correct or incorrect answer
            print('Correct!')
            correct_answers += 1
        else:
            print(f'Incorrect! The correct answer is: {correct_capital}')
        loop += 1 
    print(f'End of test.  You got {correct_answers} correct.')



main()
