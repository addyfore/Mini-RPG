#!/bin/python3
import time
import sys

#variable checking if this is the first time the player can type a move
firstMove = 0
#an inventory, which is initially empty
inventory = []
#amount of times one has been in the bedroom(For doll scenario)
bedroomCount = 0
def showInstructions():
  #print a main menu and the commands
  type_out('Commands:', 0.05)
  time.sleep(1)
  print('')
  type_out(' go [north, south, east, west]', 0.025)
  time.sleep(0.25)
  print('')
  type_out(' get [item in room]', 0.025)
  time.sleep(0.25)
  print('')
  type_out(' inspect [area/room, item]', 0.025)
  time.sleep(0.25)
  print('')
  type_out(' inventory', 0.025)
  time.sleep(0.25)
  print('')
  type_out(' commands', 0.025)
  time.sleep(1)
  print('')
  print('')

def showStatus():
  #print the player's current status
  if currentRoom != 'under the bed':
    print('You are in the ' + currentRoom + '.')
  else:
      print('You are ' + currentRoom)
  #print the current inventory
#   print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'] + '.')

  
def type_out(string, t):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(t)
  


#a dictionary linking a room to other rooms
rooms = {


            'kitchen' : {
                  'south' : 'living room',
                  'east' : 'bedroom',
                  'north' : 'garden',
                  'item' : 'dish'
                },
                
            'hallway' : {
                  'west' : 'living room',
                  'east' : 'library'
                },
            
            'library' : {
                    'west' : 'hallway',
                    'item' : 'quill'
                },
            'living room' : {
                    'north' : 'kitchen',
                    'east' : 'hallway',
                    'item' : 'picture'
                },
            'bedroom' : {
                    'west' : 'kitchen',
                    'item' : 'doll'
                },
            'garden' : {
                    'south' : 'kitchen',
                    'item' : 'diary'
                },
            'under the bed' : {
                }
         }

#start the player in the living room.
currentRoom = 'living room'
dollCount = 0
time.sleep(0.5)
type_out('The House.', 0.05) 
print('')
type_out('==============', 0.05)
print('')
time.sleep(1)
type_out('Current working features:', 0.05)
time.sleep(1)
print('')
type_out('-Moving north, south, east, and west', 0.05)
time.sleep(1)
print('')
type_out('-Picking up items', 0.05)
time.sleep(1)
print('')
type_out('-Inspecting items(still needs work)', 0.05)
time.sleep(2)
print('')
print('')

#what happens if the player has the doll and is in the bedroom for the first time
def doll_scenario(curRoom) :
    print('There is someone in the room with you.')
    print('Give her the doll?')
    answer = input('y/n: ')
    #if the player gives the girl a doll
    if answer == 'y' :
        for i in range(len(inventory)):
            if inventory[i] == 'doll':
                del inventory[i]
        type_out('She is grateful.', 0.05)
        time.sleep(1)
        print('')
        type_out('She wants you to follow her under the bed.', 0.05)
        time.sleep(1)
        print('')
        type_out('Follow?', 0.05)
        print('')
        answer3 = input('y/n: ')
        if answer3 == 'y' :
            curRoom = 'under the bed'
        elif answer3 == 'n' :
            time.sleep(2)
            type_out('She is angry.', 0.1)
            time.sleep(1)
            print('')
            type_out('Run Away?', 0.05)
            time.sleep(1)
            print('')
            answer4 = input('y/n: ')
            if answer4 == 'y' :
                time.sleep(1)
                type_out('You run to the kitchen. ', 0.05)
                time.sleep(0.5)
                type_out('Do not go back.', 0.1)
                time.sleep(1)
                print('')
                print('')
                curRoom = 'kitchen'
            elif answer4 == 'n':
                time.sleep(1)
                print('You decide to run.')
                curRoom = 'kitchen'
    #if the player refuses to give the girl a doll
    elif answer == 'n' :
        time.sleep(2)
        type_out('She is angry.', 0.1)
        time.sleep(1)
        print('')
        type_out('Run Away?', 0.05)
        time.sleep(0.5)
        print('')
        answer2 = input('y/n: ')
        if answer2 == 'y' :
            time.sleep(1)
            type_out('You run to the kitchen.', 0.05)
            time.sleep(0.5)
            type_out('Do not go back.', 0.1)
            curRoom = 'kitchen'
            
    return curRoom
    
    
def bed_scenario() :
    type_out('...', 0.75)
    time.sleep(1)
    print('')
    type_out('You follow her under the bed.', 0.05)
    time.sleep(1)
    print('')
    type_out('It is dark.', 0.05)
    time.sleep(1)
    print('')
    showInstructions()
    showStatus()

while True:
  if currentRoom == 'bedroom' and 'doll' in str(inventory) and bedroomCount == 1 :
    currentRoom = doll_scenario(currentRoom)
    dollCount = 1
    if currentRoom == 'under the bed':
        inventory = []
        bed_scenario()
  if firstMove == 0:
    showInstructions()
    firstMove += 1
  showStatus()


  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()
  
  while move[0] != '':
      #if they type 'commands' first
      time.sleep(1)
      print('')
      if move[0] == 'commands':
          showInstructions()
          break
      #if they type 'inventory' first
      if move[0] == 'inventory':
          print('')
          time.sleep(1)
          type_out('Inventory: ' + str(inventory), 0.05)
          time.sleep(1)
          print('')
          print('')
          break
      #if they type 'go' first
      if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            if move[1] == 'east' and dollCount == 1:
                if currentRoom == 'kitchen':
                    time.sleep(1)
                    type_out('It\'s locked.', 0.25)
                    time.sleep(1)
                    print('')
                    print('')
          #set the current room to the new room
            else:
                currentRoom = rooms[currentRoom][move[1]]
                type_out('You move to the ' + currentRoom + '.', 0.05)
                print('')
                print('')
                time.sleep(1)
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
        if currentRoom == 'bedroom' :
            bedroomCount += 1
        break  
    
      #if they type 'get' first
      if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
          #add the item to their inventory
          inventory += [move[1]]
          #display a helpful message
          type_out(move[1] + ' got!', 0.05)
          time.sleep(1)
          print('')
          print('')
          #delete the item from the room
          del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
          #tell them they can't get it
          print('Can\'t get ' + move[1] + '!')
        break
          
      if move[0] == 'inspect' and (move[1] == 'item' or move[1] == 'area' or move[1] == 'room'): 
          if move[1] == 'item':
              type_out('Which item will you inspect?', 0.05)
              print('')
              answer = input('>')
              if answer == 'picture':
                  if answer in inventory:
                    print('')
                    time.sleep(1)
                    type_out('You inspect the picture.', 0.05)
                    time.sleep(1)
                    print('')
                    type_out('It\'s a portrait of a small family.', 0.05)
                    time.sleep(1)
                    print('')
                    type_out('A mother sits with her child, and the father stands behind.', 0.05)
                    time.sleep(1)
                    print('')
                    type_out('It\'s ripped at the corner, concealing the father\'s face.', 0.05)
                    time.sleep(1)
                    print('')
                    type_out('On the back, there is writing.', 0.05)
                    time.sleep(1)
                    print('')
                    type_out('     "Crockett Family, 1816"', 0.05)
                    print('')
                    print('')
                    time.sleep(2)
                    break
                  elif answer in rooms[currentRoom]['item']:
                      print('')
                      type_out('You glance at the picture on the ground.', 0.05)
                      time.sleep(1)
                      print('')
                      type_out('The frame is broken and there are glass', 0.05)
                      print('')
                      type_out('shards spread out around it.', 0.05)
                      time.sleep(1)
                      print('')
                      type_out('There is a small door on the wall where', 0.05)
                      print('')
                      type_out('the picture used to hang.', 0.05)
                      time.sleep(1)
                      print('')
                      print('')
                      break
                  else:
                      type_out('You don\'t have that.', 0.05)
                      time.sleep(1)
                      print('')
                      print('')
                      break
              elif answer == 'dish':
                  if answer in inventory:
                      print('')
                      time.sleep(1)
                      type_out('You inspect the dish.', 0.05)
                      time.sleep(1.75)
                      print('')
                      type_out('It has some kind of sauce caked on it.', 0.05)
                      time.sleep(1)
                      print('')
                      print('')
                  elif answer in rooms[currentRoom]['item']:
                      print('')
                      time.sleep(1)
                      type_out('You get closer to the dish on the table.', 0.05)
                      time.sleep(1)
                      print('')
                      type_out('Flies are swarming it, claiming the', 0.05)
                      print('')
                      type_out('leftover food as their own.', 0.05)
                      time.sleep(1)
                      print('')
                      print('')
              elif answer == 'doll':
                  time.sleep(0.75)
                  type_out('...', 0.75)
                  print('')
                  time.sleep(1)
                  type_out('You don\'t want to look at the doll right now.', 0.1)
                  time.sleep(1)
                  print('')
                  print('')
                  break
              elif answer == 'diary':
                  print('')
                  time.sleep(0.5)
                  type_out('The front cover is sleek black leather.', 0.05)
                  time.sleep(1)
                  print('')
                  type_out('Written in golden ink are the words "Your Diary."', 0.05)
                  time.sleep(1)
                  print('')
                  type_out('The pages are all blank, but you get the feeling something', 0.05)
                  print('')
                  type_out('might happen if you write in it.', 0.05)
                  time.sleep(1)
                  print('')
                  print('')
                  break
              elif answer == 'quill':
                  print('')
                  time.sleep(0.5)
                  type_out('You inspect the quill.', 0.05)
                  time.sleep(1)
                  print('')
                  type_out('It appears to be the feather of a swan.', 0.05)
                  time.sleep(1)
                  print('')
                  type_out('There is still ink on the tip.', 0.05)
                  time.sleep(1)
                  print('')
                  print('')
                  break
          if move[1] == 'area' or move[1] == 'room':
            time.sleep(1)
            print('')
            if currentRoom == 'kitchen':
                type_out('You inspect the kitchen.', 0.05)
                time.sleep(1)
                print('')
                type_out('There are flies everywhere.', 0.075)
                time.sleep(1)
                print('')
                type_out('The cabinets have been raided, and open', 0.05)
                print('')
                type_out('cans litter the floor.', 0.05)
                time.sleep(1)
                print('')
                type_out('There is a bedroom to the east, the', 0.05)
                print('')
                type_out('living room to the south, and the garden', 0.05)
                print('')
                type_out('to the north.', 0.05)
                time.sleep(1)
                print('')
                print('')
                break
            if currentRoom == 'hallway':
                type_out('You inspect the hallway.', 0.05)
                time.sleep(1)
                print('')
                type_out('The paint on the walls seems to peel away', 0.05)
                print('')
                type_out('as you walk past it.', 0.05)
                time.sleep(1)
                print('')
                print('')
                break
            if currentRoom == 'library':
                type_out('You inspect the library.', 0.05)
                time.sleep(1)
                print('')
                print('')
                break
            if currentRoom == 'living room':
                type_out('You inspect the living room.', 0.05)
                time.sleep(1)
                print('')
                print('')
                break
            if currentRoom == 'bedroom':
                type_out('You inspect the bedroom.', 0.05)
                time.sleep(1)
                print('')
                print('')
                break
            if currentRoom == 'garden':
                type_out('You inspect the garden.', 0.05)
                time.sleep(1)
                print('')
                print('')
                break
            if currentRoom == 'under the bed':
                type_out('You inspect the darkness.', 0.05)
                time.sleep(1)
                print('')
                print('')
                break
      else:
          time.sleep(0.5)
          type_out('Invalid Command.', 0.05)
          time.sleep(1)
          print('')
          print('')
          break