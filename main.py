from pygame_functions import *


screenSize(600,600)
setAutoUpdate(False)


debuggingInfo = makeLabel("debug",20,10,10,"white","Arial")
showLabel(debuggingInfo)

class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.height=50
        self.width=50
        self.speed = 5
        self.sprite = makeSprite("smallLinks.png",32)  # links.gif contains 32 separate self.frames of animation. Sizes are automatically calculated.
        self.nextframe = clock()
        self.frame=0
        moveSprite(self.sprite,300,300,True)
        showSprite(self.sprite)

    def move(self,wallmap):
        moved=False
        nextx = self.x
        nexty = self.y
        if clock() > self.nextframe:                         # We only animate our character every 80ms.
            self.frame = (self.frame+1)%8                         # There are 8 self.frames of animation in each direction
            self.nextframe += 80  
        if keyPressed("d"):
            moved=True
            nextx += 5
            checkPoints = [(self.x+20, self.y+20),(self.x+20,self.y-20)]
            changeSpriteImage(self.sprite, 0*8+self.frame)    # 0*8 because right animations are the 0th set in the sprite sheet
        elif keyPressed("s"):
            moved=True
            nexty +=5
            checkPoints = [(self.x-15, self.y+30),(self.x+15,self.y+30)]
            changeSpriteImage(self.sprite, 1*8+self.frame)    # down facing animations are the 1st set
        elif keyPressed("a"):
            nextx -=5
            moved=True
            checkPoints = [(self.x-20, self.y-20),(self.x-20,self.y+20)]
            changeSpriteImage(self.sprite, 2*8+self.frame)    # and so on
        elif keyPressed("w"):
            nexty -=5
            moved=True
            checkPoints = [(self.x-15, self.y-30),(self.x+15,self.y-30)]
            changeSpriteImage(self.sprite,3*8+self.frame)
        # check background
        if moved:
            for point in checkPoints:
                colour = getPixel(wallmap,point[0], point[1])
                if colour[:3] == (255,255,255):
                    moved = False
        if moved: 
            self.x = nextx
            self.y = nexty
        else:
            changeSpriteImage(self.sprite, 1 * 8 + 5)  # the static facing front look

        changeLabel(debuggingInfo,str(self.x) + ":" + str(self.y))


wallmap = makeSprite("walls.png")

background = makeSprite("background.png")
showSprite(background)
showSprite(wallmap)
p = Player(100,100)
while True:
    p.move(wallmap)
    moveSprite(wallmap, 300-p.x, 300-p.y)
    updateDisplay()
    tick(60)
endWait()
