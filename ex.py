#from ast import FloorDiv
# library wich is responsible for floordivision
#from random import randint
# lib. for random input
#import copy
# it copies the matlab game all together with the input
print("welcome to the metlab game")
playing = input("Lets play, shell we\n")
if playing.lower() != 'yes':
    quit()

else:   
    print("Okey, let's play the game: \n")
    name1 = input("Enter your name: ")
    name2 = input("Enter your Friend's name: ")
    name3 = input('Enter another Friends name: ')
    place = input("Enter a Place name: ")
    adjective1 = input('Enter an adjective: ')
    adjective2 = input('Enter an another adjective: ')
    adjective3 = input('Enter one more adjective: ')
    adverb1 = input('Enter an adverb: ')
    adverb2 = input('Enter an another adverb: ')
    exclamation = input("Enter an imotion: ")
    #print story
    print(
        "One day " +name1+ " went to " +place+". "
    
        'He felt very lonely, even though the view was ' +adjective1+ "."
        ' He decided to call his two bestfriends ' +name2+ ' and' +name3+'.'
        ' When they came, they told ' +name1+ ' something '+adjective2+ ' had happened ' +name1+ ' went there very ' +adverb1+ '.'
        'When he came he found out that his other friend was falling off a cliff'
        +name1+ ' said ' +exclamation+ ' Inside he is was felling ' +adjective1+ '.'
        +name1+ ' manged to save him '
        "After that they had a " +adverb2+ ' celebration'
        'They all laughed')


