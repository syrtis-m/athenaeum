# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define f = Character("Frog")

# The game starts here.

#TODO implement the system that keeps track of what dialoge choices the player makes

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg meadow

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show frog talk at left

    # These display lines of dialogue.

    f "AH"


    #this menu is a chapter select.
    #TODO I need to implement a better menu for which character to talk to
    #TODO implement something that greys out talking to a character once you've done their dialoge
    menu:
        "chracter 1":
            call character1
        "character 2":
            call character2
        "character 3":
            call character3
        "character 4":
            call character4



    show frog talk at left
    f "this is the end"

    # This ends the game.

    #TODO implement the system that checks what ending it needs to show, and then calls the right script for it.

    return
