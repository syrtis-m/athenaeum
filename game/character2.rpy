#this is the script file for the character 2 script.

#TODO implement Bo
label character2:

    play music "audio/Ludum_Dare_38_Track_3.wav" loop fadein 1.0

    scene readingroom with fade

    show harper neutral at right

    h "Bo… BO!"

    $ renpy.pause(delay=1)

    show bo laugh at left

    b "Oh sorry! Didn’t see ya there."

    b neutral "What’dya need?"

    if MET_ROBINSON:
        pc "It's the day for our Stay/Leave decision, and we just talked to Robinson and she said you might be a good person to talk to…?"

        b @ happy "Aw, Robinson's lovely"
    else:
        pc "It’s the day for our Stay/Leave decision, and uh, wouldyoutalkaboutyourexperience?"

        b @ laugh "Ah, no need to be nervous!"

    b "Well, I chose to Leave. I didn’t dislike my home community, I just wanted to see more of the Library."

    b "My pa had this book about transhumance. I read it cover to cover more times than I could count when I was your age."

    h laugh "Transhumance? Is that like transhumanism?"

    b @ laugh "Ha! No, transhumanism refers to evolving beyond humanism - “trans” being latin for across, and humanism referring to the human condition."

    b "The “trans” part of transhumance is the same, but “humance” comes from the latin “humus” for ground. Transhumance - across ground."

    h neutral "Ohhhh."

    b "It’s a way of life in which herds of livestock are moved seasonally, with people who tend to the livestock traveling with the herd."

    b "Typically they move between fixed pastures in the summer and winter to take advantage of different weather and to allow vegetation to regrow."

    b @ happy "The people who lived by practicing transhumance have a permanent home, with only the people necessary to maintain the animals traveling with the herd."

    b "My pa raised sheep, and he traveled nomadically, trading the milk or wool to the communities he met on his way."

    b "When he met my mother, he decided to settle down in her community and he decreased the size of his flock to allow him to stay in one place year-round."

    menu:
        "So why leave? You could have stayed in your original village.":
            $ stay += 1
            call BQ1A1 from _call_BQ1A1
        "So why take the sheep with you on your journey?":
            $ leave += 1
            call BQ1A2 from _call_BQ1A2

    b "Transhumance is characterized by how the herd moves between two points depending on the seasons. The seasons in the Library don’t make much sense, so instead I decided to just find a path that would bring me back to my parent’s village once every year or so."

    h upset "So you left just like that? What about your friends?"

    b "Ahhh, yeah. Yeah. My friends at the time mostly decided to stay."

    b @ happy "I don’t blame them, that was just their path and I had mine."

    b "When I’m in town every year or so I’ll go over to their houses and catch up, but y’know, over time we just grew apart."

    show harper sad at right

    b "I know you probably feel like growing apart would be a tragedy, but really it’s something beautiful."

    b @ happy "We had wonderful times together, but now we’re different people than we were then."

    b "I can remember those times fondly, but this way I can live my life."

    menu:
        "Do you ever regret deciding to travel?":
            $ leave += 1
            call BQ2A1 from _call_BQ2A1
        "It must be lonely constantly traveling.":
            $ stay += 1
            call BQ2A2 from _call_BQ2A2

    if MET_ROBINSON:
        b neutral "Though now that I’m thinking of it, you might want to go talk to Robinson - she definitely had a different experience with choosing to leave."

        h happy "Yeah! We’ll definitely go talk to her."

    b @ happy "I know it’s scary to leave behind everything you’ve ever known, but I definitely recommend choosing to leave and explore the library - it really helped me figure out who I wanted to be in life."

    b "You can always come back, and it’s the best time of your life to go explore."

    h neutral "..."

    pc "..."

    b laugh "Well, it’s your decision! Good luck, whatever you choose to do!"

    return

label BQ1A1:
    b sad "Well, I… I didn’t get along with my parents. I loved the sheep and I liked our section, but I would find myself getting in fights with them constantly."

    b "The kind of thing where one person says something, and then the other person bottles it up and up and it explodes out of them a couple of days later."

    b @ upset "That kind of environment was hard for me."

    b "It’d get to be this sort of situation where I could tell one of my parents was upset and was going to blow up later, so I’d be nervous and tense waiting for the explosion."

    b neutral "I love my parents, but I didn’t want to be in that environment all the time. Now I can visit them every time my route passes through, and that’s the best for me, I think."

    return

label BQ1A2:
    b @ happy "Well, I was fascinated by transhumance. I love my sheep - some of them are the grandchildren of the sheep my dad raised when I was little. But I also wanted to get out into the world and away from where I grew up."

    b neutral "The idea of taking my sheep with me, that was the best of both worlds. And this way, I can still see my parents from time to time when my path passes through their community."

    return

label BQ2A1:
    b "No! Not at all. When I was making my decision, I could see the path I would take if I stayed."

    b @ sad "I’d tend the herd, maybe do day trips or week trips to different sections - I always did love the AGRICULTURE: ORANGE CULTIVATION section."

    b "But I also could see that while I might be happy in that life, I’d be much happier traveling and visiting all the different sections."

    return

label BQ2A2:
    b @ sad "Ahhhh, sometimes."

    b "But that’s the price I pay for leaving! It might be lonely from time to time, but I also get to experience so many different sections and talk to so many different people."

    b @ happy "I know that life isn’t for everyone, but I love it."

    return
