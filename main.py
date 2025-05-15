import pygame


pygame.init()

import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

size = (640, 480)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("PacMan")

BACKGROND = (0, 0, 0)

CIRCLE_COLOR = (255, 255, 255)

CIRCLE_RADIUS = 20
krug = pygame.image.load("krug.png")

circle_pos = (320,240)

angle = 20

speed = 2

dist = 0
max_distance = 500
max_speed = 3
min_speed = 1
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    dx = mouse_pos[0] - circle_pos[0]
    dy = mouse_pos[1] - circle_pos[1]
    angle = math.degrees(math.atan2(dy, dx))

    dist = distance(circle_pos, mouse_pos)
    speed = max_speed - (dist / max_distance) * (max_speed - min_speed)
    dx = speed * math.cos(math.radians(angle))
    dy = speed * math.sin(math.radians(angle))

    circle_pos = (circle_pos[0] + dx, circle_pos[1] + dy)
    screen.fill(BACKGROND)
    rotated_pacman = pygame.transform.rotate(krug, -angle)
    rotated_pacman_rect = rotated_pacman.get_rect()
    rotated_pacman_rect.center = circle_pos
    screen.blit(rotated_pacman, rotated_pacman_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()