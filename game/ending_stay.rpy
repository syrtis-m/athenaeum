label ending_stay:

    scene house evening with fade
    with Pause(2)

    show mom neutral at center

    m "...So you decided to Stay?"

    pc "Yeah... Yeah I think I'm going to Stay."

    m happy "Oh this is so wonderful [yn]! I’m so glad you’re going to be staying around!"

    m @ neutral "I would have been supportive of you leaving, but now I won’t have to worry if you’ll be okay out there."

    m "Anyway, write down your decision and go tell Harper!"

    "You write \'Stay\' on a scrap of paper."

    scene town center evening with fade

    show harper neutral at center
    with Pause(2)

    h "...Took you a while, huh."

    h "…Have you decided?"

    pc "Yeah."

    h "Well, I’ll hand you my note and you hand me yours."

    "You hand Harper the note reading \'Stay\'."

    "Harper hands you a note folded in half."

    if stay > leave:
        call ending_stay_stay
    else:
        call ending_stay_leave

    return

label ending_stay_stay:
    play music "audio/Ludum_Dare_38_Track_8.wav" loop fadein 1.0

    "You open the note. In shaky handwriting, \'Stay\' is written."

    $ renpy.pause(delay=1)

    h @ laugh "YES!! YOU'RE STAYING!"

    h happy "I'm... I'm really glad."

    h "Obviously like I’d support you if you’d left, but… I’d miss you."

    h @ sad "I.. was worried you’d chose to leave, and then I’d never see you again."

    h @ sad "You’d be lonely or get hurt or get lost or who knows. You’d be gone and I wouldn’t know how you were."

    h @ neutral "I..."

    h "I'm glad, [yn]."

    pc "Me too. I… I would have missed you."

    pc "I’m glad we’ll be here together."

    show harper happy at right

    show mom happy at left

    m "Harper! Are you staying?"

    h "Yes! We’ll be here together."

    m @ laugh "Oh, that’s just wonderful! I’m so glad."

    m "Come on over for dinner tonight, Harper! We’ll celebrate!"

    scene black

    show text "[yn]: Stay \nHarper: Stay" with fade
    with Pause(3)

    return

label ending_stay_leave:
    play music "audio/Ludum_Dare_38_Track_5.wav" loop fadein 1.0

    "You open the note. In shaky handwriting, \'Leave\' is written."

    $ renpy.pause(delay=1)

    h upset "...Oh. I."

    h sad "I’ll… I’ll miss you, [yn]."

    h @ happy "I’m excited to go out there! I just…"

    h "I thought we’d travel together."

    pc "Harper… I just… I’m not going to forget you."

    pc "You can travel the library and still come back to visit, like Bo!"

    pc "It’ll be different, but… different isn’t necessarily bad."

    h neutral "…Yeah. Yeah, I can do that."

    pc "I’ll miss you. I… I’ve known you forever. It’ll be different, but you’ll be happier out there."

    h happy "Yeah... Yeah."

    show harper neutral at right

    show mom happy at left

    m "Harper! Are you staying?"

    h "No I'm... I'm Leaving."

    m sad "Oh, Harper. It’ll be alright."

    m happy "I know it’s scary right now, but you’ll go out there and grow and figure out who you are!"

    h "Yeah... Yeah."

    m neutral "Come on over for dinner tonight, Harper. We'll celebrate."

    scene black

    show text "[yn]: Stay \nHarper: Leave" with fade
    with Pause(3)

    return
