# The script of the game goes in this file.

#TODO define all characters
define f = Character("Frog") #TODO remove frog from game
define m = Character("Mom")
define h = Character("Harper")
define r = Character("Robinson")
define b = Character("Bo")
define c = Character("Cosette")
define ho = Character("Holden")

#TODO load all character images
image frog talk = "frog_talk.jpg"

label splashscreen:
    scene black
    with Pause(1)

    show text "Vertical Slice" #TODO replace with game studio name https://www.renpy.org/doc/html/splashscreen_presplash.html
    with Pause(2)

    hide text with fade
    with Pause(1)

    return


# The game starts here.

#TODO implement the system that keeps track of what dialogue choices the player makes

label character_select:
    play music "audio/Ludum_Dare_30_Track_6.wav" loop fadein 1.0

    h "Hmmm… Cosette’s probably in their studio, Robinson’s down by the canal with her fish traps, Bo’s over there tending his sheep… I guess that leaves Holden off in some corner somewhere."



    #TODO consider putting something in so it auto-goes to the decision scene if needed.

    #this menu is a chapter select.
    menu:
        "Who do you want to talk to?"

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

        "Decision" if ((MET_ROBINSON == True) and (MET_BO == True)) and ((MET_HOLDEN == True) and (MET_COSETTE == True)):
            jump decision

    jump character_select

label start:

    python:
        #INITIALIZING FLAGS
        MET_ROBINSON = False
        MET_BO = False
        MET_COSETTE = False
        MET_HOLDEN = False

        #INITIALIZING DECISION TRACKER SYSTEM
        stay = 0
        leave = 0


    jump introduction

    return
