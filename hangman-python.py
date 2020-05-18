import random

def get_word():
    words = ['Miami', 'Minneapolis', 'Denver', 'San Diego', 'Los Angeles', 'Santa Fe', 'New York', 'Atlanta', 'Dallas', 'Philadelphia',
             'Baltimore', 'Houston', 'Phoenix','Austin', 'Chicago', 'Seattle', 'Boston', 'Detroit', 'Liverpool', 'Manchester', 'London', 'York']
    return random.choice(words).upper() 
    

word = get_word() 

def the_word():
    sol = []
    for letter in word:
        sol.append(letter)

    return sol

solution = the_word()

def winner():
    print("Congrats, you won!")


turns = 10
guesses = []

guess = ''  

complete = False     
while not complete: 

    guess = input("Guess a Letter!") 
    guess = guess.upper()
    status = len(word) 
    print("You have " + str(turns) + " turns remaining") 
    score = 0    

    length = len(guess)    

    if length == 1: 
        if guess in word:
            print("Yes!")
            guesses.append(guess)
            print(guesses)
            
            for letter in word: 
                if letter in guesses:
                    print (letter)
                    if letter in guesses and solution:
                        score += 1
                        if score == status:
                            winner()
                            complete = True
                else:
                    print ("*")             

            
        elif guess not in word and turns > 0:
            guesses.append(guess) 
            print("No!")
            print(guesses)
            turns -= 1
            for letter in word:
                if letter in guesses:
                    print(letter)
                else:
                    print ("*") 
            
        elif turns == 0:
            print("No more turns, YOU LOSE")
            break


    elif length > 1:
        if guess == word:
            winner()
            complete = True 
        elif guess != word and turns > 0:
            guesses.append(guess)
            print(guesses) 
            print("No!")
            turns -= 1
            for letter in word:
                if letter in guesses:
                    print(letter)
                else:
                    print ("*")
            

 
 





   
