import time
from random import randint,randrange,choice
import random
from colorama import Fore , Back,init #,Style
from termcolor import colored

def Macha_the_child():
    from pygame import mixer
    # from playsound import playsound
    # playsound('jinglebells.mp3',False)
    mixer.init()
    mixer.music.load('MachaTheKing/GingleBells/jinglebells.mp3')
    mixer.music.play()
    print('playing sound using  playsound')
    init()
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(80000*' ')


    space = ''
    spc_1 = 5*' '
    spc_2 =8*' '
    spc_3 = 12*' '
    spc_4 = 15*' '
    spc_5 = 18*' '
    spc_6 = 20*' '
    spc_list = [spc_1,spc_2,spc_3,spc_4,spc_5,spc_6]
    my_col = ['red','blue','green','white','yellow','grey','magenta','cyan',]
    data_list = [   f'{space} Merry Christmas....🥳',
                    f'{space} huhuu its Xmas...🎄',
                    f'{space} Stay Blessed..⛄',
                    f"{space} Happy Christmas...!!🎂",
                    f"{space} Christmas isn't a season. It's a feeling...❄️",
                    f"{space} The True spirit of Christmas is LOVE...❤️"

                    ]
    for i in range(1,80):
        count= randint(1,200)
        while(count > 0):
            space += ' '
            count -=1
        if(i % 3 == 0 ):
            icons_blnk_lst = ['🌲','🎄','❤️'] 
            icons_nonblnk_lst = ['🌟','❄️','⚡','✨','💫']
            print(f'{choice(spc_list)}',end=' ')
            print(colored(choice(icons_blnk_lst),attrs = []),end=' ')
            print(f'{choice(spc_list)}',end=' ')
            print(colored(choice(icons_nonblnk_lst),attrs = ['blink']),end=' ')
            print(f'{choice(spc_list)}',end=' ')
            print(colored(choice(icons_blnk_lst),attrs = []),end=' ')
            print(f'{choice(spc_list)}',end=' ')

            print(colored(choice(data_list),attrs = []),end=' ')
            print(f'{choice(spc_list)}',end=' ')


            print(colored(choice(icons_nonblnk_lst),attrs = ['blink']),end=' ')
            print(f'{choice(spc_list)}',end=' ')
            print(colored(choice(icons_blnk_lst),attrs = []),end=' ')
            print(f'{choice(spc_list)}',end=' ')
            print(colored(choice(icons_nonblnk_lst),attrs = ['blink']),end=' ')

        if(i%4==0):
            new_val = 10*' '
            print( colored(f'{space} -⛄- {new_val} '))

        elif(i%5==0):
            marry_chrs = colored(choice(data_list))
            print(marry_chrs)

        elif(i%6==0):
            its_xass = colored(choice(data_list))
            print(its_xass)

        elif(i%7==0):
            print( colored(  f'{space} 🎉'))

        elif(i%8==0  ):
            print(colored( f'{space} ✨'))      

        elif(i%9==0):
            stay_blessed = colored(choice(data_list))
            print(stay_blessed)

        elif(i%10==0):
            aa =  colored(choice(data_list))
            print(aa)
        else:
            print(space + '🎊')

        space = ''
        time.sleep(0.2)

    return 'Done'

def macha_the_santa_s_best_child():
    from . import xmas_turtle
    from . import christmas
    from . import conversation
    x = Macha_the_child()
    print(x)
    xmastree = christmas.christ()
    abc = xmas_turtle.abcdef()
    conv = conversation.santa_n_Macha()