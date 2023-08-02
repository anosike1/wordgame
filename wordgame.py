# print the intro
print ("Welcome to the guessing game".title())

# store our secret word in the variable secret
secret='MOROCCO'
# for every letter in our secret word, we'll replace with underscore(_)
clue_list = ['_' for x in secret]
# join this into a string called CLUE
clue = ' '.join (clue_list)
# print our clue
print (f"Your hint is {clue}")

# set the number of trials to 0
trial = 0
# create a loop
while True:
    # the loop increases by 1 when the loop starts    
    trial+=1
    # ask the user for a guess
    guess = input ('What is your guess? ').upper()
    # if the length of the secret word is not equal to the length of our guessed word
    if len (secret)!=len (guess):
        # the user gets this response and asked to start afresh
        print ('Not even close. Start Afresh!')

    # else, we loop through our guessed word
    else:
        for i in range (len(guess)):
# and if the letters are in the same position, we replace it with upper case   
            if secret[i]==guess[i]:
                clue_list[i]=guess[i].upper()
# if the letter is present, but not in the same position, we replace it with lower case
            else:
                if guess[i] in secret:
                    clue_list[i] = guess[i].lower()
# if it's not there at all, it remains as an underscore(_)
                else:
                    clue_list[i] = "_"    
       # combine these letters to form the new clue 
        clue = ' '.join (clue_list)
        print (f"Your hint is {clue}")

# if the guess is the secret word, the loop breaks
    if guess == secret:
        break  
# then the user gets a CONGRATULATORY response with the number of tries
print ('Congratulations. You guessed it')
print (f"It took you {trial+1} tries.")