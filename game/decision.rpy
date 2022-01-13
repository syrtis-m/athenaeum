label decision:
    #TODO implement the system that checks what ending it needs to show, and then calls the right script for it.
    #TODO implement decision

    #TODO remove this testing stuff.
    "Stay [stay]"
    "Leave [leave]"

    scene town center day with fade
    with Pause(1)

    show harper neutral at middle

    h "Okay, we’ve talked to basically everyone then."

    h "It’s weird to be saying this, but I guess we have to make our decision now? We have to decide together now."

    pc "Harper I-"

    h "Yeah?"

    pc "I was thinking, and.. well… Holden was kinda bitter but he was right that we have to make our decision separately."

    pc "I know you don’t want to lose our friendship, but it’d be worse if we ended up choosing something one of us hated."

    h "Oh… Yeah um. I,"

    h "I guess yeah. I thought we’d maybe choose the same thing together but yeah I guess maybe thats for the better."

    h "Yeah, okay."

    pc "You know you’re my best friend right, I’m not suggesting this to abandon you."

    h "Yeah I know, I just."

    h "We’ve done everything together since we were kids. And I don’t want to lose that."

    h "But, I guess if we ended up choosing to Stay or Leave together and one of us wasn’t happy, that’d be terrible."

    h "Yeah, Alright, um. How about I go over to the canal, and you go over to your house, and we both write our choice down, and then when we’re done we come back out here?"

    pc "Yeah, that sounds good."

    scene house day with fade

    show mom neutral at middle

    m "Oh, have you finished talking to everyone?"

    pc "Yeah. Um, Harper and I are making our decisions separately now."

    m "Oh, that’s a good idea!"

    menu:
        m "Are you going to Stay in our community and find a role here, or Leave and find your place in the rest of the library?"
        "Stay":
            jump ending_stay
        "Leave":
            jump ending_leave


    return #replace with jumping to either the stay or leave ending
