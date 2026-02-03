#GhostGame.py


from random import randint
print ("Cheater ba yarn?")
feeling_brave = True
score = 0

while feeling_brave:
    ghost_door = randint (1,3)
    print ("Three doors ahead...")
    
    print ("A cheater behind one")
    
    print ("Which door to open?")
    
    door = input ("1, 2, or 3? ")
    door_num = int (door)
    
    if door_num < 1 or door_num > 3:
        print ("Invalid door number. 1 , 2, or 3 lang.")

    if door_num == ghost_door:
        print ("BOO! May iba na siya!")
        feeling_brave = False
    else:
        print ("Wew, Pwede pa.")
        print ("Next room tol")
        score = score + 1
    

print ('Run Away!')
print ('aray mo cho, You scored', score, 'points')

