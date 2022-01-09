#this is the script file for the character 1 chapter.

label character1:

    play music "audio/Ludum_Dare_32_Track_2.wav" loop fadein 1.0

    scene canal with fade
    with Pause(3)

    r "Hey, let me finish up tying this knot…"

    $ renpy.pause(delay=1)

    show robinson neutral at left

    r "Hey, what's up?"

    show harper sad at right

    h "Well, you know, we have to make the Stay or Leave decision today. And ummm…"

    pc "We were hoping you could talk about how you made the decision?"

    r @ sad "Ahhhh. Yeah."

    r "Yeah, why not."

    show harper neutral at right

    r "I chose to Leave. Y’know, my family lived in the NAVAL HISTORY: NEOVIKINGS section, and-"

    h @ laugh "Wait… Neovikings?"

    r @ happy "Yeah. It was a lot less interesting than it sounds. Everyone I knew loved reading about neovikings and building longships and farming and I just couldn’t."

    r "My parents always thought that if they could get me to read the right treatise, I would be hooked. It never worked."

    r @ sad "So I left. I just wanted to go out there and see what else was in the world."

    menu:
        "Was it hard to leave?":
            $ stay += 1
            call RQ1A1 from _call_RQ1A1

        "Sounds like it was pretty easy to leave.":
            $ leave =+ 1
            call RQ1A2 from _call_RQ1A2

    h sad "What happened after you left?"

    r happy "Well, that’s the really important part."

    r @ laugh "I LEARNED ABOUT FISH!"

    r "I traveled for about a year before I found a canal in the NORTH AMERICAN POTTERY 1792-1793 section. I’d never SEEN so much water."

    pc "Wait, are canals rare?"

    r @ laugh "This is the only one I’ve ever seen in the library. You should ask Bo about that -- he’s a nomad so he’d know more than me."

    r "I was fascinated by the fish when I found them. I’d read about fish before, what they eat, how they migrate, what they meant to different people."

    r @ laugh "But never in a million sections did I actually expect to SEE fish in the Library!"

    r "So I camped there for a couple weeks and just watched the fish. You haven’t seen dry reading until you’ve visited the NORTH AMERICAN POTTERY 1792-1973 section. Trust me."

    r neutral "After a while, I packed up and decided to follow the canal - I wanted to find new fish and books about fish instead of pots."

    menu:
        "How long did you follow the canal?":
            $ leave += 1
            call RQ2A1 from _call_RQ2A1
        "What about your family? Did you ever go back?":
            $ stay += 1
            call RQ2A2 from _call_RQ2A2

    r sad "I realized at some point that I’d traveled too long along the canal. Even if I turned around, retraced half a decade of steps, when I finally found my way back, my family wouldn’t be just like I left it."

    r @ upset "My sister could be gone, left on her own journey. My parents could have left for the final journey. Who knows what my childhood friends had done. It would never be the same community as it was when I was your age."

    h sad "Oh... I hadn't thought of that."

    if MET_BO:
        pc "So when did you meet Bo?"

        r laugh "Oh, talked to him already? Bo's such a sweetheart."
    else:
        pc "So why stop here?"

    r neutral "I’d been following the canal for nearly a decade, and had started staying in interesting sections for longer and longer. The one thing that’s true no matter what section of the Library you’re in is that books are heavy."

    r @ happy "I’ve seen all sizes and shapes of books, I’ve seen all sorts of architecture. I’ve even been in sections where instead of shelves books are in piles taller than me. But no matter the section, books are always heavy."

    r "If you want to keep traveling, you can’t do much more than read a little bit and then leave that section behind. Maybe you take a book or two with you, but sooner or later you have to discard those books to make way for new books."

    r "That part of traveling sucked."

    r happy "I met Bo in the PRE-19TH CENTURY ANTARCTIC EXPEDITIONS section - It’s roughly a week upcanal. I’d lived there for a month or two when he came through on his usual route."

    r "He stayed the night there, and we talked about the canal - his sheep like the plants, I like the fish."

    r neutral "It’s easy to talk to people you don’t think you’ll ever see again, and I ended up talking about how it was getting exhausting to leave a section behind."

    r "He told me about this town, how it was right on the canal and was in need of someone to tend the fish."

    r "So I stopped here."

    r "Now I get to tend to the fish, and use what I’ve learned to ensure we don’t damage the ecosystem of the canal."

    r "Every day I get to work with the canal is a good day."

    h "Do you ever think about leaving and traveling more?"

    r @ sad "I couldn’t leave again. I’m not ancient yet, but I’m getting older and I just want to do more than just read a little bit in each section."

    if MET_BO == False:
        r happy "You might want to go talk to Bo. He also chose to leave, but he had a much different experience."

    r sad "Stay or leave. It’s your decision. Just, if you leave, don’t do what I did. Don’t lose where you’re from."

    return


#these are all the labels for the branching dialogue. they must be called, not jumped to
label RQ1A1:
    r sad "No, it was pretty easy to leave."

    r "I was angry, yknow? I wanted to leave and I thought that if I did, I could finally see what’s out there."

    r "I thought that I’d finally see what rest of the Library was like, and I could find what I loved. There had to be more than just dry nonfiction about neovikings."

    r "But I didn’t really realize what my family meant to me."

    return

label RQ1A2:

    r sad "Yeah, it was pretty easy."

    r "... I wish it had been harder."

    return

label RQ2A1:
    r laugh "Oh, I spent almost a decade following the canal."

    h @ laugh "A DECADE?"

    r happy "Yeah, it's kinda crazy in retrospect."

    r "The strange thing about the canal is there really aren’t many more people living along it than anywhere else in the library. You’d think that people would find this weird feature of the library and decide it’s a good place to live, but for whatever reason that isn’t the case."

    r "There was a good group of us who traveled the canal though. I’d pass people and then they’d pass me when I stopped. It was nice, stopped it from being too lonely."

    return

label RQ2A2:
    r neutral "Oh, I didn’t really think about them that much for the first five years."

    #show harper in shock right here

    r @ upset "Then one day, I couldn’t stop thinking about my sister. She’d become an adult and made her decision and I’d never know if she stayed or left."

    return
