label decision:
    #TODO implement the system that checks what ending it needs to show, and then calls the right script for it.
    #TODO implement decision

    #TODO remove this testing stuff.
    "Stay [stay]"
    "Leave [leave]"

    scene town center day with fade
    with Pause(1)

    show harper neutral at center

    h "Okay, we’ve talked to basically everyone then."

    h happy "It’s weird to be saying this, but I guess we have to make our decision now?"

    pc "Harper I-"

    h neutral "Yeah?"

    pc "I was thinking, and.. well… Holden was kinda bitter but he was right that we have to make our decision separately."

    show harper upset at center

    pc "I know you don’t want to lose our friendship, but it’d be worse if we ended up choosing something one of us hated."

    h sad "Oh… Yeah um. I,"

    h "I guess yeah. I thought we’d maybe choose the same thing together but yeah I guess maybe thats for the better."

    h "Yeah, okay."

    pc "You know you’re my best friend, right? I’m not suggesting this to abandon you."

    h @ happy "Yeah I know, I just."

    h "We’ve done everything together since we were kids. And I don’t want to lose that."

    h neutral "But, I guess if we ended up choosing to Stay or Leave together and one of us wasn’t happy, that’d be terrible."

    h "Yeah, alright, um. How about I go over to the canal, and you go over to your house, and we both write our choice down, and then when we’re done we come back out here?"

    pc "Yeah, that sounds good."

    scene house day with fade

    show mom neutral at center

    m "Oh, have you finished talking to everyone?"

    pc "Yeah. Um, Harper and I are making our decisions separately now."

    m @ happy "Oh, that’s a good idea!"

    menu:
        m "Are you going to Stay in our community and find a role here, or Leave and find your place in the rest of the library?"
        "Stay":
            scene black with fade
            with Pause(3)

            call ending_stay
        "Leave":
            scene black with fade
            with Pause(3)
            call ending_leave

    show text "Made by syrtis, K.O. and Villain." with fade
    with Pause(3)

    return
