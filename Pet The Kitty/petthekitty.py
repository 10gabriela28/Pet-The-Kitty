
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


bg = pygame.image.load(r"assets\ptk background.png")
bg_large = pygame.transform.scale(bg, (1000, 600))

x=605
y=806.5
cat = pygame.image.load(r"assets\cat_idle.png").convert_alpha()
cat_large = pygame.transform.scale(cat, (x, y))


cat_purr = pygame.image.load(r"assets\cat_purr.png").convert_alpha()
cat_purr_large = pygame.transform.scale(cat_purr, (x, y))

cat_meow1 = pygame.image.load(r"assets\cat_meow1.png").convert_alpha()
cat_meow1_large = pygame.transform.scale(cat_meow1,(x, y))

cat_meow2 = pygame.image.load(r"assets\cat_meow2.png").convert_alpha()
cat_meow2_large = pygame.transform.scale(cat_meow2,(x, y))

current_cat_image = cat_large

meow = [cat_meow1_large, cat_meow2_large]


cat_pos = (155, -100)
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
                reaction = random.choice(sound_list)
                sound_index = sound_list.index(reaction)
                if reaction in [r"sounds\cropped\purr1.mp3", r"sounds\cropped\purr2.mp3"]:
                    current_cat_image = cat_purr_large
                elif reaction in [r"sounds\cropped\meow1.mp3", r"sounds\cropped\meow2.mp3", r"sounds\cropped\meow3.mp3", r"sounds\cropped\meow4.mp3"]:
                    current_cat_image = random.choice(meow)
                sounds[sound_index].play()

    if not pygame.mixer.get_busy():
        current_cat_image = cat_large

    screen.blit(bg_large,(0,0))
    screen.blit(current_cat_image, cat_pos)
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

pygame.quit()