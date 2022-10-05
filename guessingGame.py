import random
import keyboard
import time 


'''
Number guessing game 
'''

welcome_user = print('Welcome! to the number guessing game')

time.sleep(2)
#ask uer for their name to personalize the game
user_name = input('Before we begin please enter your name: ')

def welcome():
    print('welcome {0} to the number guessing game'.format(user_name))
    time.sleep(2)

    print(' To play the game we you will need to you enter \n two numbers positive numbers, \n these two numbers will be the lower bound and upper bound range \n that you will use to guess a number')
    time.sleep(2)



def play():
    
    lower_bound_number = abs(int(input('please enter your lower bound number: '))) 
    if lower_bound_number < 0:
        print('your lower bound number cannot be negative')
    upper_bound_number = abs(int(input('please enter your upper bound number: ')))
    if upper_bound_number > 100:
        print('your upper bound is too big please enter a smaller number')


    if upper_bound_number < lower_bound_number:
        print('Your upper bound number is smaller then your lower bound number ')
    elif upper_bound_number - lower_bound_number < 5:
        #we can add a functionality that lets the user enter the appropriate number in order to continue
        print('the range you entered is too small to play the game, please try again')
    else:
        print('lets play')
    
    random_number = random.randint(lower_bound_number, upper_bound_number)

    

    guesses_taken = 0
    guesses = 5
    while guesses_taken <= guesses:
        time.sleep(2)
        
        
        
        number_guessed = int(input('Guess a number........ '))
        #num = int(number_guessed)
        guesses_taken += 1

        if guesses_taken < guesses:
            if number_guessed < random_number:
                print('the number guessed is too low')
            elif number_guessed > random_number:
                print('the number guessed is too high')
            elif number_guessed == random_number:
                print('Great job {} you guessed the number in {} guesses'.format(user_name, guesses_taken))  
                break
            # elif number_guessed != random_number:
            #     print('You guessed the wrong number  ')             
    else:
        print('you lost')

    
play = input('Would you like to play a number guessing game?')    

while play =='yes' or play =='Y'  or play =='y':
    welcome()
    play()
    
    if play =='n' or 'no':
        break