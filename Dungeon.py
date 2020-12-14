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
                        if dark_room.lower() == 'a':
                            print ('You hug the wall tightly while slowly making your way along the wall')
                            print ('You eventually get to a door which you open and walk through')
                            print ('On the other side of the door there is a new room filled with spider webs')
                            print ('At the end of the room you see a door covered in spiderwebs')
                            while True:
                                spider_room = input('What do you do?\n[A: Make a run for the door]\n[B: Slowly sneak through the room]')
                                if spider_room.lower() = 'a':
                                    print ('You start running hoping that you will get to the door before anything horrible happens')
                                    print ('While running you acedentaly trip on something')
                                    print ('You quickly turn around to see what you tripped on')
                                    print ('You turn pale as you see that the thing that you had tripped on was a corpse covered in spiderwebs')
                                    print ('Suddenly spiders start crawling out of the spiderwebs surrounding you')
                                    print ('They are headed straight for you')
                                    spiders = input ('What do you do?\n[A: Get up and run towards the door]\n[B: Try to fight back]')
                                    while True:
                                        if spider.lower() = 'a':
                                            print ('You quickly get back on your feet and start running towards the door')
                                            print ('When you get to the door you start trying to open it but it is stuck')
                                            print ('You feel things starting to crawl up your legs')
                                            print ('You look down and see thousands of spiders crawling up your legs')
                                            print ('They start biting you with their poisonous fangs')
                                            print ('You fall to the ground, dead from the high amount of poison injected into your body')
                                        elif spider.lower() = 'b':
                                            print ('You quickly look around for something to fight back with')
                                            print ('You spot a flamethrower just laying on the ground besides you')
                                            print ('You pick it up and start burning all of the spiders but they do not stop')
                                            print ('The now bruning spiders start crawling on you, burning your cloths and skin')
                                            print ('You die from bruning alive')
                                
                        elif dark_room.lower() == 'b':
                            print('You walk straight out into the dark room not knowing what could be there')
                            print('After a few steps you suddenly step out into nothing and fall down a dark pit')
                            print('When you reach the bottom you get impaled by spikes and die')
                            print('Guess you will just have to restart')

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
        print("You make the smart decision to not walk into the dungeon and leave")
        break

    else:
        print('Please choose one of the options!\n-------')
        continue

