#drawing with python
import pyautogui
import time
import random
# open paint and put it in the left , also move all the python window to the right
def ra(p,d,border):
    a=random.choice(range(0,10000))
    if a<(p*100):
        xmin=10+d
        xmax=1560-d
        ymin=150+d
        ymax=800-d
        if border==1: #starts at upper left 
            xmin=10
            ymin=150
        elif border==2: #starts at upper right 
            xmax=1560
            ymin=150
        elif border==3: #starts at lower left
            xmin=10
            ymax=800
        elif border==4: #starts at lower right
            xmax=1560
            ymax=800
        if xmin<xmax and ymin<ymax:
            x=random.choice(range(xmin,xmax))
            y=random.choice(range(ymin,ymax))
            pyautogui.moveTo(x,y)
    return
    
def ra2(p,d,border):
    a=random.choice(range(0,10000))
    if a<(p*100):
        xmin=10+d
        xmax=1560-d
        ymin=150+d
        ymax=800-d
        if border==1: #starts at upper left 
            xmin=10
            ymin=150
        elif border==2: #starts at upper right 
            xmax=1560
            ymin=150
        elif border==3: #starts at lower left
            xmin=10
            ymax=800
        elif border==4: #starts at lower right
            xmax=1560
            ymax=800
        if xmin<xmax and ymin<ymax:
            x=random.choice(range(xmin,xmax))
            y=random.choice(range(ymin,ymax))
            pyautogui.moveTo(x,y)
            return False
        else:
            return True
    else :
        return True
    


pyautogui.click(243,70)
pyautogui.click(243,70)
time.sleep(0.1)
pyautogui.click(150,200)

d=500
def draw(d):
    pyautogui.dragRel( d , 0 )
    while d>0:
        pyautogui.dragRel( 0 , d )
        pyautogui.dragRel( -d , 0 )
        pyautogui.dragRel( 0 , (5-d) )
        pyautogui.dragRel( (d-5) , 0)

        d-=10
    return


def draw2(d,b):
    pyautogui.dragRel( d , 0 )
    while d>0:
        pyautogui.dragRel( 0 , d )
        pyautogui.dragRel( -d , 0 )
        pyautogui.dragRel( 0 , (b-d) )
        pyautogui.dragRel( (d-b) , 0)

        d-=(2*b)
    return


def drawRan(d,b,p):
    pyautogui.dragRel( d , 0 )
    a=0
    a=p/4
    while d>0:
        pyautogui.dragRel( 0 , d )
        ra(a,d,4)
        pyautogui.dragRel( -d , 0 )
        ra(a,d,3)
        pyautogui.dragRel( 0 , (b-d) )
        ra(a,d,1)
        pyautogui.dragRel( (d-b) , 0)
        ra(a,d,2)
        d-=(2*b)
    return


def drawRand(d,b,p):
    pyautogui.dragRel( d , 0 )
    a=0.0
    a=p/4
    sq=True
    while d>0:
        pyautogui.dragRel( 0 , d )
        if sq:
            sq=ra2(a,d,4)
        pyautogui.dragRel( -d , 0 )
        if sq:
            sq=ra2((a*2),d,3)
        pyautogui.dragRel( 0 , (b-d) )
        if sq:
            sq=ra2((a*3),d,1)
        pyautogui.dragRel( (d-b) , 0)
        if sq:
            sq=ra2(p,d,2)
        d-=(2*b)
        sq=True
    return



def drawRandom(d,b,p):
    pyautogui.dragRel( d , 0 )
    a=0.0
    a=p/4
    sq=True
    sc=4
    while d>0:
        pyautogui.dragRel( 0 , d )
        sc-=1
        if sq and sc==0:
            sq=ra2(p,d,4)
            sc=4
        pyautogui.dragRel( -d , 0 )
        sc-=1
        if sq and sc==0:
            sq=ra2((p),d,3)
            sc=4
        pyautogui.dragRel( 0 , (b-d) )
        sc-=1
        if sq and sc==0:
            sq=ra2((p),d,1)
            sc=4
        pyautogui.dragRel( (d-b) , 0)
        sc-=1
        if sq and sc==0:
            sq=ra2(p,d,2)
            sc=4
        d-=(2*b)
        sq=True
    return



def loop(a,b):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    while a>0:
        draw(b)
        a-=1
        time.sleep(2)
    return


def loops(loops,size,density):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    while loops>0:
        
        draw2(size,density)
        loops-=1
        time.sleep(2)
    return

def RandLoop1(loops,size,density):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    while loops>0:
        draw2(size,density)
        ra(100,size,1)
        loops-=1
        time.sleep(3)
    return


def RandLoop2(loops):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    while loops>0:
        drawRan(300,5,0)
        ra(100,300,1)
        loops-=1
        
    return


def Ram(loops):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    size,density,p=0,0,0
    while loops>0:
        size=random.choice(range(50,400))
        density=random.choice([3,4,5,6,7,8])
        p=random.choice(range(4,25))
        ra(100,size,1)
        drawRan(size,density,p)
        loops-=1
        time.sleep(3)
    return

def Ram2(loops):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    size,density,p=0,0,0
    while loops>0:
        size=random.choice(range(50,400))
        density=random.choice([3,4,5,6,7,8])
        p=random.choice(range(4,25))
        ra(100,size,1)
        drawRandom(size,density,p)
        ra(100,size,1)
        draw2(size,density)
        loops-=1
        time.sleep(3)
    return

def Ram3(loops):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    size,density,p=0,0,0
    while loops>0:
        size=random.choice(range(50,400))
        density=random.choice([3,4,5,6,7,8])
        p=random.choice(range(0,20))
        ra(100,size,1)
        drawRandom(size,density,p)
        loops-=1
        time.sleep(3)
    return
    
print(d)

#pyautogui.dragRel( 400 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , 400 ,duration=0.01)
#pyautogui.dragRel( -400 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , -350 ,duration=0.01)
#pyautogui.dragRel( 350 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , 300 ,duration=0.01)
#pyautogui.dragRel( -300 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , -250 ,duration=0.01)
#pyautogui.dragRel( 250 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , 200 ,duration=0.01)
#pyautogui.dragRel( -200 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , -150 ,duration=0.01)
#pyautogui.dragRel( 150 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , 100 ,duration=0.01)
#pyautogui.dragRel( -100 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , -80 ,duration=0.01)
#pyautogui.dragRel( 80 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , 60 ,duration=0.01)
#pyautogui.dragRel( -60 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , -40 ,duration=0.01)
#pyautogui.dragRel( 40 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , 20 ,duration=0.01)
#pyautogui.dragRel( -20 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , -10 ,duration=0.01)
#pyautogui.dragRel( 10 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , 5 ,duration=0.01)
#pyautogui.dragRel( -5 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , -4 ,duration=0.01)
#pyautogui.dragRel( 4 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , 3 ,duration=0.01)
#pyautogui.dragRel( -3 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , -2 ,duration=0.01)
#pyautogui.dragRel( 2 , 0 ,duration=0.01)
#pyautogui.dragRel( 0 , 1 ,duration=0.01)
