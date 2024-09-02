from sys import exit
from random import *

def cemetery():
    print("you find yourself in a cemetery")#pretty self explanatory
    print("you look around and see a shovel besides a grave")
    print("will you grab the shovel and dig or leave it alone?")#the choice options 
    choice = input("> ")
    if "dig" in choice:#if you dig the grave you get killed by the corpse
        dead("the corpse in the grave wakes up and chokes you to death for forsaken it's resting place")
    else:
        print("you hear a voice say:'you did well little one, be rewarded with treasure!'")#you get teleported to the gold room if you wait
        gold_room()
    


def garden():
    print("you find yourself in a room with a beautiful garden")
    print("you see a bench beneath a tree and another door behind them")
    print("what do you wish to do?")
    choice = input("> ")
    if "sit" in choice: #if they sit they die 
        dead("you sit on the bench and you feel sharp things under you before you're eaten by a bench mimic")
    elif "door" in choice: #they go to the cemetery
        cemetery()
    else:
        garden("i dont know what that means")#resets the room incase they don't type something of the above
def gold_room(): 
  print("This room is full of gold. How much do you take?") 
  choice = input("> ")
  #if "0" in choice or "1" in choice:               Não faz sentido com a pergunta.
  how_much = int(choice)
  #else: 
    #dead("Man, learn to type a number.") 
  if how_much < 50:
    print("Nice, you're not greedy, you win!") 
    exit(0)
  elif how_much > 50: 
    dead("You greedy bastard!")
  else: 
    dead("Man, learn to type a number.") 

def bear_room():
  print("There is a bear here.")
  print("The bear has a bunch of honey.")
  print("The fat bear is in front of another door.")   
  print("How are you going to move the bear?") 
  bear_moved = False
  while True: 
    choice = input("> ")
    if choice == "take honey":
     dead("The bear looks at you then slaps your face off.")
    elif choice == "taunt bear" and not bear_moved: 
      print("The bear has moved from the door.")
      print("You can go through it now.") 
      bear_moved = True
    elif choice == "taunt bear" and bear_moved:
      dead("The bear gets pissed off and chews your leg off.") 
    elif choice == "open door" and bear_moved: 
      gold_room()
    else: 
      print("I got no idea what that means.")

def cthulhu_room(): 
  print("Here you see the great evil Cthulhu.(and a door on the corner of the room)")#new option
  print("He, it, whatever stares at you and you go insane.") 
  print("Do you flee for your life, eat your head or go through the door?")#new path the player can take
  choice = input("> ")
  if "flee" in choice: 
    start()
  elif "head" in choice: 
    dead("Well that was tasty!")
    #new code
  elif "door" in choice:
    garden()
  else:
    cthulhu_room()

def bridge_room():
    
  print("You see a long wooden bridge")
  print("Before the bridge there is a sword")
  print("What do you do?")
  sword = False #if you don't get the sword you do less dmg
  while True:
    choice = input("> ")
    guardHP = 10
    playedHP = 10
    if "grab sword" in choice:
      sword = True
      print("What do you do?")
    #START COMBAT
    elif "cross the bridge" in choice:
      print("As you cross the brige you see a guard in the middle of the bridge")
      print("He stops you and is read to fight")
      print(" O |")
      print("/|\T ")
      print("/ \.")
      while True:
        print(f"Vida atual: {playedHP}")
        print(f"Vida atua do guarda: {guardHP}")
        print("What do you do?")
        choice2 = input("> ")#this is a combat system(i don't understand it to be honest)
        if "attack" in choice2:
          
          playedHit = randint(0,1)
          guardHit = randint(0,1)
          guardDef = randint(0,1)
          
          if sword == True:
            if guardDef == 1:
              print("Guard defended")
              guardHP -= 0
              playedHP -= 0
            elif playedHit == 1:
              print("You hit the guard")
              guardHP -= 2
              if guardHit == 1:
                print("The guard hit you")
                playedHP -= 2
            elif guardHit == 1:
                print("The guard hit you")
                playedHP -= 2
            else:
                print("Both you and the guard missed")
                
          else:
            if guardDef == 1:
              print("Guard defended")
              guardHP -= 0
              playedHP -= 0
            elif playedHit == 1:
              print("You hit the guard")
              guardHP -= 1
              if guardHit == 1:
                print("The guard hit you")
                playedHP -= 2
            elif guardHit == 1:
                print("The guard hit you")
                playedHP -= 2
            else:
                print("Both you and the guard missed")
              
        elif "defend" in choice2:
          playedHP -= 0
          
        elif "heal" in choice2:
          guardHit = randint(0,1)
          
          if guardHit == 1:
            playedHP -= 1
          else:
            playedHP += 2
            
        else:
          print("I got no idea what that means.")
        #END COMBAT  
        
        if playedHP == 0:
          dead("The guard kills you")
        if guardHP == 0:
          print("You killed the guard and crossed the bridge.")#killing the guard takes you to the treasure room too
          gold_room()
          
    else:
      print("I got no idea what that means.")
      
def dead(why):
  print(why, "Good job! You are dead") #changed the dialog to make it clearer you died 
  exit(0)

def start(): 
  print("You are in a dark room.")
  print("There is a door to your right, left and forward.") 
  print("Which one do you take?")
  choice = input("> ")
  if choice == "left": 
    bear_room()
  elif choice == "right": 
    cthulhu_room()
  elif choice == "forward": 
    bridge_room()
  else: 
    dead("You stumble around the room until you starve.")

start()
