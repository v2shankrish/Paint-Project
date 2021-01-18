#Extra Features: SprayPaint, Increase and decrease size, 10 stamps,Undobutton kindof works.
from pygame import *;
from random import*
from math import *
screen=display.set_mode((800,800))
running=True
screen.fill(16777215)
c=0   #Intializing variables for color, radius, and the width of the lines.
r=1
width=5
sprayradius=10
backround=image.load("images/backroundnaruto.png")
backround=transform.scale(backround,(1000,800))
backround=screen.blit(backround,(0,0))

green=image.load("images/green.jpg")
green=transform.scale(green,(50,50))
green=screen.blit(green,(0,500))
draw.rect(screen,0,(0,500,50,50),1)
greenRect=Rect(0,500,50,50)

black=image.load("images/black.jpeg")
black=transform.scale(black,(50,50))
black=screen.blit(black,(50,500))
blackRect=Rect(50,500,50,50)

red=transform.scale(image.load("images/red.jpg"),(50,50))
red=screen.blit(red,(0,550))
redRect=Rect(0,550,50,50)
draw.rect(screen,0,(0,550,50,50),1)

blue=transform.scale(image.load("images/blue.png"),(50,50))
blue=screen.blit(blue,(50,550))
blueRect=Rect(50,550,50,50)
draw.rect(screen,0,(0,550,50,50),1)

white=transform.scale(image.load("images/white.png"),(50,50))
white=screen.blit(white,(0,600))
whiteRect=Rect(0,600,50,50)
draw.rect(screen,0,(0,600,50,50),1)

purple=transform.scale(image.load("images/purple.png"),(50,50))
purple=screen.blit(purple,(50,600))
purpleRect=Rect(50,600,50,50)
draw.rect(screen,0,purple,1)

yellow=transform.scale(image.load("images/yellow.jpg"),(50,50))
yellow=screen.blit(yellow,(0,650))
yellowRect=Rect(0,650,50,50)
draw.rect(screen,0,yellow,1)

eraserlogo=image.load("images/eraser.jpg")
eraserlogo=transform.scale(eraserlogo,(50,50))
eraserlogopos=screen.blit(eraserlogo,(0,50))
eraserRect=Rect(0,50,50,50)
draw.rect(screen,c,(0,50,50,50),1)
    
pencillogo=transform.scale(image.load("images/pencil.jpg"),(50,50))
pencillogopos=screen.blit(pencillogo,(0,0))
pencilRect=Rect(0,0,50,50)
draw.rect(screen,c,(0,0,50,50),1)

spraycan=transform.scale(image.load("images/spraycan.jpg"),(50,50))
spraycanpos=screen.blit(spraycan,(0,100))
spraycanRect=Rect(0,100,50,50)
draw.rect(screen,c,(0,100,50,50),1)

paintbucket=transform.scale(image.load("images/paintbucket.jpg"),(50,50))
paintbucketpos=screen.blit(paintbucket,(50,100))
paintbucketRect=Rect(50,100,50,50)
draw.rect(screen,c,(50,100,50,50),1)

circle=transform.scale(image.load("images/unfilledcircle.png"),(50,50))
circlepos=screen.blit(circle,(0,150))
unfilledellipseRect=Rect(0,150,50,50)
draw.rect(screen,c,(0,150,50,50),1)

unfilledrectangle=image.load("images/unfilledrect.png")
unfilledrectangle=transform.scale(unfilledrectangle,(50,50))
unfilledrectangle=screen.blit(unfilledrectangle,(0,200))
unfilledrectangleRect=Rect(0,200,50,50)
draw.rect(screen,c,(0,200,50,50),1)

line=image.load("images/line.png")
line=transform.scale(line,(50,50))
line=screen.blit(line,(0,250))
lineRect=Rect(50,150,50,50)
draw.rect(screen,0,(0,250,50,50),1)




undobutton=image.load("images/undobutton.jpg")
undobutton=transform.scale(undobutton,(50,50))
undobutton=screen.blit(undobutton,(50,0))
undobuttonRect=Rect(50,0,50,50)
draw.rect(screen,0,(50,0,50,50),1)

redobutton=image.load("images/redobutton.jpg")
redobutton=transform.scale(redobutton,(50,50))
redobutton=screen.blit(redobutton,(50,50))
redobuttonRect=Rect(50,100,50,50)
draw.rect(screen,0,(50,100,50,50),1)

Narutostamp=image.load("images/Narutocoat.png")
Narutostamp=transform.scale(Narutostamp,(50,50))
Narutostamp=screen.blit(Narutostamp,(100,50))
NarutostampRect=Rect(100,50,50,50)
draw.rect(screen,0,(100,50,50,50),1)

Sasukestamp=image.load("images/Sasuke.png")
Sasukestamp=transform.scale(Sasukestamp,(50,50))
Sasukestamp=screen.blit(Sasukestamp,(100,0))
SasukestampRect=Rect(100,0,50,50)
draw.rect(screen,0,(100,0,50,50),1)

kakashistamp=image.load("images/kakashi.png")
kakashistamp=transform.scale(kakashistamp,(50,50))
kakashistamp=screen.blit(kakashistamp,(150,0))
kakashiRect=Rect(150,0,50,50)
draw.rect(screen,0,(150,0,50,50),1)

Jiraiya=image.load("images/Jiraiya.png")
Jiraiya=transform.scale(Jiraiya,(50,50))
Jiraiya=screen.blit(Jiraiya,(150,50))
JiraiyaRect=Rect(150,50,50,50)
draw.rect(screen,0,(150,50,50,50),1)

Itachi=image.load("images/Itachi.png")
Itachi=transform.scale(Itachi,(50,50))
Itachi=screen.blit(Itachi,(200,0))
ItachiRect=Rect(200,0,50,50)
draw.rect(screen,0,(200,0,50,50),1)

rocklee=image.load("images/rocklee.png")
rocklee=transform.scale(rocklee,(50,50))
rocklee=screen.blit(rocklee,(200,50))
rockleeRect=Rect(200,50,50,50)
draw.rect(screen,0,(200,50,50,50),1)

neji=image.load("images/neji.jpg")
neji=transform.scale(neji,(50,50))
neji=screen.blit(neji,(250,0))
nejiRect=Rect(250,0,50,50)
draw.rect(screen,0,(250,0,50,50),1)

minato=image.load("images/minato.png")
minato=transform.scale(minato,(50,50))
minato=screen.blit(minato,(250,50))
minatoRect=Rect(250,50,50,50)
draw.rect(screen,0,(250,50,50,50),1)

ninetails=image.load("images/ninetails.png")
ninetails=transform.scale(ninetails,(50,50))
ninetails=screen.blit(ninetails,(300,0))
ninetailsRect=Rect(300,0,50,50)
draw.rect(screen,0,(300,0,50,50),1)

shikamaru=image.load("images/shikamaru.png")
shikamaru=transform.scale(shikamaru,(50,50))
shikamaru=screen.blit(shikamaru,(300,50))
shikamaruRect=Rect(300,50,50,50)
draw.rect(screen,0,(300,50,50,50),1)

ellipse=image.load("images/ellipse.png")
ellipse=transform.scale(ellipse,(50,50))
ellipse=screen.blit(ellipse,(50,150))
ellipseRect=Rect(50,150,50,50)


rectangle=image.load("images/rectangle.png")
rectangle=transform.scale(rectangle,(50,50))
rectangle=screen.blit(rectangle,(50,200))
rectangleRect=Rect(50,200,50,50)


savebutton=image.load("images/savebutton.png")
savebutton=transform.scale(savebutton,(50,50))
savebutton=screen.blit(savebutton,(50,250))
savebuttonRect=Rect(50,250,50,50)
draw.rect(screen,0,(50,250,50,50),1)

load=transform.scale(image.load("images/load.jpg"),(50,50))
screen.blit(load,(0,250))
loadRect=Rect(0,250,50,50)


plussign=image.load("images/plussign.jpg")
plussign=transform.scale(plussign,(50,50))
plussign=screen.blit(plussign,(0,300))
plussignRect=Rect(0,300,50,50)
draw.rect(screen,0,(0,300,50,50),1)

minussign=image.load("images/minussign.jpg")
minussign=transform.scale(minussign,(50,50))
minussign=screen.blit(minussign,(50,300))
minussignRect=Rect(50,300,50,50)
draw.rect(screen,0,(50,300,50,50),1)

tool="pencil"
draw.rect(screen,16777215,(100,100,700,700))
undolist=[]
redolist=[]

def getName(screen,showFiles):
    ans = ""                    # final answer will be built one letter at a time.
    arialFont = font.SysFont("Times New Roman", 16)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(5,5,200,25) # make changes here.

    if showFiles:
        pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
        n = len(pics)
        choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
        draw.rect(screen,(220,220,220),choiceArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),choiceArea,1)        # draw the text window and the text.
        for i in range(n):
            txtPic = arialFont.render(pics[i], True, (0,111,0))   #
            screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            before=screen.subsurface(canvasRect).copy()
            startx,starty=mx,my
           
            if eraserRect.collidepoint(mx,my): # just changing the tools. Checking if the mouse is on the picture, and also checking if the mouse is being pressed down.
                tool="eraser"
    
            if pencilRect.collidepoint(mx,my):
                tool="pencil"
            if spraycanRect.collidepoint(mx,my):
                tool="spraycan"

            if paintbucketRect.collidepoint(mx,my):
                tool="paintbucket"
            if unfilledrectangleRect.collidepoint(mx,my):
                tool="rectangle-unfilled"
            if unfilledellipseRect.collidepoint(mx,my):
                tool="unfilled-ellipse"
            if ellipseRect.collidepoint(mx,my):
                tool="ellipse"
            if rectangleRect.collidepoint(mx,my):
                tool="rectangle"
            if savebuttonRect.collidepoint(mx,my):
                if mb[0]==1:
                    image.save(screen.subsurface(canvasRect),"myPic.png")
            if loadRect.collidepoint(mx,my):
                if mb[0]==1:
                    txt = getName(screen,False)                     # this is how you would call my getName function
                    txtPic = comicFont.render(txt, True, (255,0,0))
                    screen.blit(txtPic,(100,100))

            if undobuttonRect.collidepoint(mx,my):
                if len(undolist) > 0:#see if the list has at more than one element.
                    redolist.append(undolist.pop())  # adding last action to redo list
            
                    Surface.unlock(undolist[-1])
                    screen.blit(undolist[-1], (100, 100))#blits the last item to the screen
            if redobuttonRect.collidepoint(mx,my):
                if len(redolist)>0:
            
                    screen.blit(redolist[0],(100,100))
                    redolist=[]
            if NarutostampRect.collidepoint(mx,my):
                tool="Narutostamp"

            if SasukestampRect.collidepoint(mx,my):
                tool="Sasukestamp"
            if kakashiRect.collidepoint(mx,my):
                tool="kakashistamp"
            if JiraiyaRect.collidepoint(mx,my):
                tool="Jiraiyastamp"
            if ItachiRect.collidepoint(mx,my):
                tool="Itachistamp"
            if rockleeRect.collidepoint(mx,my):
                tool="rockleestamp"
            if nejiRect.collidepoint(mx,my):
                tool="nejistamp"
            if minatoRect.collidepoint(mx,my):
                tool="minatostamp"
            if ninetailsRect.collidepoint(mx,my):
                tool="ninetailstamp"
            if shikamaruRect.collidepoint(mx,my):
                tool="shikamarustamp"

            if greenRect.collidepoint(mx,my):
                c=(50,205,50)
            if blackRect.collidepoint(mx,my):
                c=0
            if redRect.collidepoint(mx,my):
                c=(255,0,0)
            if blueRect.collidepoint(mx,my):
                c=(0,0,255)
            if whiteRect.collidepoint(mx,my):
                c=16777215
            if purpleRect.collidepoint(mx,my):
                c=(128,0,128)
            if yellowRect.collidepoint(mx,my) :
                c=(255,255,0)

            if plussignRect.collidepoint(mx,my):
                r=r+1
                sprayradius+=5
                width=width+5
                if r==11:         #Dont want the tools getting too large.
                    r=r-1
            if minussignRect.collidepoint(mx,my):
                r=r-1
                sprayradius-=5
                width=r+5
                if r==0:
                    r=r+1
                    width=width+4
                if sprayradius==0:
                    sprayradius+=5


            if e.button==3:
                image.save(screen.subsurface(canvasRect),"myPic.png")
        if e.type == MOUSEBUTTONUP:#if the mouse is up
            if e.button == 1:#if the mouse is clicked and its on the canvas
                screenCopy = screen.subsurface(canvasRect).copy()#takes a picture of the canvas rect
                undolist.append(screenCopy)#appends that into the undo list
                #clears redo list
    print(redolist)
    mx,my=mouse.get_pos()
    
    mb=mouse.get_pressed()
   


    if tool=="pencil":         #If the tool is the pencil, it will draw a circle where the mouse is click
        if mb[0]==1:            # and draw a line connecting the circles that are drawn.
            draw.circle(screen,c,(mx,my),r)
            draw.line(screen,c,(mx,my),(omx,omy),width)
            draw.rect(screen,(0,0,255),(0,0,50,50),1)
    if tool=="eraser":       #My eraser is just a white pencil.
        if mb[0]==1:
            draw.circle(screen,16777215,(mx,my),r)
            draw.line(screen,16777215,(mx,my),(omx,omy),width)
    
    if tool=="rectangle-unfilled":
        if mb[0]==1:            #If the mouse is pressed down, then a rectangle will be drawn
            screen.blit(before, (100, 100))#from where the mouse was clicked to where it was dropped.Startx
            # starty is where is was clicked, and mx,my is where it was dropped. We take a picture of the screen and 
            draw.rect(screen, (c), (startx, starty, mx-startx, my-starty), r)#blit it onto the canvas to prevent multiple rectangles being drawn at the same time.
    
    if tool=="unfilled-ellipse":
        if mb[0]==1:
            try: # the program tries what is indented.
                if startx<mx and starty<my:# We use these if statements checking which is larger so that we know which point we should start drawing the ellipse from.
                    screen.blit(before, (100, 100)) 
                    # we use the absolute value because of the ellipse cant have a negative radius.
                    ellipse = Rect(startx, starty, abs(startx - mx), abs(starty - my))  
                    ellipse.normalize()
                    draw.ellipse(screen, (c), (ellipse), r)
                if startx>mx and starty>my:
                    screen.blit(before,(100,100))
                    ellipse=Rect(mx,my,abs(mx-startx),abs(my-starty))
                    ellipse.normalize()
                    draw.ellipse(screen,(c),(ellipse),r)
                if startx>mx and starty<my:
                    screen.blit(before,(100,100))
                    ellipse=Rect(mx,starty,abs(mx-startx), abs(starty-my))
                    ellipse.normalize()
                    draw.ellipse(screen,c,(ellipse),r)
                if startx<mx and starty>my:
                    screen.blit(before,(100,100))
                    ellipse=Rect(startx,my,abs(startx-mx),abs(my-starty))
                    ellipse.normalize()
                    draw.ellipse(screen,(c),(ellipse),r)
            except: # For somereason, if i tried to draw an ellipse here, the program would crash. But if i didnt use the try and except then the program would again crash.
                r=r  # so I just put something that wouldnt change the code here.

    if tool=="rectangle":
        if mb[0]==1:
            screen.blit(before, (100, 100))
            if startx<mx and starty<my:# same things going on here as with the ellipse. We are trying to check which is larger so that we know which point we should draw the rectangle from.
                    screen.blit(before, (100, 100)) 
            
                    rect = Rect(startx, starty, abs(startx - mx), abs(starty - my))  
                    rect.normalize()
                    draw.rect(screen, (c), (rect))
            if startx>mx and starty>my:
                    screen.blit(before,(100,100))
                    rect=Rect(mx,my,abs(mx-startx),abs(my-starty))
                    rect.normalize()
                    draw.rect(screen,(c),(rect))
            if startx>mx and starty<my:
                    screen.blit(before,(100,100))
                    rect=Rect(mx,starty,abs(mx-startx), abs(starty-my))
                    rect.normalize()
                    draw.rect(screen,c,(rect))
            if startx<mx and starty>my:
                    screen.blit(before,(100,100))
                    rect=Rect(startx,my,abs(startx-mx),abs(my-starty))
                    rect.normalize()
                    draw.rect(screen,(c),(rect))
    if tool=="ellipse": 
        if mb[0]==1:
            try: # sane concept as the ellipse.
                if startx<mx and starty<my:
                    screen.blit(before, (100, 100)) 
            
                    ellipse = Rect(startx, starty, abs(startx - mx), abs(starty - my))  
                    ellipse.normalize()
                    draw.ellipse(screen, (c), (ellipse))
                if startx>mx and starty>my:
                    screen.blit(before,(100,100))
                    ellipse=Rect(mx,my,abs(mx-startx),abs(my-starty))
                    ellipse.normalize()
                    draw.ellipse(screen,(c),(ellipse))
                if startx>mx and starty<my:
                    screen.blit(before,(100,100))
                    ellipse=Rect(mx,starty,abs(mx-startx), abs(starty-my))
                    ellipse.normalize()
                    draw.ellipse(screen,c,(ellipse))
                if startx<mx and starty>my:
                    screen.blit(before,(100,100))
                    ellipse=Rect(startx,my,abs(startx-mx),abs(my-starty))
                    ellipse.normalize()
                    draw.ellipse(screen,(c),(ellipse))
            except:
                draw.ellipse(screen, (c), (ellipse))

    if tool=="paintbucket": 
        if mb[0]==1 and mx>100 and my>100: #checks if the mouse is on the canvas and then fills the screen with the desired color.
            screen.fill(c)
    if tool=="spraycan":
        if mb[0]==1:
            length=randint(-sprayradius,sprayradius) #The spray can will draw circles in at a random position, that is within a certain distance from where the mouse was clicked.
            width=randint(-sprayradius,sprayradius)
            draw.circle(screen,c,(mx+length,my+width),3)

    if tool=="Narutostamp": # All the stamps have the same concept. If the mouse is clicked on the screen, it will blit the image where the mouse was clicked.
        Narutostamp=transform.scale(image.load("images/Narutocoat.png"),(100,100))
        if mb[0]==1 and mx>100 and my>100:
            screen.blit(before,(100,100))
            screen.blit(Narutostamp,(mx,my))

    if tool=="Sasukestamp":
        Sasukestamp=transform.scale(image.load("images/Sasuke.png"),(100,100))
        if mb[0]==1 and mx>100 and my>100:
            screen.blit(before,(100,100))
            screen.blit(Sasukestamp,(mx,my))

    if tool=="kakashistamp":
        kakashistamp=transform.scale(image.load("images/kakashi.png"),(100,100))
        if mb[0]==1 and mx>100 and my>100:
            screen.blit(before,(100,100))
            screen.blit(kakashistamp,(mx,my))
    
    if tool=="Jiraiyastamp":
        Jiraiya=transform.scale(image.load("images/Jiraiya.png"),(100,100))
        if mb[0]==1 and mx>100 and my>100:
            screen.blit(before,(100,100))
            screen.blit(Jiraiya,(mx,my))

    if tool=="Itachistamp":
        Itachi=transform.scale(image.load("images/Itachi.png"),(100,100))
        if mb[0]==1 and mx>100 and my>100:
            screen.blit(before,(100,100))  # this line stops the stamp from printing multiple stamps when you drag the mous.
            screen.blit(Itachi,(mx,my))
    if tool=="rockleestamp":
        rocklee=transform.scale(image.load("images/rocklee.png"),(100,100))
        if mb[0]==1 and mx>100 and my>100:
            screen.blit(before,(100,100))
            screen.blit(rocklee,(mx,my))
    if tool=="nejistamp":
        neji=transform.scale(image.load("images/neji.jpg"),(100,100))
        if mb[0]==1 and mx>100 and my>100:
            screen.blit(before,(100,100))
            screen.blit(neji,(mx,my))
            
    if tool=="minatostamp":
        minato=transform.scale(image.load("images/minato.png"),(100,100))
        if mb[0]==1 and mx>100 and my>100:
            screen.blit(before,(100,100))
            screen.blit(minato,(mx,my))

    if tool=="ninetailstamp":
        ninetails=transform.scale(image.load("images/ninetails.png"),(100,100))
        if mb[0]==1 and  mx>100 and my>100:
            screen.blit(before,(100,100))
            screen.blit(ninetails,(mx,my))
    if tool=="shikamarustamp":
        shikamaru=transform.scale(image.load("images/shikamaru.png"),(100,100))
        if mb[0]==1 and mx>100 and my>100:
            screen.blit(before,(100,100))
            screen.blit(shikamaru,(mx,my))
    

    canvasRect=(100,100,700,700)
    
    screen.set_clip(canvasRect)
    omx,omy=mx,my
    
    display.flip()
quit()
