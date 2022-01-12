#this is the script file for the character 3 script.

#TODO implement Cosette
label character3:
    #TODO pick a music track to play here
    play music "audio/Ludum_Dare_30_Track_5.wav" loop fadein 1.0


    scene workshop with fade
    with Pause(3)

    show harper neutral at right

    c "Give me just a second, I need to pin this fabric."

    Pause(2)

    show cosette neutral at left

    c happy "Harper! [yn]! Good to see you!"

    c @ laugh "Did you decide to leave? Do you need some traveling clothes? I’m a little bit under capacity right now, so I can probably get you sketches by tonight and some new clothes by the day after tomorrow."

    pc "Actually, we need some advice on the decision to stay or leave, and we hoped you could talk us through how you made your decision?"

    c neutral "Ah hah! Did you talk to Holden already?"

    if MET_HOLDEN:
        h sad "Yeah..."

        c @upset "Let me guess, it was like pulling teeth."

        pc "Exactly."

        c "Oh Holden. He used to tell me that he’d write shelves of books. Now he’s stuck and unhappy. He won’t even talk about his ideas anymore."

        c "He’s not happy here, but he won’t let himself decide to try something new."
    else:
        h @ sad "No…?"

        c "Ah. You should probably talk to him."

        c sad "Just, when you talk to him, keep in mind that he could choose to leave at any time. He’s stubborn and won’t admit to himself he’s making no progress on his books just sitting around."

    h neutral

    c neutral "Anyway, like Holden, I chose to Stay."

    c "I had some friends growing up who really wanted to get out there and find somewhere in the Library to call their own, to find their place in it."

    c "I never really felt that way. I didn’t have a great desire to go out into the rest of the Library and travel with no clear goal in sight, figuring it out as I went."

    c @ happy "There’s probably a section somewhere that’s all about fashion, with books and books about different time periods and designers and styles."

    c "That section could be 3 days from here or 3 months from here or 3 years from here. That’s just the nature of the Library, with random organization of sections."

    c @ sad "And I could go chase that section, but I wouldn’t be happy chasing it. What brings me joy in the world isn’t pursuing some idea, but actually designing and creating clothes!"

    c @ happy "I get to do that every day here. I get to make clothes that people wear - I made the clothes you’re both wearing. I get to work with people to develop what they want to wear, and I love that!"

    c "So yeah. That’s why I chose to stay."

    h happy "That’s really nice!"

    menu:
        "What about the people? Don’t you miss your friends who left?":
            $ leave += 1
            call CQ1A1
        "Wait, you’ve been able to be creative without leaving?":
            $ stay += 1
            call CQ1A2
    h neutral
    c neutral

    pc "Do you ever feel like you need to leave to find something new?"

    c "The Library’s a huge place. Everyone understands that, but I don’t think people really get it."

    c laugh "I don’t think I’ll ever need to find something new. At most, when I’m really feeling bereft of new ideas, I’ll pick a direction and do a day trip."

    c happy "The amount of books you can find within a three-hour radius of here is insane. It might all be the SPECULATIVE FICTION: AGRICULTURE section, but there’s a lot of variety."

    c "I don’t think everyone’s like me though. I enjoy reading a lot about a topic, finding interesting little niches and corners."

    c "For me, that means I’ll probably focus on this section forever. But I know a lot of people - Robinson and Bo, for example - can’t stand reading only from one section. They want variety, they want to read about a bunch of wildly different things."

    menu:
        "You really never get bored of this section?":
            $ leave += 1
            call CQ2A1
        "What's it like staying in one place for so long?":
            $ stay += 1
            call CQ2A2

    c neutral "People come and leave, but I’ll carry the memories of time spent with people I care about, and I get to meet new people all the time."

    c @ sad "I once met someone who was traveling the library trying to find everything about the Irish literary revival."

    c "Or at least I think it was the Irish literary revival… I can’t remember exactly, he only stayed a couple of nights."

    c @ happy "Anyway, he told me that this poet once said \"There are no strangers here, only friends you haven’t yet met.\""

    h "Oh wow. Do you know who the poet was?"

    c @ sad "Yates.. Yeets… I can’t remember…"

    c "I guess that’s how I look at the Library. Everyone’s someone, and I want to meet them."

    pc "Huh..."

    c @ sad "Where did this start?..."

    c @ happy "Oh yes, you were making your decision soon."

    c neutral "If I had one real piece of advice - not the rambling I was doing - it would be to make your decisions separately."

    c @ upset "I just don’t want one of you to end up like Holden, stubbornly doing the opposite of what would make them happy."

    c "If you decide separately, you won't."

    c laugh "On a bit of a brighter note, if one of you decides to leave, remember to stop by my shop! I can get you all set up with some clothes that’ll last."

    H happy "Will do!"

    return

label CQ1A1:

    c upset "Of course! A lot of my friends from when I was your age decided to leave. Most of them never came back."

    h sad

    c sad "It’s hard, not knowing what happened to them, it they’re okay or if…"

    c "Yeah. I miss them."
    return

label CQ1A2:
    c laugh "Yes! A lot of people romanticize creativity, make it something that only happens due to divine inspiration, something that must be sought after."

    c neutral "I don’t think about creativity like that. It doesn’t require a hero’s journey to create something wonderful."

    c @ happy "Creativity comes from actually creating art. The more you create things, the better you are at the act of creation. Taking that first step, creating the first thing, might feel like an insurmountable obstacle."

    c "But if you don’t take that first step, you won’t create anything."

    h @ laugh "Huh. I never thought about it like that."

    return

label CQ2A1:
    c laugh "I don’t!"

    c happy "Maybe that means I’m a little bit boring, but I’m happy."

    c "I get to make things for people I care about. Sure, they may eventually leave, but that’s okay. It’s a little bittersweet when they leave, but if leaving is what’s best for someone, then they shouldn’t force themself to stay."

    return

label CQ2A2:
    c neutral "Oh, it’s a little weird. People come and go, sometimes staying for days, and sometimes decades."

    c happy "But I get to know them while they’re here. It might be sad to see them go, but I don't want to see people I care about force themselves to stay when it wouldn’t be the best for them."

    return
