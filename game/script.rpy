# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Frog")
define h = Character("Harper")

image frog talk = "frog_talk.jpg"

# The game starts here.

#TODO implement the system that keeps track of what dialoge choices the player makes

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    jump introduction

    # scene town day

    jump character_select #go to a menu of what characters to talk to

    jump decision #go to the decision scene -> they should jump to endings from inside this

    #something about how your decisions affected the story should be here

    return

label character_select:
    h "Hmmm… Cosette’s probably in their studio, Robinson’s down by the canal with her fish traps, Bo’s over there tending his sheep… I guess that leaves Holden off in some corner somewhere."

    h "Who do you want to talk to?"

    #this menu is a chapter select.
    #TODO I need to implement a better menu for which character to talk to
    #TODO implement something that greys out talking to a character once you've done their dialoge
    menu:
        "Robinson" if MET_ROBINSON == False:
            $MET_ROBINSON = True
            call character1
        "Bo" if MET_BO == False:
            $MET_BO = True
            call character2
        "Cosette" if MET_COSETTE == False:
            $MET_COSETTE = True
            call character3
        "Holden" if MET_HOLDEN == False:
            $MET_HOLDEN = True
            call character4
    return
