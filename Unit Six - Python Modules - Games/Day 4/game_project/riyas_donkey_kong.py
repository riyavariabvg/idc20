# This game is a modified version of donkey kong. The goal of the game is to get the highest score possible. 
# The user scores points by controlling their mario character (SPACE to jump, RIGHT to go right, LEFT to go left, UP to climb lader, DOWN to descend ladder)
# to reach the house on the top platform. However, there are moving barrel obstacles in the way.
# The user must jump over these barrels and climb ladders to reach the top platform. There is also a floating fireball that the player must avoid. Once they reach the house on the top platform, the mario resets to its original position
# and the user scores a point. As the user's points increase, the speed of the moving barrels increases as well as the speed of the fireball, which makes the game harder. 


import random
import pygame
import time
from pygame import mixer

# initialize pygame
pygame.init()

# set up the screen dimensions and frames per second
WIDTH, HEIGHT = 1000, 800
fps = 60

# lists to store platforms and ladders
platforms = []
climbers = []

# set up the game window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# define section dimensions for easier positioning (32*32)
section_width = WIDTH // 32
section_height = HEIGHT // 32

# define slope for the platforms
slope = section_height // 8

# define y positions for each row of platforms
row1_y = HEIGHT - 3 * section_height
row2_y = HEIGHT - 8 * section_height
row3_y = HEIGHT - 13 * section_height
row4_y = HEIGHT - 18 * section_height

# load sprite images and scale them to appropriate sizes
barrel = pygame.transform.scale(pygame.image.load('barrel.png'), (section_width * 1, section_height * 1))
mario = pygame.transform.scale(pygame.image.load('mario.png'), (1.5*section_width, 2.5 * section_height))
mario_climbing = pygame.transform.scale(pygame.image.load('climbing1.png'),(1.5 * section_width, 2.5 * section_height))
house = pygame.transform.scale(pygame.image.load('house.png'), (section_width * 3, section_height * 4))
fireball = pygame.transform.scale(pygame.image.load('fireball.png'), (1.5 * section_width, 2 * section_height))


# define the positions and lengths of bridges
bridges_list = [(0, row1_y, 16), (16, row1_y - slope, 3),
                       (19, row1_y - 2 * slope, 3), (22, row1_y - 3 * slope, 3),
                       (25, row1_y - 4 * slope, 3), (28, row1_y - 5 * slope, 4),
                       (25, row2_y, 7), (22, row2_y - slope, 3),
                       (19, row2_y - 2 * slope, 3), (16, row2_y - 3 * slope, 3),
                       (13, row2_y - 4 * slope, 3), (10, row2_y - 5 * slope, 3),
                       (7, row2_y - 6 * slope, 3), (4, row2_y - 7 * slope, 3),
                       (0, row2_y - 8 * slope, 4), 
                       (0, row3_y, 7), (7, row3_y - slope, 3), (10, row3_y - 2 * slope, 3),
                       (13, row3_y - 3 * slope, 3), (16, row3_y - 4 * slope, 3),
                       (19, row3_y - 5 * slope, 3), (22, row3_y - 6 * slope, 3),
                       (25, row3_y - 7 * slope, 3), (28, row3_y - 8 * slope, 4),
                       (25, row4_y, 7), (22, row4_y - slope, 3),
                       (19, row4_y - 2 * slope, 3), (16, row4_y - 3 * slope, 3),
                       (13, row4_y - 4 * slope, 3), (10, row4_y - 5 * slope, 3),
                       (7, row4_y - 6 * slope, 3), (4, row4_y - 7 * slope, 3),
                       (0, row4_y - 8 * slope, 4), 
                       
                       (10, 200, 13)]

# define positions and lengths of ladders
ladders_list = [(25 * section_width, row2_y + 8 * slope, 6),
                (6 * section_width, row3_y + 9 * slope, 5),
                (14 * section_width, row3_y + 7 * slope, 6),
                (16 * section_width, row4_y + 6 * slope, 6),
                (25 * section_width, row4_y + 9 * slope, 5),
                (20 * section_width, 9 * section_height, 8)]

# define the mario class
class Mario(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.x = x_pos
        self.y = y_pos
        self.current_score = 0
        self.high_score = 0
        self.direction = "right"
        self.png = mario
        self.rect = self.png.get_rect()
        self.rect.move_ip(self.x, self.y)
        self.landed = False
        self.bottom = pygame.rect.Rect(self.rect.left, self.rect.bottom, self.rect.width, 20)
        self.climbing = False
        self.y_change = 2
        self.x_change = 0
        self.jumping_up = False
        self.reset = False
    
    # function to reset mario's position
    def reset_position(self):
        self.rect.move_ip(self.x - self.rect.x, self.y - self.rect.y)
        self.direction = "right"
        
    # function to update mario's position and behaviour 
    def update(self):
        if self.reset:
            self.reset = False
            self.reset_position()
            return
        self.landed = False
        for i in range(len(platforms)):
            if self.bottom.colliderect(platforms[i]):
                self.landed = True
                if self.rect.bottom <= 210 and self.rect.left <= 540:
                    self.current_score +=1
                    scored = mixer.Sound("beep.wav")
                    scored.play()
                    time.sleep(1)
                    if self.current_score > self.high_score:
                        self.high_score = self.current_score
                    for b in barrel_list:
                        b.reset_position()
                    fireball.reset_position()
                    self.reset = True
                if not self.climbing and not self.jumping_up:
                    self.y_change = 0
                    self.rect.centery = platforms[i].top - self.rect.height/2 +1 
        if not self.climbing:
            if self.jumping_up:
                self.y_change -= 0.25
                if self.y_change == -4:
                    self.jumping_up = False
                    self.landed = False
            else:               
                if not self.landed:
                    self.y_change += 0.25

        # if mario goes off the screen
        if self.rect.right > 990: 
            self.rect.right = 990
        elif self.rect.left < 10:
            self.rect.left = 10
                
        self.rect.move_ip(self.x_change, self.y_change) 
        self.bottom = pygame.rect.Rect(self.rect.left, self.rect.bottom, self.rect.width,20)
    
    # function to draw the mario sprite 
    def draw(self):
        if self.climbing:
            self.png = mario_climbing
        elif self.direction == "right":
            self.png = mario
        elif self.direction == "left":
            self.png = pygame.transform.flip(mario, True, False)
        
        self.rect = screen.blit(self.png, self.rect.topleft)
        self.bottom = pygame.rect.Rect(self.rect.left, self.rect.bottom, self.rect.width, 20)

# define barrel class
class Barrel(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, dir="right"):
        self.x = x_pos
        self.y = y_pos
        self.dir = dir
        self.x_change = 0
        self.y_change = 0.25
        self.landed = False
        self.png = barrel
        self.rect = self.png.get_rect()
        self.rect.move_ip(self.x, self.y)
        self.init_x = x_pos
        self.init_y = y_pos
        self.change_speed_rate = 2
    
    # function to reset the barrel position 
    def reset_position(self):
        self.rect.move_ip(self.init_x - self.rect.x, self.init_y - self.rect.y)
    
    # function to update barrel position and behaviour 
    def update(self):
        if self.rect.colliderect(player.rect):
            dead = mixer.Sound("explosion.wav")
            dead.play()
            time.sleep(1)
            player.reset = True
            player.current_score = 0
            for b in barrel_list:
                b.reset_position()
            fireball.reset_position()
        self.landed = False
        for i in range(len(platforms)):
            if self.rect.colliderect(platforms[i]):
                self.landed = True
                if self.dir == "right":
                    self.x_change = player.current_score//self.change_speed_rate + 3
                else:
                    self.x_change = -1*(player.current_score//self.change_speed_rate) - 3
                self.y_change = 0
        if not self.landed:
            self.y_change += 0.25
        self.rect.move_ip(self.x_change, self.y_change)
        if self.dir == "right" and self.rect.right > 1000:
            self.rect.move_ip(-1000, -40)
        elif self.dir == "left" and self.rect.left < 0:
            self.rect.move_ip(1000, -40)
    
    # function to draw the barrel sprite 
    def draw(self):
        self.rect = screen.blit(self.png, self.rect.topleft)

class Fireball(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.x_change = random.randint(2, 5)
        self.y_change = 1
        self.x_speed = 1
        self.y_speed = 1
        self.png = fireball
        self.rect = self.png.get_rect()
        self.rect.move_ip(self.x, self.y)
        
     
    def reset_position(self):
        self.rect.move_ip(random.randint(200, 700) - self.rect.x, random.randint(20, 500) - self.rect.y)
    
    def update(self):
        if self.rect.colliderect(player.rect):
            dead = mixer.Sound("explosion.wav")
            dead.play()
            time.sleep(1)
            player.reset = True
            player.current_score = 0
            for b in barrel_list:
                b.reset_position()
            self.reset_position()
        else: 
            self.x_speed = player.current_score/4 +1 # this will cause the speed of the fireball to increase as the score increases. 
            self.y_speed = player.current_score/4 + 1
            # cases for going off screen
            if self.rect.bottom > 790:
                self.y_change = -1*(random.randint(1,2))
            if self.rect.left < 10:
                self.x_change = random.randint(1,2)
            if self.rect.right > 990:
                self.x_change = -1*(random.randint(1,2))
            if self.rect.top < 10:
                self.y_change = random.randint(1,2)

            self.rect.move_ip(self.x_change *self.x_speed, self.y_change*self.y_speed)
            
    
    def draw(self):
        self.rect = screen.blit(self.png, self.rect.topleft)
        
        
        



# function to draw platforms 
def draw_platform(x_pos, y_pos, length):
    x_pos *= section_width
    platform = pygame.rect.Rect((x_pos, y_pos), (length * section_width, section_height))
    pygame.draw.rect(screen, 'white', platform)
    return platform 

# function to draw ladders
def draw_ladder(x_pos, y_pos, length):
    line_width = 3
    lad_color = 'blue'
    lad_height = 0.6
    for i in range(length):
            top_coord = y_pos + lad_height * section_height * i
            bot_coord = top_coord + lad_height * section_height
            mid_coord = (lad_height / 2) * section_height + top_coord
            left_coord = x_pos
            right_coord = left_coord + section_width
            pygame.draw.line(screen, lad_color, (left_coord, top_coord), (left_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (right_coord, top_coord), (right_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (left_coord, mid_coord), (right_coord, mid_coord), line_width)
    ladder_rect = get_rect_value_for_ladder(x_pos, y_pos, length)
    return ladder_rect

# function to get rectangular value for ladder
def get_rect_value_for_ladder(x_pos, y_pos, length):
    lad_height = 0.6
    rect_value = pygame.rect.Rect((x_pos, y_pos - section_height), (section_width, (lad_height * length * section_height +section_height)))
    return rect_value

# function to draw the game screen
def draw_screen():
    platforms.clear()
    climbers.clear()
    # draw bridges on the screen
    for bridge in bridges_list:
        platforms.append(draw_platform(*bridge))
    
    # draw ladders on the screen
    for ladder in ladders_list:
        climbers.append(draw_ladder(*ladder))
    
    return platforms, climbers

# Function to check if player can climb
def check_climb():
    able_to_climb = False
    able_to_climb_down = False
    for lad in climbers:
        if lad.colliderect(player.rect) and not able_to_climb:
            able_to_climb = True
        if lad.colliderect(player.bottom):
            able_to_climb_down = True

    if (not able_to_climb and (not able_to_climb_down or player.y_change < 0)) or (player.landed and able_to_climb and player.y_change > 0 and not able_to_climb_down):
        player.climbing = False
    return able_to_climb, able_to_climb_down

# create player instance of the mario class
player = Mario(50,650)

# create barrel instances 
barrel_list = [Barrel(900, 650, "left"), Barrel(50, 500), Barrel(900, 400, "left"), Barrel(50, 200)]

fireball = Fireball(random.randint(200, 700), random.randint(20, 500)) 



# main game loop
def main():
    timer = pygame.time.Clock()
    pygame.display.set_caption("Donkey Kong")
    running = True
    while running:
        screen.fill('black')
        font = pygame.font.Font('freesansbold.ttf', 24)
        score_text = font.render("Score: " + str(player.current_score), True, (255, 255, 255))
        high_score_text = font.render("High Score: " + str(player.high_score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (200, 10))
        climb, down = check_climb()
        draw_screen()
        screen.blit(house, (500, 120))
        player.update()
        player.draw()
        fireball.update()
        fireball.draw()
        


        for barrel in barrel_list:
            barrel.update()
            barrel.draw()
        
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type== pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and not player.climbing:
                    player.x_change = 3
                    player.direction = "right"
                if event.key == pygame.K_LEFT and not player.climbing:
                    player.x_change = -3
                    player.direction = "left"
                if event.key == pygame.K_SPACE and player.landed:
                    player.jumping_up = True
                    jump_sound = mixer.Sound("laser.wav")
                    jump_sound.play()
                if event.key == pygame.K_UP:
                    if climb:
                        player.y_change = -2
                        player.x_change = 0
                        player.climbing = True 
                        ladder_sound = mixer.Sound("climbing_ladder.mp3")
                        ladder_sound.play()
            
                if event.key == pygame.K_DOWN:
                    if down:
                        player.y_change = 2
                        player.x_change = 0
                        player.climbing = True 
                        ladder_sound = mixer.Sound("climbing_ladder.mp3")
                        ladder_sound.play()
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.x_change = 0
                if event.key == pygame.K_LEFT:
                    player.x_change = 0
                if event.key == pygame.K_UP:
                    if climb:
                        player.y_change = 0
                    if player.climbing and player.landed:
                        player.climbing = False
                if event.key == pygame.K_DOWN:
                    if climb:
                        player.y_change = 0
                    if player.climbing and player.landed:
                        player.climbing = False
                    
        pygame.display.flip()
        timer.tick(fps)
    pygame.quit()

# execute the main function 
if __name__ == "__main__":
    main()
