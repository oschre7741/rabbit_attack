import pygame
import sys
from time import sleep
import secret_game

# Rabbit Attack!

def start():
    print("""
                                                   (                    (                                                     )  ____")
     (  (         (                         )      )\ )   (      (   (  )\ )  *   )     (      *   )  *   )   (       (    ( /( |   /")
     )\))(   '  ( )\          )     (    ( /(     (()/(   )\   ( )\( )\(()/(` )  /(     )\   ` )  /(` )  /(   )\      )\   )\())|  / ")
    ((_)()\ )  ))((_)(  (    (     ))\   )\())(    /(_)|(((_)( )((_)((_)/(_))( )(_)) ((((_)(  ( )(_))( )(_)|(((_)(  (((_)|((_)\ | /  ")
    _(())\_)()/((_)  )\ )\   )\  '/((_) (_))/ )\  (_))  )\ _ )((_)((_)_(_)) (_(_())   )\ _ )\(_(_())(_(_()) )\ _ )\ )\___|_ ((_)|/   ")
    \ \((_)/ (_))| |((_|(_)_((_))(_))   | |_ ((_) | _ \ (_)_\(_) _ ) _ )_ _||_   _|   (_)_\(_)_   _||_   _| (_)_\(_|(/ __| |/ /(     ")
     \ \/\/ // -_) / _/ _ \ '  \() -_)  |  _/ _ \ |   /  / _ \ | _ \ _ \| |   | |      / _ \   | |    | |    / _ \  | (__  ' < )\    ")
      \_/\_/ \___|_\__\___/_|_|_|\___|   \__\___/ |_|_\ /_/ \_\|___/___/___|  |_|     /_/ \_\  |_|    |_|   /_/ \_\  \___|_|\_((_)   ")
    """)                                                                                                                           
    
def end():
    print("""
    ,---.            . .                ,--,--'.           .                          .                    /\\")
    |  -'  ,-. ,-. ,-| |-. . . ,-.      `- |   |-. ,-. ,-. | , ,-.   ,'' ,-. ,-.  ,-. |  ,-. . . . ,-. ,-. )( ")
    |  ,-' | | | | | | | | | | |-'       , |   | | ,-| | | |<  `-.   |- | | |     | | |  ,-| | | | | | | | \/ ")
    `---|  `-' `-' `-^ ^-' `-| `-' :;    `-'   ' ' `-^ ' ' ' ` `-'   |  `-' '     |-' `' `-^ `-| ' ' ' `-| :; ")
     ,-.|                   /|                                       '            |           /|        ,|    ")
     `-+'                  `-'                                                    '          `-'        `'    ")
    """)
    
def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()
        if "y" in answer:
            return True
        elif "n" in answer:
            return False

def play():
    num_knights = 5
    rabbit_is_alive = True
    flee = False
    play_game = False

    bunny = ("Look, a cute little bunny rabbit.")
    for char in bunny:
        sys.stdout.write(char)
        sleep(0.1)
    print()
     
    print("""
         (\_/)
         (-.-)
         (> <)
          = =    
            """)
    approach_rabbit = confirm("Shall we approach the rabbit?")

    if approach_rabbit:
        while rabbit_is_alive and num_knights > 0 and not flee:
            use_grenade = confirm("Shall we use the Holy Hand Grenade?")
        
            if use_grenade:
                count = ("1... 2... 5... No, 3!")
                for char in count:
                    sys.stdout.write(char)
                    sleep(0.1)
                print()
                print("Boom!")
                rabbit_is_alive = False
            else:
                run_away = confirm("Shall we run away then?")
                if run_away:
                    print("RUN AWAY!!!")
                    flee = True
                else:
                    num_knights -= 1
                    dead = ("Oh, no! The rabbit just killed one of the knights!")
                    for char in dead:
                        sys.stdout.write(char)
                        sleep(0.1)
                    print()
                    left = ("Only " + str(num_knights) + " remain.")
                    for char in left:
                        sys.stdout.write(char)
                        sleep(0.1)
                    print()

        if not approach_rabbit:
            go_away = ("Just go away. I don't want you here.")
            for char in go_away:
                sys.stdout.write(char)
                sleep(0.1)
            print()
        elif flee:
            wuss = ("You were too much of a wuss to face the tiny little rabbit. You lose.")
            for char in wuss:
                sys.stdout.write(char)
                sleep(0.1)
            print()
        elif num_knights > 0:
            win = ("The killer rabbit has been defeated. You win!")
            for char in win:
                sys.stdout.write(char)
                sleep(0.1)
            print()
        else:
            loss = ("All of the knights are dead. You lose.")
            for char in loss:
                sys.stdout.write(char)
                sleep(0.1)
            print()
            
    else:
        here = ("Then what are you even doing here?")
        for char in here:
            sys.stdout.write(char)
            sleep(0.1)
        print()
        
        dots = "..."
        for char in dots:
            sys.stdout.write(char)
            sleep(0.5)
        print()
        
        more_dots = "......"
        for char in more_dots:
            sys.stdout.write(char)
            sleep(0.5)
        print()
        
        even_more_dots = "............"
        for char in even_more_dots:
            sys.stdout.write(char)
            sleep(0.5)
        print()
        
        why = ("...Why are you still here?")
        for char in why:
            sys.stdout.write(char)
            sleep(0.1)
        print()
        
        stay = ("No one's ever stayed with me this long.")
        for char in stay:
            sys.stdout.write(char)
            sleep(0.1)
        print()

        friend = confirm("Maybe we could be friends...what do you say?")
        if friend:
            friends = ("You discovered the secret ending. You are the true winner, for you have the greatest prize of all: ")
            for char in friends:
                sys.stdout.write(char)
                sleep(0.1)
            print()
        
            print("""
                /)    o             /     /  o      
               // _  ,  _  _ _   __/ (   /_ ,   ,_  
              //_/ (_(_(/_/ / /_(_/_/_)_/ /_(__/|_)_
             /)                                /|   
            (/                                (/
            """)
            
            dots = "..."
            for char in dots:
                sys.stdout.write(char)
                sleep(0.5)
            print()
            
            more_dots = "......"
            for char in more_dots:
                sys.stdout.write(char)
                sleep(0.5)
            print()
            
            what = "You've won the game. You can go now."
            for char in what:
                sys.stdout.write(char)
                sleep(0.1)
            print()
            
            unless = "Unless...do you want to play another game with me?"
            for char in unless:
                sys.stdout.write(char)
                sleep(0.1)
            print()
            
            play_game = confirm("Play another game?")
            if play_game:
                secret_game.main()
            else:
                ok = ("Oh. ok.")
                for char in ok:
                    sys.stdout.write(char)
                    sleep(0.2)
                print()
                playing = False
        else:
            print("rude.")
            playing = False
            
start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to play again?")

end()
