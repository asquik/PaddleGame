import random
class Brick:
    def __init__(self, pos_x, pos_y, w, h, colour):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.active = True
        self.BrickColour = random.randint(50, 255)
        self.colour = colour
        if self.colour == "b":
            self.points = 100
        elif self.colour == 'r':
            self.points = 200
        else:
            self.active = False
        
    def draw(self):            
        if self.active == True:
            if self.colour == 'b':                
                fill(0, 0, 255)
            else:
                fill(255, 0, 0)    
            rect(self.pos_x, self.pos_y, self.w, self.h)
        #else:
            #fill(0,0,0,0)
            #rect(self.pos_x, self.pos_y, self.w, self.h)
        
    def erase(self):
        self.active = False
        #fill(0, 0, 0, 255)
        #rect(self.pos_x, self.pos_y, self.w, self.h)
        
    '''def hit_test(self, x, y):
        x_state = x > self.pos_x and x < self.pos_x + self.w
        y_state = y > self.pos_y and y < self.pos_y + self.h
        hit_test_state = x_state and y_state
        return hit_test_state and self.active
    '''
    
    def bottom_hit_test(self, x, y):
        self.center_x = self.pos_x + self.w/2
        self.center_y = self.pos_y + self.h/2
        if sqrt((x - self.center_x)**2 + (y - self.center_y)**2) < self.w/2:
            return True
        else:
            return False
    
    
    
    def hit_test(self, x, y):
        # Returns true if the coordinate x, y is within the brick.
        return (x > self.pos_x and x < (self.pos_x + self.w) and
                y > self.pos_y and y < (self.pos_y + self.h))  
                    
    
