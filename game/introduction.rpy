#this is the introduction
label introduction:

    #TODO implement introduction

    play music "audio/Ludum_Dare_30_Track_1.wav" loop fadein 1.0

    define pc = Character("[povname]")

    scene black

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
             povname = ""

    show text "Your name is [povname]."
    with Pause(2)

    hide text with fade
    with Pause(1)

    show text "Your choices matter." with fade
    with Pause(2)

    hide text with fade
    with Pause(1)


    scene house evening with fade

    # This shows a character sprite.

    show frog talk at left

    # These display lines of dialogue.

    f "AH"

    jump character_select
