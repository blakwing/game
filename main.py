import pygame
import sys
from entities import entity, GameObject, map_generator
pygame.init()

# test commit
clock = pygame.time.Clock()

window_size = (700, 500)

background = 95, 205, 228

screen = pygame.display.set_mode(window_size)
screen.fill(background)
pygame.display.flip()

x_momentum = 0
y_momentum = 0

second_guy = GameObject("assets/art/chico.png", 2)

map_generator("assets/maps/map1.txt", "assets/art/Grass_Tile.png", 2)

camera_value = [96, -100]
flipped = False

while 1:
    camera = [0, 0]
    camera[0] += (second_guy.rectangle.x-camera[0]-((window_size[0]-camera_value[0])/2))/20
    camera[1] += (second_guy.rectangle.y-camera[1]-((window_size[1]-camera_value[1])/2))/20

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("game quit!")
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                second_guy.moving["left"] = True
                camera_value[0] = -80
                flipped = True
            if event.key == pygame.K_RIGHT:
                second_guy.moving["right"] = True
                camera_value[0] = 96
                flipped = False
            if event.key == pygame.K_UP:
                second_guy.moving["up"] = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                second_guy.moving["left"] = False

            if event.key == pygame.K_RIGHT:
                second_guy.moving["right"] = False

            if event.key == pygame.K_UP:
                second_guy.moving["up"] = False

# Y coordinate movement

    if second_guy.collision_kind["bottom"]:
        y_momentum = 0
    else:
        y_momentum += 0.3

    if second_guy.moving["up"] and second_guy.collision_kind["bottom"]:
        y_momentum += -8

    if y_momentum > 7:
        y_momentum = 7
# X coordinate movement
    if second_guy.moving["left"]:
        x_momentum += -3
    if second_guy.moving["right"]:
        x_momentum += 3

    if x_momentum > 0:
        x_momentum -= 0.4
    elif x_momentum < 0:
        x_momentum -= -0.4
    else:
        pass
    if x_momentum > 5:
        x_momentum = 5
    elif x_momentum < -5:
        x_momentum = -5

    second_guy.movement(x_momentum, y_momentum)

    clock.tick(60)
    screen.fill(background)

    for i in entity.entity_list:
        i.rectangle.move_ip(-camera[0], -camera[1])
        i.update_rect.move_ip(-camera[0], -camera[1])
        screen.blit(i.image_entity, i.rectangle)

    pygame.display.update(entity.update_list)
