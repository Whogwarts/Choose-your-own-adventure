import time
import random
ply = input('Do you want to play maze of secrets?')

while ply in ['y', 'Y', 'YES', 'yes', 'Yes']:
  print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("Welcome to the maze of secrets!")
  print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

  time.sleep(.5)
  print ("You have been captured by the evil king Drago he has thrown you into his maze of terror you must escape to survive. You wake up in the maze and it is dark and you can make out a stick on the floor.")
  ch1 = str(input("Do you take it? [y/n]: "))
  if ch1 in ['y','Y','yes','Yes','YES']:
    print ('You have taken the stick!')
    time.sleep(.5)
    stick = 1
  else:
    stick = 0
    print ('You did not take the stick (too bad this would have been usefull)')
  print ('As you advance you see a small glowing obejct in the distance.')
  ch2 = str(input('Do you approach it [y/n]:'))
  if ch2 in ['y','Y','yes','Yes','YES']:
      print ('You approach the light')
      time.sleep
      print ("As you draw closer, you begin to make out the object as an eye!")
      time.sleep(.5)
      print ("It's a giant spider!!")
      ch3 = str(input("Do you try to fight it? [Y/N]"))
      if ch3 in ['y', 'Y', 'Yes', 'YES', 'yes',]:
        if stick == 1:
          print ("You only have a stick to fight with!")
          print ("You quickly jab the spider in its eye and gain an advantage")
          time.sleep(1)
          print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          print ("                  Fighting...                   ")
          print ("   YOU MUST HIT ABOVE A 6 TO KILL THE SPIDER    ")
          print ("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
          print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          time.sleep(1)
          fdmg1 = int(random.randint(3, 10))
          edmg1 = int(random.randint(1, 6))
          print ("you hit a", fdmg1)
          print ("the spider hits a", edmg1)
          time.sleep(1)

          if edmg1 > fdmg1:
            print ("The spider has dealt more damage than you!")
            ply = input('Do you want to play again?')
          elif fdmg1 < 5:
              print ("You didn't do enough damage to kill the spider, but you manage to escape")
              ply = input('Do you want to play again?')
          else:
            print ("You killed the spider!")
            alive = True
            print ('you have won the game for now ...')
            ply = input('Do you want to play again?')
        else:
              print ("You don't have anything to fight with!")
              time.sleep(2)
              print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
              print ("                  Fighting...                   ")
              print ("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
              print ("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
              print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
              time.sleep(2)
              fdmg1 = int(random.randint(1, 7))
              edmg1 = int(random.randint(1, 5))
              print ("you hit a", fdmg1)
              print ("the spider hits a", edmg1)
              time.sleep(2)
              if edmg1 > fdmg1:
                print ("The spider has dealt more damage than you!")
                print ('\n')
                print ('Game Over')
                ply = input('Do you want to play again?')
              elif fdmg1 < 5:
                print ("You didn't do enough damage to kill the spider, but you manage to escape")
                ply = input('Do you want to play again?')
              else:
                print ("You killed the spider!")
                alive = True
                print ('You have won the game for now ...')
                ply = input('Do you want to play again?')
      else:
        print ("You choose not to fight the spider.")
        print ("As you turn away, it ambushes you and impales you with it's fangs!!!")

  else:
    print ('You decide no to approach the light and go in the opposite direcrtion')
    time.sleep (1)
    print ('\n')
    print ('As you continue to walk you eventually come to the statue of a sphynx')
    print ('The statue suddenly comes to life and leaps landing at your feet ')
    print ('\n')
    print ('The sphynx tells you that if you answer her riddle you may pass but if you dont you will have to fight her')
    print ('\n')
    rid = input('I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?')
    if rid in ['map', 'maps', 'a map', 'a Map', 'Map', 'Maps']:
      print ('\n')
      print ('You have solved the riddle')
      print ('Time rewinds and you wake up like nothing ever happened')
    else:
      print ('\n')
      print ('You have answered wrong you must now fight me!')
      print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print ("              Fighting...                   ")
      print ("   YOU MUST HIT ABOVE A 17 TO KILL THE SPHYNX     ")
      print ("IF THE SPHYNX HITS HIGHER THAN YOU, YOU WILL DIE")
      print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      time.sleep(2)
      fdmg2 = int(random.randint(10, 20))
      edmg2 = int(random.randint(17, 20))
      print ("you hit a", fdmg2)
      print ("the sphynx  hits a", edmg2)
      time.sleep(2)
      if edmg2 > fdmg2:
        print ("The sphynx has dealt more damage than you!")
        print ('\n')
        print ('Game Over')
        ply = input('Do you want to play again?')
      else:
        print ("You killed the sphynx!")
        sword = 1
        print ('\n')
        print ('you gained a sword')
        print ('+ 3 atack')
        print ('\n')
        print ('As you continue throught the maze you come to a fork in the road')
        turn = input('left or right')
        if turn in ['right', 'Right']:
          print ('\n')
          print ('you decide to go right')
          print ('you enter a warp portal')

        else:
          print ('\n')
          print ('you decide to take a left turn and as you adventure you come across a giant tesla coil that immiditaly zaps you and kills you')
          ply = input('Do you want to play again?')





else:
  print ('good bye for now')
  time.sleep(.1)
  print ('\n')
  print ('Game Over')
