def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print '-----------'
   
    lettersGuessed = []
    nguess = 8 
    while nguess>0:
        print 'You have ' +str(nguess)+' guesses left.'
        print 'Available letters: ' +  getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
        
        if isWordGuessed(guess, lettersGuessed) == True:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
        
        elif isWordGuessed(guess, list(secretWord)) == True:
            lettersGuessed.append(guess)
            print 'Good guess: '+ getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
            if isWordGuessed(secretWord, lettersGuessed) == True:
                break
            
        
        else:
            lettersGuessed.append(guess)
            nguess -= 1
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            print '-----------'       
        
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print 'Congratulations, you won!'
        
    elif nguess == 0:
        print "Sorry, you ran out of guesses. The word was " + secretWord +'.'                             
        
