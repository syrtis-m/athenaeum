# The script of the game goes in this file.

define m = Character("Mom", image="mom")
define h = Character("Harper", image="harper")
define r = Character("Robinson", image="robinson")
define b = Character("Bo", image="bo")
define c = Character("Cosette", image="cosette")
define ho = Character("Holden", image="holden")


# The game starts here.

#TODO FIND AND REPLACE ’ WITH '

label character_select:
    play music "audio/Ludum_Dare_30_Track_6.wav" loop fadein 1.0

    scene town center day with fade

    show harper neutral at right

    h "Hmmm… Cosette’s probably in their studio, Robinson’s down by the canal with her fish traps, Bo’s over there tending his sheep… I guess that leaves Holden off in some corner somewhere."

    "stay: [stay], leave: [leave]"

    menu:
        h "Who do you want to talk to, [yn]?"
        #TODO add scene transitions.

        "Robinson" if MET_ROBINSON == False:
            $ MET_ROBINSON = True
            pc "Let's talk to Robinson..."
            call character1 from _call_character1

        "Bo" if MET_BO == False:
            $ MET_BO = True
            pc "Let's talk to Bo..."
            call character2 from _call_character2

        "Cosette" if MET_COSETTE == False:
            $ MET_COSETTE = True
            pc "Let's talk to Cosette..."
            call character3 from _call_character3

        "Holden" if MET_HOLDEN == False:
            $ MET_HOLDEN = True
            pc "Let's talk to Holden..."
            call character4 from _call_character4

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
