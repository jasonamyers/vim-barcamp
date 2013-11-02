# MOVEMENT
'''
You move around by using h, j, k, and l keys, or arrow keys
j will move you up a line
k will move you down a line
h will move you right
l will move you left
'''

'''
You can also use G to go to the bottom of a file
'''































'''
Ctrl-F will move you forward a page
Ctrl-B will move you back a page
'''

'''
$ will take you to the end of a line
0 will take you to the beginning of a line
    ^ will take you to the first character of a line
'''

'''
w will move you forward a word beginning
b will move you back a word beginning
e will move you forward to the next word ending
'''

'''
H will move you to top of screen
M will move you to middle of screen
L will move you to bottom of screen
'''

'''
:# will move you to that line number
'''

'''
% will move you between sets of symbols such as ( parentheses ) or { curly braces }
'''





















'''
 __________________________
< Slow moving cow defeated >
 --------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''





































# EDITING
'''
i will place you in insert mode
<Esc> will exit insert mode
r will replace a character
R will replace until you stop
Replace me with info about x
d will delete one object
dd will delete one line
D will delete till the end of the line
c will change one object
C will change till the end of the line
'''

'''
Bacon ipsum dolor sit amet spare ribs shankle pancetta venison turducken ribeye,
kevin hamburger shank jerky. Turducken corned beef filet mignon, bresaola doner
fatback jerky short loin sirloin shankle sausage pork loin. Chicken pork loin
frankfurter venison tri-tip, chuck sirloin ribeye shankle pork tongue jowl doner.
Frankfurter sirloin short loin boudin capicola, leberkas jowl drumstick venison
salami shoulder meatloaf shankle. Strip steak bresaola tongue pastrami chicken
andouille tri-tip turducken shank. Fatback drumstick leberkas swine kevin pork
loin, t-bone cow bacon.

Bacon ipsum dolor sit amet spare ribs shankle pancetta venison turducken ribeye,
kevin hamburger shank jerky. Turducken corned beef filet mignon, bresaola doner
fatback jerky short loin sirloin shankle sausage pork loin. Chicken pork loin
frankfurter venison tri-tip, chuck sirloin ribeye shankle pork tongue jowl doner.
Frankfurter sirloin short loin boudin capicola, leberkas jowl drumstick venison
salami shoulder meatloaf shankle. Strip steak bresaola tongue pastrami chicken
andouille tri-tip turducken shank. Fatback drumstick leberkas swine kevin pork
loin, t-bone cow bacon.

Bacon ipsum dolor sit amet spare ribs shankle pancetta venison turducken ribeye,
kevin hamburger shank jerky. Turducken corned beef filet mignon, bresaola doner
fatback jerky short loin sirloin shankle sausage pork loin. Chicken pork loin
frankfurter venison tri-tip, chuck sirloin ribeye shankle pork tongue jowl doner.
Frankfurter sirloin short loin boudin capicola, leberkas jowl drumstick venison
salami shoulder meatloaf shankle. Strip steak bresaola tongue pastrami chicken
andouille tri-tip turducken shank. Fatback drumstick leberkas swine kevin pork
loin, t-bone cow bacon.
'''

'''
v will put you in visual mode
   - in visual mode normal movement keys work
V will select a whole line
<Ctrl-V> opens block selection
y is copy
d/x work like cut
p is paste
'''

'''
 _________
< Cookies >
 ---------
          \           \  /
           \           \/
               (__)    /\
               (oo)   O  O
               _\/_   //
         *    (    ) //
          \  (\\    //
           \(  \\    )
            (   \\   )   /\
  ___[\______/^^^^^^^\__/) o-)__
 |\__[=======______//________)__\
 \|_______________//____________|
     |||      || //||     |||
     |||      || @.||     |||
      ||      \/  .\/      ||
                 . .
                '.'.`

'''


# SEARCHING

'''
/<string> will search forward for string
n will find next match in search
/ will find next thing forward matching search
?<Enter> will flip the search backwards
:%s/<old>/<new>/<g> find and replace <globally>.
:%s/\%V<old>/<new>/<g> find and replace <First only>
'''

'''
Bacon ipsum dolor sit amet spare ribs shankle pancetta venison turducken ribeye,
kevin hamburger shank jerky. Turducken corned beef filet mignon, bresaola doner
fatback jerky short loin sirloin shankle sausage pork loin. Chicken pork loin
frankfurter venison tri-tip, chuck sirloin ribeye shankle pork tongue jowl doner.
Frankfurter sirloin short loin boudin capicola, leberkas jowl drumstick venison
salami shoulder meatloaf shankle. Strip steak bresaola tongue pastrami chicken
andouille tri-tip turducken shank. Fatback drumstick leberkas swine kevin pork
loin, t-bone cow bacon.

Bacon ipsum dolor sit amet spare ribs shankle pancetta venison turducken ribeye,
kevin hamburger shank jerky. Turducken corned beef filet mignon, bresaola doner
fatback jerky short loin sirloin shankle sausage pork loin. Chicken pork loin
frankfurter venison tri-tip, chuck sirloin ribeye shankle pork tongue jowl doner.
Frankfurter sirloin short loin boudin capicola, leberkas jowl drumstick venison
salami shoulder meatloaf shankle. Strip steak bresaola tongue pastrami chicken
andouille tri-tip turducken shank. Fatback drumstick leberkas swine kevin pork
loin, t-bone cow bacon.

Bacon ipsum dolor sit amet spare ribs shankle pancetta venison turducken ribeye,
kevin hamburger shank jerky. Turducken corned beef filet mignon, bresaola doner
fatback jerky short loin sirloin shankle sausage pork loin. Chicken pork loin
frankfurter venison tri-tip, chuck sirloin ribeye shankle pork tongue jowl doner.
Frankfurter sirloin short loin boudin capicola, leberkas jowl drumstick venison
salami shoulder meatloaf shankle. Strip steak bresaola tongue pastrami chicken
andouille tri-tip turducken shank. Fatback drumstick leberkas swine kevin pork
loin, t-bone cow bacon.
'''



















'''
 _______________________
< Search Bunny Defeated >
 -----------------------
  \
   \   \
        \ /\
        ( )
      .( o ).
'''





import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pytn.settings")

from django.core.wsgi import get_wsgi_application
#from dj_static import Cling

#application = Cling(get_wsgi_application())
application = get_wsgi_application()


'''
 _________
< COLORS! >
 ---------
          \
           \
            \          __---__
                    _-       /--______
               __--( /     \ )XXXXXXXXXXX\v.
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\
          /XXXXX(              )--_  XXXXXXXXXXX\
         /XXXXX/ (      O     )   XXXXXX   \XXXXX\
         XXXXX/   /            XXXXXX   \__ \XXXXX
         XXXXXX__/          XXXXXX         \__---->
 ---___  XXX__/          XXXXXX      \__         /
   \-  --__/   ___/\  XXXXXX            /  ___--/=
    \-\    ___/    XXXXXX              '--- XXXXXX
       \-\/XXX\ XXXXXX                      /XXXXX
         \XXXXXXXXX   \                    /XXXXX/
          \XXXXXX      >                 _/XXXXX/
            \XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""
'''





































'''
. repeats the last chorded action
q<register> Start macro recording
q Stops record
@<register> Executes the macro
@@ Executes last macro
#@@ Executes it # times
<Ctrl>-A Increments a number
<Ctrl>-X Decrements a number
'''
#Dot formula
'''
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
'''
#Macro
'''
1.
'''








'''
 _______________
< Repeatability >
 ---------------
   \         ,        ,
    \       /(        )`
     \      \ \___   / |
            /- _  `-/  '
           (/\/ \ \   /\
           / /   | `    \
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \
<----|====O)))==) \) /====
<----'    `--' `.__,' \
             |        |
              \       /
        ______( (_  / \______
      ,'  ,-----'   |        \
      `--{__________)        \/
'''




















# DRAGONS

'''
 _________________
< Setting/Plugins >
 -----------------
      \                    / \  //\
       \    |\___/|      /   \//  \\
            /0  0  \__  /    //  | \ \
           /     /  \/_/    //   |  \  \
           @_^_@'/   \/_   //    |   \   \
           //_^_/     \/_ //     |    \    \
        ( //) |        \///      |     \     \
      ( / /) _|_ /   )  //       |      \     _\
    ( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
  (( / / )) ,-{        _      `-.|.-~-.           .~         `.
 (( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \
 (( /// ))      `.   {            }                   /      \  \
  (( / ))     .----~-.\        \-'                 .~         \  `. \^-.
             ///.----..>        \             _ -~             `.  ^-`  ^-_
               ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                  /.-~
'''























'''
This file online at:
https://github.com/jasonamyers/vim-barcamp
'''















'''
You can use gg to go to the top of a file
'''
