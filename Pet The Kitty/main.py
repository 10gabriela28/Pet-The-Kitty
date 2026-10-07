
# creds for the sounds: https://www.youtube.com/watch?v=YMn9JUfDFEc&t=80s
# https://www.youtube.com/watch?v=p56fpxl7WEA
# https://www.youtube.com/watch?v=GXXvBu-j2Co

# original drawings coming soon :)
# i might even add a song in the bg
# up to the user if they wanna mute it

import random
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Pet The Kitty")

x=450
y=450
cat = pygame.image.load(r"assets\cat2.png").convert_alpha()
cat_large = pygame.transform.scale(cat, (x, y))

cat_pos = (275, 75)
rect = cat_large.get_rect(topleft=cat_pos)

clock = pygame.time.Clock()

sound_list = [r"sounds\cropped\meow1.mp3",
              r"sounds\cropped\meow2.mp3",
              r"sounds\cropped\meow3.mp3",
              r"sounds\cropped\meow4.mp3",
              r"sounds\cropped\purr1.mp3",
              r"sounds\cropped\purr2.mp3"]

sounds = [pygame.mixer.Sound(ind) for ind in sound_list]

running = True

while running:

    cursor = pygame.mouse.get_pos()
    if rect.collidepoint(cursor):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                random.choice(sounds).play()

    screen.fill((143, 0, 143))
    screen.blit(cat_large, cat_pos)
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

pygame.quit()