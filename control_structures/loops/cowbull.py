'''
Python program to make a game similar to cows and bulls
Two players can play the game
firstly a player enters a 4 digit secret number in range of 1-6.
Second player have to guess the number given by first player in 3 guesses
Suppose if first player entered 1234 as secret number
second player will be given three chances for guessing
1st guess : 1345 => should print +--  as (+)1 is at exact position and also present in secret number
    (-)3,4 are in number but in different position  (' ')5 not in number
2nd guess : 1234 => should print ++++ and you won and stops 3rd guess as player won

Input
enter secret number for game:2345
player have three guesses for a 4digit number.(number range 1-6)

Output
1234
 --- have another try
1245
 -++ have another try
2345
++++ you won
well played

'''
import getpass
#getpass is used to get input hidden
msg = 'enter secret number for game:'
sec = getpass.getpass(prompt=msg,stream=None)
msg = 'player have three guesses for a 4digit number.(number range 1-6)'
print(msg)
for i in range(0,3):#three guesses
    g = str(raw_input())
    scr = str()
    if(g==sec):#if guess = actual
        print('++++ you won')
        break
    else:
        for j in range(0,len(sec)):
            if(sec.find(g[j])==g.find(g[j])):
                #if position of a digit in guess = position of digit in actual number
                scr = scr+'+'
            elif(sec.count(g[j])==g.count(g[j]) and sec.find(sec[j]) != sec.find(g[j]) ):
                #if position of digit is not same but if digit exists in numbers
                scr = scr+'-'
            else:
                #if no match in position or occurence
                scr = scr+' '
        print(scr+' have another try')
print('well played')
