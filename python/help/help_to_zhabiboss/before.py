
import pygame
import sys
import random

pygame.init()

res = width, height = 1080, 720
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
fps = 60
lives = 5
dead = False
score = 0
globaltimer = 0
counting = False


class Target:
    def __init__(self, position = (width // 2, height // 2)):
        self.position = position
        self.destroyed = False
        self.timer = 0

    def onclick(self):
        pos = pygame.mouse.get_pos()
        if pygame.Rect(self.position[0] - 20, self.position[1] - 20, 40, 40).collidepoint(pos[0], pos[1]):
            self.destroyed = True

    def draw(self):
        if self.destroyed == False: pygame.draw.circle(screen, (255, 255, 255), self.position, 20)

    def update(self):
        if self.destroyed == False: self.timer += 1

target = Target()
font = pygame.font.Font("freesansbold.ttf", 32)

while True:
    if dead == False:
        screen.fill((0, 0, 0))
    else:
        screen.fill((255, 0, 0))

    text = font.render(f"Score: {score}", True, "white")
    screen.blit(text, (0, 0))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            target.onclick()

    if dead == False:
        target.update()
        target.draw()

        if target.destroyed:
            counting = True
            #target = Target(position = (random.randint(0, width), random.randint(0, height)))
        else:
            if target.timer > 70:
                target = Target(position = (random.randint(0, width), random.randint(0, height)))
                lives -= 1
                score -= 5
                if score < 0: score = 0
                if lives == 0: dead = True

        if counting:
            globaltimer += 1
            if globaltimer == 40 and dead == False:
                score += 1
                target = Target(position = (random.randint(0, width), random.randint(0, height)))
                globaltimer = 0
                counting = False

    pygame.display.update()
    clock.tick(fps)