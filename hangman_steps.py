# KP, Hangman Steps


#create a list of 10 words on a seperate txt file
#done

# create another file holdswin/loss counts
# 

# Use split(",") on the content of the words txt document to create your list of words.


# Pull win and lose totals from the other txt file and save them as 2 seperate variables.

#Build the hangman game

#Save the correct word as a variable random.choice(name of the list)
#number of wrong guesses
#What letters have been guessed


# Function to display the hangman (Needs number of wrong guesses)
"""______
   |    |
   |    O
   |   /|\\
   |   / \\
   |________
"""

# Function to show the letters and spaces (The correct word, letters that have been guessed)

#Loop over the correct word
    #check if lettetr has been guessed
    #Variable for display word 
    #Check if letter has been guessed
        #then add the letter to the display word
    # If they haven't guessed the letter
        #add an underscore to the display word
# return the finished word (outside of the loop)



# Main game loop (while True)
# call function to show hangman
# print function call to show display word
# create variable and user to guess a letter 
# add the letter to list of guessed letters
# check if letter is not in word
    # increase incorrect guesses
# check if display word is same as the word
    # Tell user they won!
    # Increase win total
    #Ask if they want to play agian
        #reset random word, wrong guess count
# check to see if they lost (if they have 6 worng guesses)
    #tell them they lost
    #tell them what the word was
    #Increase the lost count
     #Ask if they want to play agian
        #reset random word, wrong guess count