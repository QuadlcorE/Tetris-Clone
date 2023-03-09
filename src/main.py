################################################
#                                              #
#                TETRIS-CLONE                  #
#                                              #
################################################

import pygame 

# Game Values 
WIDTH ,HEIGHT= 250, 310
BLOCK_HEIGHT = 10

PLAY_WIDTH = BLOCK_HEIGHT *10
PLAY_HEIGHT = BLOCK_HEIGHT*20

LEFT_OFFSET, RIGHT_OFFSET = 50, 50

PLAY_AREA = (LEFT_OFFSET, 0, LEFT_OFFSET, PLAY_HEIGHT, PLAY_WIDTH+LEFT_OFFSET, 0)

FPS = 25

C_WHITE = pygame.Color("white")
C_BLACK = pygame.Color("black")

DROPPED = pygame.USEREVENT + 1


buffer = [[0, 0, 0],
          [0, 0, 0], 
          [0, 0, 0],
          [0, 0, 0] 
           ]

Box_shape = [[0, 0, 0],
             [0, 0, 0],
             [0, 1, 0],
             [1, 1, 1],
             ]

grid_start = (5, 0)

grid = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 6
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 11
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 12
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 13
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 14
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 15
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 16
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 17
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 18
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 19
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 20
        ]

def clear_buffer():
    for _ in range(len(buffer)):
        for square in range(len(buffer[_])):
            buffer[_][square] = 0

def set_buffer_left(x,y):
    for _ in range(len(buffer)):
        buffer[_][0]=grid[y+_][x-1]
    print(buffer)

def buffer_grid_update(x,y):
    for _ in range(len(buffer)):
        for s in range(len(buffer[_])):
            if (s == 0 or s == 2) and not (buffer[_][s] == 0):
                grid[y+_][x+s] = buffer[_][s]
    clear_buffer()

#------------------PLAYER FUNCTIONS---------------------------
class player:
    def __init__(self):
        self.x = grid_start[0]
        self.y = grid_start[1]
        self.active = True
        self.shape = Box_shape
        self.counter = 0
        self.colided = False
    
    def player_update(self):
        if self.active == True:
            i, j = 0, 0
            for _ in range(len(self.shape)):
                for square in range(len(self.shape[_])):
                    grid[self.y+i][self.x+j] = self.shape[_][square]        # Reading from the shape to the grid
                    j+=1
                j=0
                i+=1

    def player_pos_check_bottom(self):
        i, j = 0, 0
        for _ in range(len(self.shape)):
            for square in range(len(self.shape[_])):
                if self.shape[i][j] == 1:
                    if i+1 < 4:
                        if self.shape[i+1][j] == 0:
                            if grid[self.y+i+1][self.x+j] == 1:
                                return False
                    else:
                        if grid[self.y+i+1][self.x+j] == 1:
                                return False
                j+=1
            j=0
            i+=1
        return True

    def player_pos_check_left(self):
        i, j = 0, 0
        for _ in range(len(self.shape)):
            for square in range(len(self.shape[_])):
                if self.shape[i][j] == 1:
                    if j-1 >= 0:
                        if self.shape[i][j-1] == 0:
                            if grid[self.y+i][self.x+j-1] == 1:
                                return False
                    else:
                        if grid[self.y+i][self.x+j-1] == 1:
                                return False
                j+=1
            j=0
            i+=1
        return True

    def move_left(self):
        if self.active == True:
            if self.x > 0 and self.player_pos_check_left() == True:
                set_buffer_left(self.x, self.y)
                i, j = 0, 0
                for _ in range(len(self.shape)):
                    for square in range(len(self.shape[_])):
                        if grid[self.y+i][self.x+j] == 1 and self.x+j < 10:
                            grid[self.y+i][self.x+j] = 0
                        j+=1
                    j=0
                    i+=1
                self.x -=1
    
    def player_pos_check_left(self):
        i, j = 0, 0
        for _ in range(len(self.shape)):
            for square in range(len(self.shape[_])):
                if self.shape[i][j] == 1:
                    if j-1 >= 0:
                        if self.shape[i][j-1] == 0:
                            if grid[self.y+i][self.x+j-1] == 1:
                                return False
                    else:
                        if grid[self.y+i][self.x+j-1] == 1:
                                return False
                j+=1
            j=0
            i+=1
        return True
    
    def move_right(self): 
        if self.active == True:           
            if self.x+2 < 9:
                i, j = 0, 0
                for _ in range(len(self.shape)):
                    for square in range(len(self.shape[_])):
                        if grid[self.y+i][self.x+j] == 1 and self.x >= 0:
                            grid[self.y+i][self.x+j-1] = 0
                        j+=1
                    j=0
                    i+=1
                self.x +=1
    
    def move_down(self):
        if self.active == True:
            if self.y+4 < 20 and self.player_pos_check_bottom() == True:
                self.y += 1  
            else:
                self.active = False
                pygame.event.post(pygame.event.Event(DROPPED))
                
    def player_rotate():
        ...
    
    def player_gravity(self):
        self.counter += 1
        if self.active == True and self.counter == FPS:
            if self.y+4 < 20 and self.player_pos_check_bottom() == True:
                if not self.colided:
                    self.y += 1
                    self.counter = 0
                else:
                    self.active = False
            else:
                self.active = False
                pygame.event.post(pygame.event.Event(DROPPED))
        
        
            
#---------------------DRAW FUNCTIONS-----------------------------

def draw_grid(screen):
    i, j = 0, 0
    y_coordinate = PLAY_AREA[1]
    x_coordinate = PLAY_AREA[0]
    
    for _ in range(len(grid)):
        for square in range(len(grid[_])):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, C_WHITE, pygame.Rect( (x_coordinate, y_coordinate), (BLOCK_HEIGHT, BLOCK_HEIGHT) ))
            x_coordinate += BLOCK_HEIGHT
            j+=1
        j=0
        x_coordinate = PLAY_AREA[0]
        y_coordinate += BLOCK_HEIGHT
        i+=1

def draw_play_area(screen):
    screen.fill(C_BLACK)
    
    pygame.draw.rect(screen, C_WHITE, pygame.Rect( (PLAY_AREA[0]-BLOCK_HEIGHT, PLAY_AREA[1]), (PLAY_WIDTH+BLOCK_HEIGHT, BLOCK_HEIGHT) ))
    pygame.draw.rect(screen, C_WHITE, pygame.Rect( (PLAY_AREA[0]-BLOCK_HEIGHT, PLAY_AREA[1]), (BLOCK_HEIGHT, PLAY_HEIGHT+BLOCK_HEIGHT)))
    pygame.draw.rect(screen, C_WHITE, pygame.Rect( (PLAY_AREA[2], PLAY_AREA[3]), (PLAY_WIDTH+BLOCK_HEIGHT, BLOCK_HEIGHT)))
    pygame.draw.rect(screen, C_WHITE, pygame.Rect( (PLAY_AREA[4], PLAY_AREA[5]), (BLOCK_HEIGHT, PLAY_HEIGHT+BLOCK_HEIGHT)))

def main():
    # Screen initialization
    pygame.init()

    pygame.display.set_caption("Tetris Clone")

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    
    player1 = player()
    
    # Main game loop
    while True:
        draw_play_area(WIN)    
         
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.move_left()
                if event.key == pygame.K_RIGHT:
                    player1.move_right()
                if event.key == pygame.K_DOWN:
                    player1.move_down()
                if event.key == pygame.K_SPACE:
                    print(buffer)
            if event.type == DROPPED:
                player1 = player()
            
            if event.type == pygame.QUIT:
                exit()
        
        keys_pressed = pygame.key.get_pressed()
        
        
        player1.player_gravity()
        player1.player_update()
        buffer_grid_update(player1.x, player1.y)
 

        
        draw_grid(WIN)
        
        clock.tick(FPS)
        
        pygame.display.update()

if __name__ == "__main__":
    main()