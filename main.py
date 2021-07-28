import pygame
import random

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

clock = pygame.time.Clock()
FPS = 60

# Sounds
eat_music = pygame.mixer.Sound("music/smw_coin.wav")
hit_music = pygame.mixer.Sound("music/smw_hit_while_flying.wav")

class Lion:
    
    def __init__(self,*args,**kwargs):
        #Size
        self.width = 40
        self.height = 30

        #Position
        self.x = (SCREEN_WIDTH / 2) - (self.width / 2)
        self.y = SCREEN_HEIGHT - self.height

        #Move
    def control(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] and self.x <= (SCREEN_WIDTH - self.width - 10):
            self.x += 10
        if pressed[pygame.K_LEFT] and self.x - 10 >= 0:
            self.x -= 10
        if pressed[pygame.K_UP] and self.y - 10 >= 0:
            self.y -= 10
        if pressed[pygame.K_DOWN] and self.y <= (SCREEN_HEIGHT - self.height -10):
            self.y += 10
        
        #Draw
    def draw(self):
        pygame.draw.rect(screen,BLUE,(self.x,self.y,self.width,self.height))

class Food:

    def __init__(self,*args,**kwargs):
        #Color
        self.color = GREEN

        #Size
        self.width = 40
        self.height = 30

        #Positions
        self.food_list = []

        #Directions
        self.dirs = ('r','l','u','d')

    def generate(self):
        for i in range(0,11 + random.randint(0,5)):

            x = random.randint(0,SCREEN_WIDTH - self.width)
            y = random.randint(0,SCREEN_HEIGHT - self.height)

            self.food_list.append([x,y,self.width,self.height])
    
    def move(self):
        for rect in self.food_list:
            direction = random.choice(self.dirs)

            if rect[0] < 0 : direction = 'r'
            if rect[0] > SCREEN_WIDTH : direction = 'l'
            if rect[1] < 0 : direction = 'd'
            if rect[1] > SCREEN_HEIGHT : direction = 'u'

            if direction == 'r': rect[0] += 5
            if direction == 'l': rect[0] -= 5
            if direction == 'u': rect[1] -= 5
            if direction == 'd': rect[1] += 5

    def draw(self):
        for rect in self.food_list:
            pygame.draw.rect(screen,self.color,rect)

class Obstacle:

    def __init__(self,*args,**kwargs):
        #Color
        self.color = RED

        #Size
        self.width = 40
        self.height = 30

        #Positions
        self.obstacle_list = []
    
    def generate(self):
        for i in range(0,11 + random.randint(0,5)):

            x = random.randint(0,SCREEN_WIDTH - self.width)
            y = random.randint(0,SCREEN_HEIGHT - self.height)

            self.obstacle_list.append([x,y,self.width,self.height])

    def move(self):
        for rect in self.obstacle_list:
            rect[1] += 5

    def spawn_condition(self):
        for rect in self.obstacle_list:
            if rect[1] >= SCREEN_HEIGHT:
                return True
        return False
    
    def spawn_rect(self):
        self.obstacle_list.append([random.randint(0,SCREEN_WIDTH - self.width),0,self.width,self.height])

    def draw(self):
        for rect in self.obstacle_list:
            pygame.draw.rect(screen,RED,rect)

#Objects
lion = Lion()
food = Food()
obstacle = Obstacle()



#Outer logics
food.generate()
obstacle.generate()
condition_counter = 0
points_counter = 0
running = True

while running:
    #Creating rect of lion
    lion_rect = pygame.Rect(lion.x,lion.y,lion.width,lion.height)

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Logics
    lion.control()
    obstacle.move()
    food.move()

        #Spawn
    if obstacle.spawn_condition():
        condition_counter += 1
        if condition_counter % 5 == 0:
            obstacle.spawn_rect()

        #Collision detection
    for rect in food.food_list:

        food_rect = pygame.Rect(rect[0],rect[1],rect[2],rect[3])

        if lion_rect.colliderect(food_rect):
            eat_music.play()
            points_counter += 1
            food.food_list.remove(rect)

    for rect in obstacle.obstacle_list:

        obstacle_rect = pygame.Rect(rect[0],rect[1],rect[2],rect[3])

        if lion_rect.colliderect(obstacle_rect):
            hit_music.play()
            points_counter -= 1
            obstacle.obstacle_list.remove(rect)

    #Draw
    screen.fill(WHITE)
    lion.draw()
    food.draw()
    obstacle.draw()

    #Write scores
    font = pygame.font.Font(None,20)
    text = font.render(f"Score: {points_counter}",True,BLACK)
    screen.blit(text,(0,0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()