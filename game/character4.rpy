#this is the script file for the character 4 script.

#TODO implement Holden
label character4:
    #TODO pick a music track to play here
    play music "audio/Ludum_Dare_32_Track_5.wav" loop fadein 1.0

    show harper neutral at right

    scene holdenhovel with fade
    with Pause(3)

    h "Hey, Holden, are you around?"

    $ holden_not_home = renpy.random.randint(1,100)

    if holden_not_home <= 40:
        $ renpy.pause(delay=2)

        "... Nobody answers."

        $ MET_HOLDEN = False

        return

    show holden neutral at left

    ho "Where else would I be?"

    h sad "Sorry, It’s just- me and [yn] have to make the Stay or Leave decision today, and we were wondering if you had some insight."

    ho "Well, you both already know that I’ve been here all of my life."

    pc "I think we were hoping for a little more information than that."

    ho upset "Fine. I’m warning you though, asking people for their experiences is just going to make your decision harder. There’s a danger in outside influences."

    h upset "..."

    ho neutral "So what do you want to know?"

    menu:
        "What made you choose to stay?":
            $ stay += 1
            call HQ1A1
        "Do you ever regret staying?":
            $ leave += 1
            call HQ1A2

    ho sad "I can’t leave now, not after all of this time. There’s nothing for me out there, and I’m past the point of any interest in going out alone."

    menu:
        "You probably wouldn't have to be alone that long.":
            $ leave += 1
            call HQ2A1
        "I understand.":
            $ stay += 1
            call HQ2A2

    ho upset "Did you talk to Cosette yet?"

    if MET_COSETTE:
        h "Yeah?"

        ho "They don’t get it. They think that I can just up and leave whenever I want to but they don’t understand what it’s like-"

        ho sad "Just forget it. They’re just lucky to still be happy here."
    else:
        h "Not yet, why?"

        ho sad "Nothing. Even if you do talk to them, I doubt you’ll be able to break through the blind optimism."

    ho neutral "Cosette just doesn’t understand all of the things that can go wrong out there."

    ho "There’s always the possibility that you leave and don’t find anything worth looking at for months. Let alone any other people."

    ho sad "I guess that’s one of the real reasons that I stayed. This village is certain, expected, and predictable. I don’t know what happens out there."

    ho "And that’s what anything I try to write is missing. It’s all predictable. No one wants to read a book about daily village life."

    ho "And even if I try to write something different, It’s painfully obvious that I’m out of my depth. anyone could guess what will happen next."

    ho "I chose to stay here because I thought that I needed the stability of being here. But I’ve suffered for that, my writing has suffered for that."

    ho neutral "..."

    ho happy "Ugh. Didn’t mean to talk that long. Why don’t you go ask other people to bare their souls for you instead of me?"

    return

label HQ1A1:
    ho happy "That’s an easy one. I’ve wanted to write books since I started reading them, and I started reading them here. It seemed like there was no reason to leave when I had all I needed right where I am."

    show harper neutral at right

    ho laugh "So what was the point in leaving? I figured that I had everything I needed to write right here. Even if that sentiment was a little misguided."

    ho neutral "Less effort that way too. Didn’t have to find a new place to live, or meet new people  - Or at least, I didn’t think I would have had to meet new people."

    h "What do you mean?"

    ho @ sad "The people here change sometimes. Kids like you choose to leave all the time. Other people come in and settle down. I end up having to introduce myself to new people and say goodbye to others."

    h "Do you know people who chose to leave?"

    ho sad "Yeah, of course I did."

    h "..."

    pc "Care to elaborate?"

    ho neutral "I had a few friends who chose to leave. Some even stayed past their decision and left later. I could never do anything like that."

    h "Why not?"

    return

label HQ1A2:
    ho @ sad "Hah. Yes. Fairly often."

    show harper neutral at right

    pc "Why?"

    ho "I stayed because I wanted to write. It’s hard not to want to write when you're surrounded by all of these amazing books."

    ho "It seemed like there was no point in leaving. I just figured that I had everything I needed to write right here."

    ho sad "I was wrong, of course."

    h @ laugh "What do you mean by “wrong”?"

    ho laugh "Have either of you ever heard of the saying “Write what you know”?"

    ho "Well, I guess you wouldn’t have unless you’re collecting books about writing- which there honestly are not a lot of around here."

    ho upset "I haven’t finished writing anything in years. Nothing I have to say is interesting enough to be worth writing down."

    ho neutral "It’s hard to write books with excitement and intrigue when the most exciting thing that happened to me this week was when one of Bo’s sheep got away and sat outside my place for a little bit."

    ho @ laugh "… or whatever those things are, I’ve read some books about sheep and I’m pretty sure that’s not what that is."

    h "Couldn't you still leave?"

    return

label HQ2A1:
    ho @ upset "I appreciate the sentiment. Nothing is going to change my mind at this point, though."

    return

label HQ2A2:
    ho neutral "Exactly. Too much can go wrong at this point to be worth the risk. "

    return
