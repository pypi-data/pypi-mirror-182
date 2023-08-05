import turtle
import time

def santa_n_Macha():
    
    screen= turtle.Screen()
    turtle.title('Santa vs Macha')
    screen.setup(width=1.0, height=1.0)
    screen.bgcolor('black')
    screen.tracer(0)
    tt = turtle.Turtle()


    info_turtle = turtle.Turtle()
    info_turtle.color('red')
    info_turtle.hideturtle()
    info_turtle.speed(0)
    info_turtle.penup()
    info_turtle.goto(-300,0)
    info_turtle.pendown()
    info_turtle.write('Next vache script yevarini vudesinchi kadhu just for FUN , Please fun ghane tesukondiiiiiii , A HUMBLE REQUEST')
    time.sleep(5)
    info_turtle.clear()


    
    my_col = ['red','purple','blue','green','orange','yellow']
    
    tt.color('blue')
    tt.hideturtle()
    tt.speed(10)
    tt.penup()
    
    #Macha
    tt.right(180)
    tt.forward(200)
    tt.right(90)
    tt.pendown()
    #tt.right(90)
    tt.forward(100)
    tt.right(90)
    tt.circle(30)
    tt.right(90)
    tt.forward(40) #head to hands
    tt.left(45)
    tt.forward(60)
    tt.backward(60)
    tt.right(90)
    tt.forward(60)
    tt.backward(60)
    tt.right(315)
    tt.forward(110) #hands to legs
    tt.left(45)
    tt.forward(60)
    tt.backward(60)
    tt.right(90)
    tt.forward(60)
    tt.backward(60)
    tt.penup()
    tt.goto(-180,-10)
    tt.pendown()
    tt.write('*Macha')
    
    #santa
    tt2 = turtle.Turtle()
    tt2.color('red')
    tt2.hideturtle()
    tt2.speed(6)
    tt2.penup()
    
    #tt2.right(180)
    tt2.forward(200)
    tt2.left(90)
    tt2.pendown()
    #tt.right(90)
    tt2.forward(100)
    tt2.right(90)
    tt2.circle(30)
    tt2.right(90)
    tt2.forward(40) #head to hands
    tt2.left(45)
    tt2.forward(60)
    tt2.backward(60)
    tt2.right(90)
    tt2.forward(60)
    tt2.backward(60)
    tt2.right(315)
    tt2.forward(110) #hands to legs
    tt2.left(45)
    tt2.forward(60)
    tt2.backward(60)
    tt2.right(90)
    tt2.forward(60)
    tt2.backward(60)
    tt2.penup()
    tt2.goto(220,60)
    tt2.pendown()
    tt2.write('*Santa')

    #conversation #santa
    tt3 = turtle.Turtle()
    tt3.color('green')
    tt3.hideturtle()
    tt3.speed(0)
    tt3.penup()
    tt3.goto(220,180)
    tt3.pendown()
    tt3.write('Hello Sai Krishna')
    time.sleep(3)
    tt3.clear()

    #conversation #santa
    tt4 = turtle.Turtle()
    tt4.color('red')
    tt4.hideturtle()
    
    tt4.penup()
    tt4.goto(-220,180)
    tt4.pendown()
    tt4.write('OMG OMGG Santa is it real or am i dreaming')
    time.sleep(5)
    tt3.speed(6)
    tt4.speed(6)
    
    tt4.clear()
    tt3.write('Yes My child, \n Its Real')
    time.sleep(2)
    tt3.clear()
    tt4.write('Thank god I have lot of items \n in my amazon and flipkart cart for you')
    time.sleep(5)
    tt4.clear()
    tt3.write('Don"t Expect too much my dear Sai krishna \n Maku konni budjet problems unnay')
    time.sleep(6)
    tt3.clear()
    tt4.write('oho noooo , \n Firstly  santa please don"t call me as Sai krishna \n just use "Macha", Macha is Fine')
    time.sleep(6)
    tt4.clear()
    tt3.write('Enduku child')
    time.sleep(3)
    tt3.clear()
    tt4.write('Sai Krishna is old santa \n Macha is in trending now,\n i think nek elantivi teleeka povachu santa')
    time.sleep(6)
    tt4.clear()    
    tt3.write('Uff...  Its ok my child...') #🤦🏽
    time.sleep(4)
    tt3.clear()    
    tt4.write('Santa, Chala bore kodutundhiii.....')
    time.sleep(4)
    tt4.clear()    
    tt3.write('Please My Child, Konni ammaila numbers evvandi ani matram aadagaku')
    time.sleep(5)
    tt3.clear()
    tt4.write('uff.....') #🙆🏽‍♂️
    time.sleep(3)
    tt4.clear()
    tt3.write('Shall we play a game Macha')
    time.sleep(4)
    tt3.clear()
    tt4.write('huhuu im too excited santa  lets start') #🦸🏽‍♂️ 🦹🏽‍♀️
    time.sleep(5)
    tt4.clear()
    tt3.write('But Truth matrame cheppali , \n this game is like truth or dare')
    time.sleep(5)
    tt3.clear()
    tt4.write('haha santa...! i think neku ee vishayam teleeka povachu \n Macha yeppudu nijale chepthadu , \n Lie ante entoo kuda naku teleedhu')
    time.sleep(6)
    tt4.clear()
    tt3.write('Edhi Comedy chese time kadhu my child')
    time.sleep(5)
    tt3.clear()
    tt4.write('uff (Inside : Navvalo yedalo kuda \n  teleeedam ledhu karma )') #🥲😰  🤦‍♂️
    time.sleep(5)
    tt4.clear()
    tt4.write('Sarlendi santa aha game ento \n start cheyyandi nijale cheptha')
    time.sleep(5)
    tt4.clear()


    tt3.write('Nee bestie aina RANJITH Gurinchi \n  em anukuntunnav cheppu')
    time.sleep(4)
    tt3.clear()
    tt4.write('Em cheppamantaru santa , \n  Chepthe oka badha cheppaka pothe oka badha')
    time.sleep(6)
    tt4.clear()
    tt4.write('Aha Dashboard yedho chesthunnam kadha , \n  Kastamainavi anni naku echi easy tasks emo thanu chesthunnadu')
    time.sleep(6)
    tt4.clear()
    tt4.write('Poni avi aina chesthunnada ante , \n  Phone nokkuthaa Phone matladuthanee untadu')
    time.sleep(6)
    tt4.clear()
    tt4.write('Chivaraku em chestham Deadline time lo thana tasks kuda \n  nenee cheyyalsina paristhithi ')
    time.sleep(6)
    tt4.clear()
    tt4.write('Eppatiki oka regret enti ante Callcenter lo \n  join aipothe best emo anipistha untadhu ,\n  Mana vadu kalipee pulihoraki')
    time.sleep(6)
    tt4.clear()

    tt3.write('Ounaa... , Enni kastalu ochayi macha, \n  Nee kastalu pagavadiki kuda rakudadhu') #😕 🙁
    time.sleep(6)
    tt3.clear()


    tt3.write('Mari, What about SAI ABINESH my child')
    time.sleep(4)
    tt3.clear()
    tt4.write('Emo santa , Konni sarlu bayam vestha untadhi, \n  Sai abinesh valla Naku mental ochesthademo  ')
    time.sleep(6)
    tt4.clear()
    tt4.write('Yee erragadda hospital lo aina join chesestharemo ani ')
    time.sleep(5)
    tt4.clear()
    tt3.write('Em aindhi macha')
    time.sleep(3)
    tt3.clear()

    tt4.write('Abinesh code medha chese prayogalu chusthe, \n Athanu aadighee questions chusthe yeppudoo kappudu \n naku mental ochisthadi santa ')
    time.sleep(6)
    tt4.clear()

    tt3.write('Hoo , Mari Vamsi gurinchi em anukuntunnav')
    time.sleep(6)
    tt3.clear()

    tt4.write('Em cheppali santa Over action candidate')
    time.sleep(6)
    tt4.clear()
    
    tt3.write('Ouna em aindhi macha')
    time.sleep(4)
    tt3.clear()
   
    tt4.write('Ounu santa Yedhoo chesthunna anukuntadu , em cheyyadu \n aha kullipoina jokes okati vesthadu')
    time.sleep(6)
    tt4.clear()

    tt4.write('Ninna kaka monna ochadaa , \n Appudee nannu commanding chesthunnadu')
    time.sleep(6)
    tt4.clear()
   
   
    tt4.write('Yevarini command chesina naku badha ledhu')
    time.sleep(4)
    tt4.clear()
    
    tt4.write('Andarini vadilesi nannu commanding chesthunnadu')
    time.sleep(4)
    tt4.clear()
    
    tt4.write('Work cheydu em cheydu \n Memu chesina work antha \n athanu chesa  annatlu cheppukuntadu santa')
    time.sleep(6)
    tt4.clear()

    tt3.write('Ouna, Enni kastalu ochay macha')
    time.sleep(4)
    tt3.clear()
    
    tt3.write('Mari last gha Meenakshi Gurinchi em antav macha')
    time.sleep(5)
    tt3.clear()

  
    tt4.write('Cheppedhi em undhi santa He is like one type of psycho')
    time.sleep(6)
    tt4.clear()
    
    tt4.write('Emee kuda overaction candidate ehe, \n Yekkado yee forest lono puttalsindhi , \n by mistake ekkadaki ochesindhi')
    time.sleep(7)
    tt4.clear()
    
    tt4.write('Narakam chupinchesthadi santa babu \n papam chesukune athanu ela bathukuthadoo entoo')
    time.sleep(6)
    tt4.clear()


    tt3.write('Ayyooo, Oka doubt \n Why are you pronouncing with "HE"')
    time.sleep(5)
    tt3.clear()

    tt4.write('i too have some serious doubts on that')
    time.sleep(5)
    tt4.clear()


    #Meenakshi
    tt5 = turtle.Turtle()
    tt5.color('Yellow')
    tt5.hideturtle()
    tt5.speed(6)
    tt5.penup()
    
    #tt2.right(180)
    tt5.forward(0)
    tt5.left(90)
    tt5.pendown()
    #tt.right(90)
    tt5.forward(100)
    tt5.right(90)
    tt5.circle(30)
    tt5.right(90)
    tt5.forward(40) #head to hands
    tt5.left(45)
    tt5.forward(60)
    tt5.backward(60)
    tt5.right(90)
    tt5.forward(60)
    tt5.backward(60)
    tt5.right(315)
    tt5.forward(110) #hands to legs
    tt5.left(45)
    tt5.forward(60)
    tt5.backward(60)
    tt5.right(90)
    tt5.forward(60)
    tt5.backward(60)
    tt5.penup()
    tt5.goto(0,60)
    tt5.pendown()
    tt5.write('Meenakshi')

    tt6 = turtle.Turtle()
    tt6.color('yellow')
    tt6.hideturtle()
    
    tt6.penup()
    tt6.goto(0,180)
    tt6.pendown()
    tt6.write('Em matladutunnav Macha')
    time.sleep(5)
    tt6.clear()

    tt4.write('Ayyo sorry meenakshi nuv ekkade vunnav ani teleeka \n Nijam cheppesaa')
    time.sleep(6)
    tt4.clear()

    tt6.write('Nee yenkamma , Cheptha cheptha naku time vasthadi Macha')
    time.sleep(6)
    tt6.clear()

    tt4.write('sorry Meenakshi')
    time.sleep(4)
    tt4.clear()
    tt5.clear()
    
    tt4.write('Santa last gha oka question')
    time.sleep(5)
    tt4.clear()

    tt4.write('Naa Jeevitham lo unna kastalanni, \n Povalante em cheyyali santa ')
    time.sleep(6)
    tt4.clear()

    tt3.write('Ala avvalante 1st nuv over action cheyyadam manali , Automatic gha antha set avthadi')
    time.sleep(6)
    tt3.clear()

    tt3.write('Ok Macha I need to GO,\n will meet you again, \n Always Keep this smile like this \n (i Hope you are smiling now)')
    time.sleep(6)
    tt3.clear()

    tt4.write('Ok santa Bye and Miss u')
    time.sleep(5)
    tt4.clear()
    tt.clear()
    tt2.clear()


    exit_info_turtle = turtle.Turtle()
    exit_info_turtle.color('red')
    exit_info_turtle.hideturtle()
    exit_info_turtle.speed(0)
    exit_info_turtle.penup()
    exit_info_turtle.goto(-300,0)
    exit_info_turtle.pendown()
    exit_info_turtle.write('Humble request andi , \n Yevaru serious gha tesukokandi , \n Just casual gha and fun kosamee chesina, \n if memalni hurt chesi unte im really sorry and im ready to remove this module')
    time.sleep(10)
    exit_info_turtle.clear()

    exit_info_turtle = turtle.Turtle()
    exit_info_turtle.color('red')
    exit_info_turtle.hideturtle()
    exit_info_turtle.speed(0)
    exit_info_turtle.penup()
    exit_info_turtle.goto(-300,0)
    exit_info_turtle.pendown()
    exit_info_turtle.write('Merry Christmas to you and your family , \n #221133')
    time.sleep(10)
    exit_info_turtle.clear()



    print('successfull completed')
    turtle.bye()
    turtle.mainloop()
    return 'Done'


if __name__ ==  '__main__':
    santa_n_Macha()
