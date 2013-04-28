# Rock-paper-scissors-lizard-Spock
# Author: Jessica Burnett 2013

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def number_to_name(number):
    # fill in your code below
    if number == 0:
        name = "rock"
        #print name
    elif number == 1:
        name = 'Spock'
        #print name
    elif number == 2:
        name = 'paper'
        #print name
    elif number == 3:
        name = 'lizard'
        #print name
    elif number == 4:
        name = 'scissors'
        #print name
    else: 
        print 'Warning: invalid number_to_name'
    return name

#test 
#number_to_name(1)
    
    
def name_to_number(name):
    # fill in your code below
    if name == 'rock':
        number = 0
        #print number
    elif name == 'Spock':
        number = 1
        #print number
    elif name == 'paper':
        number = 2
        #print number
    elif name == 'lizard':
        number = 3
        #print number  
    elif name == 'scissors':
        number = 4
        #print number
    else:
        print 'Warning: invalid name_to_number'
    return number
#test 
#name_to_number('lizard')   

def rpsls(name): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
   
    print 'Player chooses', name 
    print 'Computer chooses', number_to_name(comp_number) 
    
   
    #compute difference of player_number and comp_number modulo five
    diff = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner
    if diff == 1 or diff == 2: 
        print 'Computer wins!'
    elif diff == 0:
        print 'Player and computer tie!'
    else:
        print 'Player wins!'
    print ''    
   
# test
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
