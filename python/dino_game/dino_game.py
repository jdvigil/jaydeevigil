#!/usr/bin/python3
import pygame, random, time

# Setup

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((750,500))

pygame.display.set_caption('Dinosaur Game')
clock = pygame.time.Clock()

# Color
white = (255, 255, 255)
black = (0, 0, 0)
brown = (150,150,100)


# Classes
class Steve(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 40])
        self.image.fill(brown)
        self.rect = self.image.get_rect()
        self.points = 0

class SmallTree(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 20])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0

class TallTree(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 30])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0

# Sprite Setup
steve = Steve()
steve.rect.x = 200
steve.rect.y = 300

small_tree = SmallTree()
small_tree.rect.x = 750
small_tree.rect.y = 320
hurdles = pygame.sprite.Group()
hurdles.add(small_tree)

player = pygame.sprite.Group()
player.add(steve)

# Redraw
def redraw():
    end_game = False
    screen.fill(black)
    player.draw(screen)
    hurdles.draw(screen)
    pygame.display.update()

run = True

jump = False
jump_up = 0
jump_down = 0
game_over = False
hurdle_speed = 5

# Game Loop
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(60)

    # Jump
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        jump = True
    if jump_up < 100 and jump == True:
        steve.rect.y -= 10
        jump_up += 10
        redraw()
    elif jump_down < 20 and jump_up == 100:
        steve.rect.y += 25
        jump_down += 5
        redraw()
    if jump_down >= 20:
        jump_up = 0
        jump_down = 0
        steve.rect.y = 300
        jump = False

    small_tree.rect.x -= hurdle_speed
    if small_tree.rect.x == 0:
        small_tree.kill()
        small_tree = SmallTree()
        small_tree.rect.x = 750
        small_tree.rect.y = 320
        hurdles = pygame.sprite.Group()
        hurdles.add(small_tree)

    if small_tree.rect.colliderect(steve):
        game_over = True
        hurdle_speed = 0
        if steve.rect.y < 300:
            jump_up = 0
            jump_down = 0
            steve.rect.y = 300
            redraw()
            time.sleep(1)
        #if key[pygame.K_SPACE]:
        #    print(jump)
        #    jump = False
        #    pygame.time.wait(700)
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            small_tree.kill()
            small_tree = SmallTree()
            small_tree.rect.x = 750
            small_tree.rect.y = 320
            hurdles = pygame.sprite.Group()
            hurdles.add(small_tree)
            hurdle_speed = 5
            game_over = False

    redraw()

pygame.quit()
