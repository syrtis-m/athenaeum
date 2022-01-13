label ending_stay:

    scene house evening with fade
    with Pause(2)

    show mom neutral at left

    m "... So you decided to Stay?"

    pc "Yeah... Yeah I think I'm going to Stay"

    m "Oh this is so wonderful [yn]! I’m so glad you’re going to be staying around!"

    m "I would have been supportive of you leaving, but now I won’t have to worry if you’ll be okay out there."

    m "Anyway, write down your decision and go tell Harper!"

    "[yn] writes \'Stay\' on a piece of paper"

    scene town center evening with fade

    show harper neutral at middle
    with Pause(2)

    h "...Took you a while, huh."

    h "…Have you decided?"

    pc "Yeah."

    h "Well, I’ll hand you my note and you hand me yours."

    "You hand Harper the note reading \'Stay\'"

    "Harper hands you a note, folded in half"

    if stay > leave:
        call ending_stay_stay
    else:
        call ending_stay_leave

    return

label ending_stay_stay:
    "You open the note. In shaky handwriting. the word \'Stay\' is written."

    $ renpy.pause(delay=1)

    h "YES!! YOU'RE STAYING!"

    h "I'm... I'm really glad"

    h "Obviously like I’d support you if you’d left, but… I’d miss you."

    h "I.. was worried you’d chose to leave, and then I’d never see you again."

    h "You’d be lonely or get hurt or get lost or who knows. You’d be gone and I wouldn’t know how you were."

    h "I..."

    h "I'm glad, [yn]."

    pc "Me too. I… I would have missed you."

    pc "I’m glad we’ll be here together."

    show harper neutral at right

    show mom happy at left

    m "Harper! Are you staying?"

    h "Yes! We’ll be here together."

    m "Oh, that’s just wonderful! I’m so glad."

    m "Come on over for dinner tonight, Harper! We’ll celebrate!"

    scene black

    show text "[yn]: Stay \nHarper: Stay" with fade
    with Pause(3)

    return

label ending_stay_leave:
    "You open the note. In shaky handwriting. the word \'Leave\' is written."

    $ renpy.pause(delay=1)

    h "...Oh. I."

    h "I’ll… I’ll miss you, [yn]."

    h "I’m excited to go out there I just… I thought we’d travel together."

    pc "Harper… I just… I’m not going to forget you."

    pc "You can travel the library and still come back to visit, like Bo!"

    pc "It’ll be different, but… different isn’t necessarily bad."

    h "…Yeah. Yeah, I can do that."

    pc "I’ll miss you. I… I’ve known you forever. It’ll be different, but you’ll be happier out there."

    h "Yeah... Yeah."

    show harper neutral at right

    show mom neutral at left

    h "No I'm... I'm Leaving."

    m "Oh, Harper. It’ll be alright."

    m "I know it’s scary right now, but you’ll go out there and grow and figure out who you are!"

    h "Yeah... Yeah."

    m "Come on over for dinner tonight, Harper. We'll celebrate."

    scene black

    show text "[yn]: Stay \nHarper: Leave" with fade
    with Pause(3)

    return
