################################################
#                                              #
#                TETRIS-CLONE                  #
#                                              #
################################################

import pygame, os, random

pygame.font.init()

#------------------GAME VALUES----------------------------------- 
WIDTH ,HEIGHT= 250, 310
BLOCK_HEIGHT = 10

FRAMES_BETWEEN_SCREEN_CLEARING = 2

X_SQUARES = 10
Y_SQUARES = 20

PLAY_WIDTH = BLOCK_HEIGHT *X_SQUARES
PLAY_HEIGHT = BLOCK_HEIGHT*Y_SQUARES

LEFT_OFFSET, RIGHT_OFFSET, TOP_OFFSET, BOTTOM_OFFSET = 50, 50, 30, 50
CENTRAL_POS = WIDTH/2

PLAY_AREA = (LEFT_OFFSET, TOP_OFFSET, 
             LEFT_OFFSET, PLAY_HEIGHT+TOP_OFFSET, 
             PLAY_WIDTH+LEFT_OFFSET, TOP_OFFSET)

FPS = 25

POINTS = 5

C_WHITE = pygame.Color("white")
C_BLACK = pygame.Color("black")

DROPPED = pygame.USEREVENT + 1

FONT = pygame.font.Font(os.path.join("ARCADECLASSIC.TTF"), 16)
FONT_2 = pygame.font.Font(os.path.join("ARCADECLASSIC.TTF"), 32)
SCORE_X, SCORE_Y = WIDTH-RIGHT_OFFSET-10, TOP_OFFSET+20

S_S = [[0, 1, 1],
       [1, 1, 0],
       [0, 0, 0]
       ]

S_Z = [[1, 1, 0],
       [0, 1, 1],
       [0, 0, 0]
       ]

S_L = [[0, 1, 0],
       [0, 1, 0],
       [0, 1, 1]
       ]

S_J = [[0, 1, 0],
       [0, 1, 0],
       [1, 1, 0]
       ]

S_I = [[0, 1, 0],
       [0, 1, 0],
       [0, 1, 0],
       ]

S_O = [[1, 1, 0],
       [1, 1, 0],
       [0, 0, 0]
       ]

S_T = [[1, 1, 1],
       [0, 1, 0],
       [0, 0, 0]
       ]

#-----------------GRID FUNCTIONS---------------------------------

current_shape = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0],
                ]

grid_start = (5, 0)

grid = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 1
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 2
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 3
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 4
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 5
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 6
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 7
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 8
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 9
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 10
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 11
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 12
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 13
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 14
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 15
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 16
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 17
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 18
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 19
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 20
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],   # 21
        ]

player_grid =  [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 1
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 2
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 3
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 4
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 5
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 6
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 7
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 8
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 9
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 10
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 11
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 12
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 13
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 14
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 15
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 16
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 17
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 18
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 19
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # 20
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],   # 21
                ]

def grid_to_player_grid():
    for _ in range(len(player_grid)):
        for s in range(len(player_grid[_])):
            if player_grid[_][s] == 1:
                grid[_][s] = 1

def drop_grid(cleared):
    if cleared == True:
        for _ in range(len(grid)-1):
            for s in range(len(grid[_])):
                if grid[-(_+1)][s] == 0 and grid[-(_+2)][s] == 1 and not (s==0 or s==11):
                    grid[-(_+1)][s] = grid[-(_+2)][s]
                    grid[-(_+2)][s] = 0
        cleared = False
    ...

def clear_complete_grids():
    clearable = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for l in range(len(grid)):
        counter = 0
        for s in range(len(grid[l])):
            if grid[l][s] == clearable[s]:
                counter += 1
        if counter == 12 and not (l == 20):
            for s in range(len(grid[l])):
                if not (l == 20):
                    grid[l][s] = 0
            grid[l][0] = 1
            grid[l][11] = 1
            increase_score(multiplier)
            return True
    return False
    ...                


#------------------SHAPE FUNCTIONS----------------------------
shapes = [S_Z, S_S, S_L, S_J, S_I, S_O, S_T]

def get_random_shape():
    return shapes[random.randint(0, 6)]
    ...

def change_current_shape():
    
    ...

#------------------PLAYER FUNCTIONS---------------------------

class player:
    def __init__(self):
        self.x = grid_start[0]
        self.y = grid_start[1]
        self.active = True
        self.shape = get_random_shape()
        self.counter = 0
        self.colided = False
        
    
    def player_update(self):
        if self.active:
            for _ in range(len(self.shape)):
                for s in range(len(self.shape[_])):
                    if self.shape[_][s] == 1:
                        player_grid[self.y+_][self.x+s] = 1
        ... 

    def player_pos_check_bottom(self):
        for _ in range(len(self.shape)):
            for s in range(len(self.shape[_])):
                if self.shape[_][s] == 1:
                    if grid[self.y+_+1][self.x+s] == 1:
                        return False
        return True
        ...

    def player_pos_check_left(self):
        for _ in range(len(self.shape)):
            for s in range(len(self.shape[_])):
                if self.shape[_][s] == 1:
                    if grid[self.y+_][self.x+s-1] == 1:
                        return False
        return True
        ...

    def move_left(self):
        if self.active == True:
            if self.x > 0 and self.player_pos_check_left() == True:
                self.x -= 1
        ...

    def player_pos_check_right(self):
        for _ in range(len(self.shape)):
            for s in range(len(self.shape[_])):
                if self.shape[_][s] == 1:
                    if grid[self.y+_][self.x+s+1] == 1:
                        return False
        return True
        ...
       
    def move_right(self):
        if self.active == True:
            if self.x < 10 and self.player_pos_check_right() == True:
                self.x += 1 
        ...
    
    def move_down(self):
        if self.active == True:
            if self.y+2 < Y_SQUARES and self.player_pos_check_bottom() == True:
                self.y += 1
            else:
                self.active = False
                pygame.event.post(pygame.event.Event(DROPPED))
        ...
            
    def check_collision(self, buffer):
        for _ in range(len(buffer)):
            for s in range(len(buffer[_])):
                if buffer[_][s] == 1 and grid[self.y+_][self.x+s] == 1:
                    return True
        return False
        ...

    def game_over(self, screen):
        if self.player_pos_check_bottom() == False:
            draw_game_over(screen)
            return True
        return False
        
    def player_rotate(self):
        buffer = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]
                  ]
        
        for _ in range(len(self.shape)):
            for s in range(len(self.shape[_])):
                buffer[s][2-_] = self.shape[_][s]

        if self.check_collision(buffer) == False:             
            for _ in range(len(self.shape)):
                for s in range(len(self.shape[_])):
                    self.shape[_][s] = buffer[_][s]
        ...
    
    def last_pos(self):
        for _ in range(len(self.shape)):
            for s in range(len(self.shape[_])):
                if self.shape[_][s] == 1:
                    player_grid[self.y+_][self.x+s] = 1
    
    def player_gravity(self, speed):
        self.counter += 1
        if self.active == True and self.counter >= speed:
            if self.y+2 < Y_SQUARES and self.player_pos_check_bottom() == True:
                if not self.colided:
                    self.y += 1
                    self.counter = 0
                else:
                    self.active = False
            else:
                self.active = False
                pygame.event.post(pygame.event.Event(DROPPED))
        ...


       
#--------------------SCORE FUNCTIONS----------------------------

multiplier = 1
score = 0

def increase_score(multiplier=1):
    global score 
    score += multiplier*POINTS


           
#---------------------DRAW FUNCTIONS-----------------------------

def draw_grid(screen):
    y_coordinate = PLAY_AREA[1]
    x_coordinate = PLAY_AREA[0]
    
    for _ in range(len(grid)):
        for s in range(len(grid[_])):
            if grid[_][s] == 1:
                pygame.draw.rect(screen, C_WHITE, pygame.Rect( (x_coordinate, y_coordinate), (BLOCK_HEIGHT, BLOCK_HEIGHT) ))
            x_coordinate += BLOCK_HEIGHT
        x_coordinate = PLAY_AREA[0]
        y_coordinate += BLOCK_HEIGHT

def draw_player_grid(screen):
    y_coordinate = PLAY_AREA[1]
    x_coordinate = PLAY_AREA[0]
    
    for _ in range(len(player_grid)):
        for s in range(len(player_grid[_])):
            if player_grid[_][s] == 1:
                pygame.draw.rect(screen, C_WHITE, pygame.Rect( (x_coordinate, y_coordinate), (BLOCK_HEIGHT, BLOCK_HEIGHT) ))
                player_grid[_][s] = 0
            x_coordinate += BLOCK_HEIGHT
        x_coordinate = PLAY_AREA[0]
        y_coordinate += BLOCK_HEIGHT
    
def draw_play_area(screen):
    screen.fill(C_BLACK)
    
    pygame.draw.rect(screen, C_WHITE, pygame.Rect( (PLAY_AREA[0], PLAY_AREA[1]), (PLAY_WIDTH+BLOCK_HEIGHT, BLOCK_HEIGHT) ))
    #pygame.draw.rect(screen, C_WHITE, pygame.Rect( (PLAY_AREA[0]-BLOCK_HEIGHT, PLAY_AREA[1]), (BLOCK_HEIGHT, PLAY_HEIGHT+BLOCK_HEIGHT)))
    #pygame.draw.rect(screen, C_WHITE, pygame.Rect( (PLAY_AREA[2], PLAY_AREA[3]), (PLAY_WIDTH+BLOCK_HEIGHT, BLOCK_HEIGHT)))
    #pygame.draw.rect(screen, C_WHITE, pygame.Rect( (PLAY_AREA[4], PLAY_AREA[5]), (BLOCK_HEIGHT, PLAY_HEIGHT+BLOCK_HEIGHT)))

def draw_score(screen):
    screen.blit(FONT.render("SCORE", 0, C_WHITE), (SCORE_X, SCORE_Y))
    screen.blit(FONT.render(str(score), 0, C_WHITE), (SCORE_X, SCORE_Y+20))
    
def draw_game_over(screen):
    screen.blit(FONT_2.render("Game Over", 0, C_WHITE), (CENTRAL_POS-80, HEIGHT-BOTTOM_OFFSET))

#---------------------SPEED FUNCTIONS--------------------------

timer = 1

def get_speed():
    return FPS/timer 

def increase_speed():
    global timer
    timer += 0.01

            

#--------------------MAIN PROGRAM--------------------------------
def main():
    # Screen initialization
    pygame.init()

    pygame.display.set_caption("Tetris Clone")

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    
    player1 = player()
    
    change_current_shape()
    
    GameOver = False
    
    # Main game loop
    while GameOver == False:
        draw_play_area(WIN)    
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.move_left()
                if event.key == pygame.K_RIGHT:
                    player1.move_right()
                if event.key == pygame.K_UP:
                    player1.player_rotate()
                if event.key == pygame.K_DOWN:
                    player1.move_down()
                if event.key == pygame.K_SPACE:
                    print(grid)
                    ...
            if event.type == DROPPED:
                increase_speed()
                multiplier = 1
                player1.last_pos()
                grid_to_player_grid()
                player1 = player()
                if player1.game_over(WIN) == True:
                    pygame.display.update()
                    GameOver = True
            
            if event.type == pygame.QUIT:
                exit()
                
        player1.player_gravity(get_speed())
        player1.player_update()
        
            
        draw_grid(WIN)
        draw_player_grid(WIN)
        drop_grid(clear_complete_grids())
        draw_score(WIN)
        clock.tick(FPS)
        
        pygame.display.update()


    while True:
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

if __name__ == "__main__":
    main()