from random import randint

print(f'''
{'Game Rules':*^110}
If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
It doesn't count the tries that are "OUT OF BOUNDS!"
On a player's first turn, if their guess is within 10 of the number, return "WARM!"
If it is further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is closer to the number than the previous guess return "WARMER!"
If it is farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
{'':*^110}
''')

random_number = randint(1, 100)
guess_list = []

while True:  
    my_guess = int(input('What is your guess: '))
            
    if my_guess<1 or my_guess>100:
        print ('OUT OF BOUNDS')
        continue
    
    guess_list.append(my_guess)        
    
    if my_guess == random_number:
        number_of_tries = len(guess_list)
        print (f'\nYou guessed correctly and it took {number_of_tries} tries! The random number is {random_number}!')
        break
       
    elif len(guess_list)>1:
        if abs(my_guess-random_number) < abs(guess_list[-2]-random_number):
            print ('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs (my_guess-random_number)>= 10:
            print ('COLD!')
        else:
            print ('WARM!')
    
