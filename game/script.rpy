# The script of the game goes in this file.

#TODO implement a splash screen

#TODO define all characters
define f = Character("Frog")
define h = Character("Harper")

#TODO load all character images
image frog talk = "frog_talk.jpg"


# The game starts here.

#TODO implement the system that keeps track of what dialogue choices the player makes

label character_select:
    play music "audio/Ludum_Dare_30_Track_1.wav" loop fadein 1.0

    h "Hmmm… Cosette’s probably in their studio, Robinson’s down by the canal with her fish traps, Bo’s over there tending his sheep… I guess that leaves Holden off in some corner somewhere."

    h "Who do you want to talk to?"

    #this menu is a chapter select.
    #TODO I need to implement a better menu for which character to talk to
    #TODO implement something that greys out talking to a character once you've done their dialoge
    menu:
        "Robinson" if MET_ROBINSON == False:
            $ MET_ROBINSON = True
            call character1
        "Bo" if MET_BO == False:
            $ MET_BO = True
            call character2
        "Cosette" if MET_COSETTE == False:
            $ MET_COSETTE = True
            call character3
        "Holden" if MET_HOLDEN == False:
            $ MET_HOLDEN = True
            call character4
    jump decision

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    python:
        MET_ROBINSON = False
        MET_BO = False
        MET_COSETTE = False
        MET_HOLDEN = False

    call introduction #use call instead of jump to do a transfer of the control stack as a whole https://www.renpy.org/doc/html/label.html

    call character_select

    return
