import turtle
import math



win=turtle.Screen()
win.bgcolor('black')
win.title('game')
win.setup(700,700)



class Zoubuliao(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)



class Wanjia(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('blue')
        self.penup()
        self.speed(0)
        self.hp=9999
        self.gold=0


    def xiangShangZou(self):
        if (self.xcor(),self.ycor()+24) not in walls:
            self.goto(self.xcor(),self.ycor()+24)

    def xiangXiaZou(self):
        if (self.xcor(), self.ycor()-24) not in walls:
            self.goto(self.xcor(),self.ycor()-24)

    def xiangZuoZou(self):
        if (self.xcor()-24, self.ycor()) not in walls:
            self.goto(self.xcor()-24,self.ycor())
    def xiangYouZou(self):
        if (self.xcor()+24, self.ycor()) not in walls:
            self.goto(self.xcor()+24,self.ycor())

    def jiechu(self,qita):
        a=self.xcor()-qita.xcor()
        b=self.ycor()-qita.ycor()
        juli=math.sqrt((a*a)+(b*b))

        if juli<5:
            return 1
        else:
            return 0



class Guaiwu(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('red')
        self.penup()
        self.speed(0)
        self.hp=100
        self.gold=50
        self.goto(x,y)
        self.fangxiang=''


    def chouhen(self,qita):
        a=self.xcor()-qita.xcor()
        b=self.ycor()-qita.ycor()
        juli=math.sqrt((a*a)+(b*b))

        if juli<75:
            return 1
        else:
            return 0


    def yidong(self):
        if self.chouhen(wanjia):
            if wanjia.xcor()<self.xcor():
                self.fangxiang='zuo'

            elif wanjia.xcor()>self.xcor():
                self.fangxiang='you'
            elif wanjia.ycor()<self.ycor():
                self.fangxiang='xia'
            elif wanjia.ycor()>self.ycor():
                self.fangxiang='shang'

        if self.fangxiang is 'shang':
            dx=0
            dy=24
        elif self.fangxiang is 'xia':
            dx=0
            dy=-24
        elif self.fangxiang is 'zuo':
            dx=-24
            dy=0
        elif self.fangxiang is 'you':
            dx=24
            dy=0
        else:
            dx=0
            dy=0

        if (self.xcor()+dx, self.ycor()+dy) not in walls:
            self.goto(self.xcor()+dx,self.ycor()+dy)

        win.ontimer(self.yidong,200)





    def cuihui(self):
        self.goto(999,999)
        self.hideturtle()



class Baozang(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('gold')
        self.penup()
        self.speed(0)
        self.gold=100
        self.goto(x,y)

    def cuihui(self):
        self.goto(999,999)
        self.hideturtle()


ditu=['']
walls=[]

ditu1=[
    #25*25个
    'xxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxx  xxxxxxxxxxxxxxbxx',
    'xxxxxxx xxxxxxxxxxxxxx xx',
    'xxxx        xxxxxxxxxx xx',
    'xxxx xxxxxx xxxxxxxxxx xx',
    'xxxx xxxxxx xxxxxxxxxx xx',
    'xxxx xxxxxx x xxxxxxxx xx',
    'xb  gbxxxxx   xxxxxxxx xx',
    'xxxxxxxxxxxxx xxxxxxxxgxx',
    'xxxxxxxxxxxxx xxxxxxxxgxx',
    'xxxxxxxxxxxxw     bxxx xx',
    'xxxxxxxxxxxxxxxxx xxxxgxx',
    'xxxxxxxxxxxxxxxxx xxxx xx',
    'xxxxxxxxxxxx      xxxx xx',
    'xxxxxxxxxxxx xxxxxxxxx xx',
    'xxxxxxxxxxxb xxxxxxxxx xx',
    'xxxxxxxxxxxx xxxxxxxxx xx',
    'xxg          xxxxxxxxx bx',
    'xxxxxxxxxx xxxxxxxxxxx xx',
    'xxxxxxxxxx xxxxxxxxxxx xx',
    'xxxxxxxxxx             gx',
    'xxxxxxxxxx xxxxxxxxxxxxxx',
    'xx         xxxxxxxxxxxxxx',
    'xxxxxxxxxxgxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxx'

]

ditu.append(ditu1)


def setup(ditu):
    for y in range(len(ditu)):
        for x in range(len(ditu[y])):
            character=ditu[y][x]
            screen_x=-288+(x*24)
            screen_y=288-(y*24)
            if character is 'x':
                qiang.goto(screen_x,screen_y)
                qiang.stamp()
                walls.append((screen_x,screen_y))

            if character is "w":
                wanjia.goto(screen_x,screen_y)

            if character is 'b':
                baozang.append(Baozang(screen_x,screen_y))

            if character is 'g':
                guaiwu.append(Guaiwu(screen_x,screen_y))


qiang=Zoubuliao()
wanjia=Wanjia()
baozang=[]
guaiwu=[]




win.tracer(0)

setup(ditu[1])


win.listen()
win.onkey(wanjia.xiangShangZou,'w')
win.onkey(wanjia.xiangXiaZou,'s')
win.onkey(wanjia.xiangZuoZou,'a')
win.onkey(wanjia.xiangYouZou,'d')


for z in guaiwu:
    win.ontimer(z.yidong(),200)


while 1:
    for x in baozang:
        if wanjia.jiechu(x):
            wanjia.gold+=x.gold
            print("人物金币："+str(wanjia.gold))
            x.cuihui()
            baozang.remove(x)

    for y in guaiwu:
        if wanjia.jiechu(y):
            wanjia.hp -= y.hp
            wanjia.gold+=y.gold
            print('人物血量：'+str(wanjia.hp))
            y.cuihui()
            guaiwu.remove(y)




    win.update()





