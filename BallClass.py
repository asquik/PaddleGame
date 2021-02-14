class Ball:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = 0    #ball direction x
        self.dy = 0    #ball direction y
        self.sz = 10    #ball size
        self.padpos = 0  
        self.lives = 3
        self.game_over = False
        self.speed = 50
        
    def draw(self, pad_speed):
        self.pos_x = self.pos_x + self.dx   #ball position x + ball direction x
        self.pos_y = self.pos_y + self.dy   #ball position y + ball direction y
        if self.pos_x > width - self.sz/2:  #if the ball x position becomes greater than the width minus half the thickness of the ball
            self.dx *= -1                   #Reverse the x direction (Bouncing off right side)
        if self.pos_x < self.sz/2:          #if the ball x position becomes less than half the width of the ball
            self.dx *= -1                   #Reverse the x direction (Bouncing off left side)
        if self.pos_y < 30 + self.sz/2:     #if the ball y position becomes less than 30 plus half the size of the ball
            self.dy *= -1                   #reverse ball y direction (bouncing off the top)
        if self.pos_y > height-80 - self.sz/2: #if ball y position becomes greater than the height minus 50 minus half the ball size
            if self.paddle_hit_detection():     #if ball hits the paddle
                if pad_speed * self.dx > 0 and abs(self.dx) < 12:
                    self.dx *= 1.4
                    self.dy *=0.9
                elif pad_speed * self.dx < 0 and abs(self.dx) > 2:
                    self.dx /= 1.4
                else:
                    self.dx = self.dx
                root = sqrt((self.dx ** 2 + self.dy **2)/self.speed)
                self.dx /= root
                self.dy /= root               
                self.dy *= -1               # x direction of ball stays the same
        if self.pos_y > height+100 - self.sz/2: #if ball y position goes below the height plus 100 minus half the ball size
            self.new_life()                 #instance new ball from the "lives"
        fill(50,255,255)                     #Ball fill colour is green
        circle(self.pos_x, self.pos_y, self.sz) #makes a circle to represent the ball
        for i in range(self.lives):          #for the number of lives, draws balls at the top of the screen
            stroke(50,200,255)
            circle(10+i * 20, 15, self.sz)
            
    def paddle_hit_detection(self):
        if self.pos_x > self.padpos - 46 and self.pos_x < self.padpos + 41 and self.pos_y < height-80 - self.sz/2 + 2 *self.dy: #if ball position x is greater than the paddle poition minus 20, and is less than the paddle position plus 20 and the ball y position is greater than the height les 49(the height where the paddle is)
            
            on_the_paddle = True    #then the ball is on the paddle
            
        else: 
            on_the_paddle = False    #then the ball is no on the paddle
        return on_the_paddle
    def new_life(self):                    
        if self.lives > 0:
            self.lives -= 1
            self.dx = 0
            self.dy = 0
            self.pos_x = self.padpos
            self.pos_y = 515
        else:
            self.game_over = True
            self.frame_count_lose = frameCount
           
   
                 
    def hit_test(self, x, y):
        # Returns true if the coordinate x, y is within the ball.
        return (self.pos_x - x) ** 2 + (self.pos_y - y) ** 2 < self.sz ** 2
        
