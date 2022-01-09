#this is the introduction
label introduction:

    play music "audio/Ludum_Dare_30_Track_1.wav" loop fadein 1.0

    define pc = Character("[yn]")

    scene black

    python:
        yn = renpy.input("What is your name?", length=32)
        yn = yn.strip()

        if not yn:
             yn = "... c'mon, pick an actual name"

    show text "Your name is [yn]."
    with Pause(2)

    hide text with fade
    with Pause(1)

    show text "Your choices matter." with fade
    with Pause(2)

    hide text with fade
    with Pause(1)


    scene house evening with fade

    # This shows a character sprite.
    show mom neutral at left

    m "My father used to tell me that someday, he’d find the front desk."

    m "You know how in every book when they describe a library, there’s always a front desk?"

    m "My father was convinced that in this Library, the one he was born in and died in, somewhere was the front desk. At that desk, there would be a librarian."

    m "I think he hoped they would be able to explain why the Library we live in is so different from anything described in any of the books."

    show mom sad at left

    m "I don’t know what he wanted the answer to be."

    show mom neutral at left

    m "He never found the front desk. I always thought that the problem was whoever made the library didn’t have a “front” place for the desk to be."

    m "There’s no “front” in an infinite library."

    show mom happy at left

    m "Front. Front front front. Frooont. Funny word, starts to look like gibberish after a bit."

    m "Anyway, tomorrow you get to make the big decision - are you going to stay in our community in the SPECULATIVE FICTION: AGRICULTURE section, or go explore the rest of the Library?"

    pc "I don’t know, I haven’t really decided yet."

    show mom neutral at left

    m "That’s okay! It was scary when I had to decide. I stayed, and I’ll never regret that. But it’s your decision! I’ll miss you, but if you decide to leave that’s okay."

    pc "Thanks, mom."

    show mom happy at left

    m "Why don’t you sleep on it, and in the morning talk to Harper? You and her could go talk to some people who stayed, and some who left."

    pc "Yeah! Harper'll have a idea of who'd be good to talk to."

    scene house day with fade

    show harper happy at right

    h "Hello [yn]! Hello Alex!" #TODO tentatively named the mom alex.

    pc "Hey Harper!"

    show mom happy at left

    m "Hello Harper! [yn] still doesn't know if they want to Stay or Leave."

    h "Yeah... I've been having trouble deciding also."

    show mom neutral at left

    m "Well, are you leaning one way or the other?"

    show harper sad at right

    h "Not really, it's just - I just need to think about it more"

    m "Well, what if you and [yn] go talk to some people who’ve made the choice before? I know Bo’s in town this week, and you can probably find Robinson down at the canal."

    h "Yeah..."

    show harper neutral at right

    h "Yeah that sounds like a good idea. We could probably talk to Cosette and Holden as well."

    m "Well, the day is still young, plenty of time to go talk to them before your decision tonight."

    jump character_select
