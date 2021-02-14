add_library("sound")

import random
import BallClass
import BrickClass
key_mode = 1
padpos= -10 
padpos1 = 350
prev_padpos = 0
score = 0
game_won = False
high_score = 0


import random
    
BrickColour = 255
t= -750
y= -750 


def restart():
    global sound_file
    global ball, Bricks, game_won, score, key_mode , imgWin
    word = 'bbbbbbbbbbrrrrrrrrrrrbbbbbbbbbbrrrrrrrrrbrbbbbbbbbbbbrrrrrrrrrrrbbbbbbbbbbbbbbrrrrrrrrbbbbbbbbbbbb'
    #word = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaar'   
    word_num = 0
    for i in range(14):
        for j in range(8):
            brick1 = BrickClass.Brick(10 + i*48, 70+j*20, 48, 20, word[word_num])
            Bricks.append(brick1)
            word_num +=1
            if word_num == len(word):
                word_num = 0
    ball = BallClass.Ball(300, 515)
    game_won = False
    score = 0
    padpos1 = 350
    key_mode = 1
    
    
    

def setup():
    global sound_file
    #word = 'bbbbbbbbbbrrrrrrrrrrrbbbbbbbbbbrrrrrrrrrbrbbbbbbbbbbbrrrrrrrrrrrbbbbbbbbbbbbbbrrrrrrrrbbbbbbbbbbbb'   
    #word_num = 0
    size(700, 600)
    background(50)
    global ball ,imgBG , imgTop, imgBot, imgPaddle, imgWin
    global Bricks , img, t, y , imgStart , imgGameOver
    Bricks = []
    imgTop = loadImage("Top.png")
    imgBot = loadImage("Bottom.png")
    imgBG = loadImage("GlowBack.png")
    imgPaddle = loadImage("Paddle.png")
    imgStart = loadImage("Start.png")
    imgWin = loadImage("youwin.png")
    imgGameOver = loadImage("GameOver.png")
    restart()
    img = loadImage("BlackBackground8.png")
    #Bricks[10].erase()
    image(imgStart,0,0)
    sound_file = SoundFile(this, "sound.mp3")
    sound_file.play()
    
def paddle():
    image(imgPaddle, padpos - 350 ,280)
    #fill(255)
    #circle(padpos , 560 , 20)
   # circle(padpos + 20 , 560, 20)
    #rect(padpos, 550 , 20 , 20)    
    
def draw():
    global sound_file
    global ball, prev_padpos, score, game_won, high_score , imgWin
    global Bricks , imgBG , imgStart , imgGameOver, frame_count_won
    global padpos1 , img, t, y , key_mode, sound_file
    background(0, 0, 0)
    image(imgBG,0,0)
    fill(100)
    rect(-1,0, width+1, 30)
    if (not game_won) and (not ball.game_over):    
        
        prev_padpos = padpos1
        count = 0
        #Bricks[random.randint(0, 79)].erase()
        
        
                
                
                
        '''for i in range(len(Bricks)):
            if Bricks[i].hit_test(ball.pos_x, ball.pos_y):
                if Bricks[i].bottom_hit_test(ball.pos_x, ball.pos_y):
                    ball.dy *= -1
                else:
                    ball.dx *= -1
                score += Bricks[i].points
                Bricks[i].erase()    
            Bricks[i].draw()
            if Bricks[i].active:
                count += 1'''
        for brick in Bricks:
            if brick.active:
                count += 1
                brick.draw()
                    
        if count == 0:
            game_won = True
            frame_count_won = frameCount
    #Ball release with spacebar        
        t = ball.pos_x - 1000
        y = ball.pos_y - 1000
            
        if keyPressed:
                key_mode = 1
                if ball.dx == 0 and key == " ":
                    ball.dx = sqrt(ball.speed/2)
                    ball.dy = -1 *  ball.dx
        #Ball release with mouse        
        if mousePressed:
                key_mode = 0
                if ball.dx ==0:
                    ball.dx = sqrt(ball.speed/2)
                    ball.dy = -1 *  ball.dx
        if key_mode == 0:
                padpos1 = mouseX        
        
            #ball.pos_x = mouseX
            #ball.pos_y = mouseY
        
        #Paddle Movement left and right with keys    
        if key_mode == 1:     
                if keyPressed:
                    if keyCode == LEFT:
                        padpos1 = padpos1 - 10
                        
                    if keyCode == RIGHT:
                        padpos1 = padpos1 + 10
        #Limit Paddle Movement to keep within the frame along x axis                
        if padpos1 >= 670: 
                padpos1 = 665                
        if padpos1 <= 30: 
                padpos1 = 43
    
        #Locking Ball to paddle when ball x position is at 0    
        if ball.dx ==0:
            ball.pos_x = padpos1
        image(img, int(t), int(y))
        image(imgTop,0,-20)
        
        ball.draw(padpos1 - prev_padpos)    
        pushMatrix()
        #padpos1 = 100
        translate(padpos1,0)       
        paddle()
        popMatrix()
        ball.padpos = padpos1    
        #print(padpos1)
        #print(ball.pos_x)
        #print(ball.pos_y)
        textSize(16)
        text('score', width/2 - 25, 20)
        text(score, width/2 + 25, 20)
        image(imgBot,0,0)
        
        
        for brick in Bricks:
            if brick.active:
                if brick.hit_test(ball.pos_x, ball.pos_y - ball.sz):
                    brick.active = False
                    score += brick.points
                    ball.dy = -ball.dy
                    break
                if brick.hit_test(ball.pos_x, ball.pos_y + ball.sz):
                    brick.active = False
                    score += brick.points
                    ball.dy = -ball.dy
                    break
                if brick.hit_test(ball.pos_x - ball.sz, ball.pos_y):
                    brick.active = False
                    score += brick.points
                    ball.dx = -ball.dx
                    break
                if brick.hit_test(ball.pos_x + ball.sz, ball.pos_y):
                    brick.active = False
                    score += brick.points
                    ball.dx = -ball.dx
                    break
                    # Now test the other parts of the ball
                            
                    # Collision detection type 2:
                    # Bottom right corner
                    
                    if ball.hit_test(brick.pos_x + brick.w, brick.pos_y + brick.h):
                        brick.active = False
                        score += brick.points
                        if ball.dx <= 0 and ball.dy <= 0:
                            ball.dx, ball.dy = -ball.dy, -ball.dx
                        else:
                            if ball.dx > 0:
                                ball.dy *= -1
                            else:
                                if ball.dy > 0:
                                    ball.dx *= -1
                        break
                    
                    #Top left corner
                    if ball.hit_test(brick.pos_x, brick.pos_y):
                        brick.active = False
                        score += brick.points
                        if ball.dx >= 0 and ball.dy >= 0:
                            ball.dx, ball.dy = -ball.dy, -ball.dx
                        else:
                            if ball.dx < 0:
                                ball.dy *= -1
                            else:
                                if ball.dy < 0:
                                    ball.dx *= -1
                        break
                    #Top right corner
                    if ball.hit_test(brick.pos_x + brick.w, brick.pos_y):
                        brick.active = False
                        score += brick.points
                        if ball.dx <= 0 and ball.dy >= 0:
                            ball.dx, ball.dy = ball.dy, ball.dx
                        else:
                            if ball.dx > 0:
                                ball.dy *= -1
                            else:
                                if ball.dy < 0:
                                    ball.dx *= -1
                                
                        break
                    #Botoom left corner
                    if ball.hit_test(brick.pos_x, brick.pos_y + brick.h):
                        brick.active = False
                        score += brick.points
                        if ball.dx >= 0 and ball.dy <= 0:
                            ball.dx, ball.dy = ball.dy, ball.dx
                        else:
                            if ball.dx < 0:
                                ball.dy *= -1
                            else:
                                if ball.dy > 0:
                                    ball.dx *= -1
                        break
        
        #ball.game_over = True
        #ball.frame_count_lose = frameCount    
    else: #when the game is over:
        if high_score < score:
            high_score = score
        textSize(72)
        fill(255)
        if game_won: #the victory screen
            if frameCount - frame_count_won > 300:
                image(imgStart,0,0)
                between_x = mouseX > 250 and mouseX < 450
                between_y = mouseY > 400 and mouseY < 460
                if mousePressed and between_x and between_y:
                    restart()
            else:
                image(imgWin, 0 , 0 )
                
            #text('you won', 110, 150)
            #text('your score', 75, 275)
            #text(score, 190, 400)
        if ball.game_over: #the loose screen
            if frameCount - ball.frame_count_lose > 300:
                image(imgStart,0,0)
                between_x = mouseX > 250 and mouseX < 450
                between_y = mouseY > 400 and mouseY < 460
                if mousePressed and between_x and between_y:
                    restart()
            else:    
                image(imgGameOver,0,0)
                textAlign(CENTER)
                textSize(42)
                fill(156, 222, 255)
                text(score, 240, 400)
                text(high_score, 460, 400)
                
            #text('you lost', 110, 150)
            #text('your score', 75, 275)
            #text(score, 190, 400)
    
