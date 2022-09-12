################################################################
# LINK: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json.
# COPY ABOVE LINK PASTE ON URL AND THEN CHOOSE "HURDLE 1" FROM BAR LEFT TO WORLD INFO.
################################################################

def turn_right():
    turn_left()
    turn_left()
    turn_left()

move()
turn_left()
move()
turn_right()
move()
turn_right()
move()

for i in range(0,5):
    turn_left()
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()


    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
