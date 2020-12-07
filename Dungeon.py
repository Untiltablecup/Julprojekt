import string

while True:
    start = input('Do you want to enter the dungeon?\n[Y/N]\n>')
    if start.lower() == 'y':
        while True:
            print('You open the big old wooden door')
            print('Behind it is a staircase leading down into the deep dark dungeon')
            print('You start walking down the old and broken staircase')
            print('When you get to the bottom of the staircase you enter a small stone room lit with torches on the walls and with two doors')
            while True:
                door = input('Which one do you enter?\n[Left/Right]\n>')
                if door.lower() == 'left':
                    print ('You choose to open the left door')
                    print ('You open and walk through')
                    print ('When you enter the room the doors slams shut behind you')
                    print ('It is a very dark room and you can not see anything')
                    while True:
                        dark_room = input('What do you do?\n [A: You walk along the wall]\n [B: You walk straight into the dark room]\n>')
                        if dark_room.lower == 'a':
                            print ('You hug the wall tightly while slowly making your way along the wall')
                            print ('You eventually get to a door which you open and walk through')
                        elif dark_room.lower == 'b':
                            print('You walk straight out into the dark room not knowing what could be there')
                            print('After a few steps you suddenly step out into nothing and fall down a dark pit')
                            print('When you reach the bottom you get impaled by spikes')

                        else:
                            continue

                elif door.lower() == 'right':
                    print("ja")
                else:
                    print('You choose not to try any of the doors')
                    print('You instead look around trying to see if there is anything hidden in the room')
                    print('But you find nothing')
                    print('You decide to try one of the doors instead\n-------')
                    continue

    elif start.lower() == 'n':
        print("You give up and leave the dungeon")
        break

    else:
        print('Please choose one of the options!\n-------')
        continue

