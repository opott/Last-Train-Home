define a = Character("Announcer", voice_tag="announcer")
define s = Character("Stranger", voice_tag="stranger", color="#268DFF")
define y = Character("You", voice_tag="you", color="#51e019ff")

screen stop_scr():
    key "dismiss" action [[]]

image platform:
    "images/Night Platform BMO.png"

image platform_arriving:
    "images/Night Platform BMO - Train.png"

image platform_standing:
    "images/Night Platform BMO - Standing.png"

image stranger_serious:
    "images/Stranger - Serious.png"
    zoom 0.4

label start:
    scene platform

    play music "audio/night.opus" volume 0.1 loop
    
    "The time is 00:12."

    "You are standing at Birmingham Moor Street station waiting to catch the last train home."
    
    "Looks like your train is about to arrive"

    play sound "audio/arriving_bmo.opus" volume 0.6

    scene platform_arriving

    $ renpy.pause(3.0, hard=True)

    voice "audio/bmo_approaching_ann.mp3"
    a "\"The train now approaching platform 1 is the 00:13 service to Stratford-upon-Avon.\""

    # $ renpy.pause(3.0, hard=True)

    jump train_standing

label train_standing:
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
    "..."

label board_train:
    "..."