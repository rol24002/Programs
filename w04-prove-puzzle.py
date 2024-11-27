"""
    Madison Rollins 
   W04 Prove Assignment: Word Puzzle
"""
"""
#title
print(""
___________

      HI PALL!  WELCOME TO SHIKI'S CRAZY WORD GUEESER!

                    °˖✧◝(⁰▿⁰)◜✧˖°  
      
        I have thought of a super awsome 8 letter
        word and it's your job to guess what it is!
      
      You get INFINATE GUESSES!!!! :   ⊹⋛⋋( ՞ਊ ՞)⋌⋚⊹
___________
"")
#ready fready?
print()
ready = input ('Are you ready?: ')
#if no loop
if ready.lower() == 'no':
    print()
    ready = input ('Are you ready?: ')
#yes to start
else: 
    print()
    print('YAY!   °˖✧◝(⁰▿⁰)◜✧˖° ')
    print()
    print()
    #da word
    word = 'frazzled'
    count = 0
    #display enitial
    print('Your word is! : _ _ _ _ _ _ _ _')
    #Enter Guess
    guess = input('What word is it? (○´ ― `)ゞ  ')
    while word != guess.lower():
        print()
        print('Sorry, that is not the word. (っ˘̩╭╮˘̩)っ Try again: ')
        guess= input('What word is it? (○´ ― `)ゞ  ')
        count = (count + 1)
    print()
    print(f'YAY!   °˖✧◝(⁰▿⁰)◜✧˖°  You guessed it! The word was {word.upper()}!')
    print()
    print(f'You guessed it in {count} tries! ⊹⋛⋋( ՞ਊ ՞)⋌⋚⊹ ')


    #prove part

"""
print("""___________

      HI PALL!  WELCOME TO SHIKI'S CRAZY WORD GUEESER!

                    °˖✧◝(⁰▿⁰)◜✧˖°  

        I have thought of a super awsome word and..
      it's your job to guess what it is!
                 
                 ⊹⋛⋋( ՞ਊ ՞)⋌⋚⊹
___________
""")
print()
print("""====== How to Play ======:
          ~ Enter a gues that has the
          same # of letters as 
          my chosen word!
          ~ "_" means the letter is 
          not in the word.
          ~ Lowercase letters mean the
          letter is in the word but 
          are not in that spot.
          ~ Upercase letters mean the 
          letter is in the right spot.
    """)
#ready fready?
print()
ready = input ('Are you ready?: ')
#if no loop
if ready.lower() != 'yes':
    print()
    ready = input ('Are you ready?: ')
#yes to start
else: 
    print()
    print('YAY!   °˖✧◝(⁰▿⁰)◜✧˖° ')
    print()
  #da word
    word = 'frazzled'
    count = 1
    for index in range(len(word)):
        letter = word[index]
#display enitial
    print('Here is my word! づ ◕‿◕ )づ ')
    for _ in range(len(word)):
        print('_ ', end="")
    print()
    print()
    #enter Guess
    guess = input('What word is it? (○´ ― `)ゞ  ')
while True:
    if range(len(guess)) != range(len(word)):
            print('I am so sorry, THAT is not an 8 letter word. ༽◺_◿༼  Please try again.')
            guess = input('What word is it? (○´ ― `)ゞ  ')
    else:
        while guess.lower() != word:
            count = (count + 1)
        for i in range(len(word)):
            letter = word[i]
            guess_letter = guess.lower()[i]
            if letter.lower() == guess_letter:
                print(letter.upper(), end=" ")
            elif guess_letter in word:
                 print(guess_letter.lower(), end=" ")
            else:
                 print('_ ', end="")
        print()
        guess = input('What word is it? (○´ ― `)ゞ  ')
        
        print(f'YAY!   °˖✧◝(⁰▿⁰)◜✧˖°  You guessed it! The word was {word.upper()}!')
        print()
        print(f'You guessed {word.upper()} in {count} tries! ⊹⋛⋋( ՞ਊ ՞)⋌⋚⊹ ')

"""for letter in word:
        if range(len(guess)) != range(len(word)):
            print('I am so sorry, THAT is not an 8 letter word. ༽◺_◿༼  Please try again.')
            guess = input('What word is it? (○´ ― `)ゞ  ')
        elif letter == word[index]:
            print(letter.upper(), end="")
        else:
           print('_', end="")
           guess = input('What word is it? (○´ ― `)ゞ  ')"""
    
#Enter Guess
"""guess = input('What word is it? (○´ ― `)ゞ  ')
    for letter in word:
        if letter.lower() == guess.lower():
            print(letter.upper(), end="")
        #elif letter.lower() == 
    else:
       guess = input('What word is it? (○´ ― `)ゞ  ')
"""