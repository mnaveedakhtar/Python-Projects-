################################################################
# LINK: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json.
# COPY ABOVE LINK PASTE ON URL AND THEN CHOOSE "HURDLE 4" FROM BAR LEFT TO WORLD INFO.
################################################################

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    while wall_on_right()==True:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear()==True:
        move()
    turn_left()
    
while not at_goal()==True:
    if wall_in_front():
        jump()
    else:
        move()

    
        
         
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
