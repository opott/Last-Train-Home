define a = Character("Announcer", voice_tag="announcer")
define s = Character("Stranger", voice_tag="stranger", color="#268DFF")
define y = Character("You", voice_tag="you", color="#51e019ff")

transform leftseat:
    xalign 0.30 yalign 0.22 zoom 0.80

transform rightseat:
    xalign 0.66 yalign 0.22 zoom 0.80

image platform:
    "images/Night Platform BMO.png"

image platform_arriving:
    "images/Night Platform BMO - Train.png"

image platform_standing:
    "images/Night Platform BMO - Standing.png"

image train_carriage:
    "images/Train Carriage.png"

image stranger_serious:
    "images/Stranger - Serious.png"
    zoom 0.4

image you_serious:
    "images/You - Serious.png"
    zoom 0.4

label start:
    scene platform

    play music "audio/night.opus" volume 0.1 loop
    
    "The time is 00:12."

    "You are standing at Birmingham Moor Street station waiting to catch the last train home."

    play sound "audio/arriving_bmo.opus" volume 0.6

    "Sounds like your train is about to arrive!"

    scene platform_arriving

    $ renpy.pause(3.0, hard=True)

    voice "audio/bmo_approaching_ann.mp3"
    a "\"The train now approaching platform 1 is the 00:13 service to Stratford-upon-Avon.\""

    jump train_standing

label train_standing:
    stop sound

    scene platform_standing

    show stranger_serious

    s "\"I wouldn't get on that train if I were you...\""

    y "\"Why?\""

    s "\"Because that train doesn't go where you think it does.\""

    y "\"But it's going to Stratford!?\""

    s "\"That's where you think its going...\""

    a "\"This is the final call for the service to Stratford-upon-Avon on platform 1\""

    menu:
        "Ask the stranger what they mean":
            jump ask_stranger
        "Ignore them and board the train":
            jump board_train

label ask_stranger:
    y "\"What do you mean it doesn't go there?\""

    s "\"People get on that train every night...\""
    s "\"But nobody remembers getting off...\""

    y "*laughing nervously*"

    a "\"Any passengers wishing to travel on the 00:13 service, please board the train now!\""

    menu:
        "Board the train anyway":
            jump board_train
        "Stay on the platform":
            jump stay_on_platform

label board_train:
    stop music
    
    scene train_carriage

    play music "audio/engine.mp3" volume 0.5

    show stranger_serious at leftseat

    "You step onto the train..."

    "You sit opposite the stranger..."
    
    show you_serious at rightseat

    y "\"So you got on after all that?\""

    s "\"I had to.\""

    voice "audio/next_station_.mp3"
    a "\"The next station is...\""

    play sound "audio/static.opus" volume 2.0 loop

    "..."

    s "\"Oh no...\""

    y "\"WHAT!?\""

    menu:
        "Look out of the window":
            jump window_ending
        "Ask the stranger what's going on":
            jump truth_ending

label window_ending:
    scene black
    
    stop sound

    "You look out of the window"

    "The train isn't passing through the countryside."

    "It's still inside a tunnel."

    "And it isn't slowing down."

    "You realise the stranger was right all along."

    "The End..."

    return

label truth_ending:

    y "\"You knew this would happen!?\""

    s "\"Yes.\""

    y "\"So why did you get on!?\""

    s "\"Because someone has to warn the next passenger.\""

    "The stranger stands up"

    "The train slows."

    hide stranger_serious

    "You're now alone in the carriage."

    stop sound

    voice "audio/approach_bmo_ann.wav"
    a "\"We are now approaching Birmingham Moor Street.\""

    "The End..."

    return

label stay_on_platform:
    "The train doors close."

    "You watch as the train disappears into the night."

    scene platform

    "*phone vibrating*"

    "News Alert: Train disappears between stations..."

    "You walk home instead."

    "The End..."

    return