import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)

road_width = int(width/1.6)
road_mark_w = int(width/80)
right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4
speed = 1

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Game")
# Set background colour
screen.fill((60, 220 ,0))



# load player vehicle
car = pygame.image.load("src/car.png")
#resize image
#car = pygame.transform.scale(car, (250, 250))
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

# load enemy vehicle
car2 = pygame.image.load("src/otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

# Game loop
counter = 0
while running:
    counter += 1

    # Increase difficulty
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up", speed)

    # Animate enemy vehicle
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # Randomly select lane
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    # End game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break

    # Event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            # Exit the app
            running = False
        if event.type == KEYDOWN:
            # Move left
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_width/2), 0])
            # Move right
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_width/2), 0])        

    # Draw graphics
    pygame.draw.rect(screen, (50,50,50), (width/2-road_width/2, 0, road_width, height))
    pygame.draw.rect(screen, (255,240,60), (width/2-road_mark_w/2, 0, road_mark_w, height))
    pygame.draw.rect(screen, (255,255,255), (width/2-road_width/2+road_mark_w*3, 0, road_mark_w, height))
    pygame.draw.rect(screen, (255,255,255), (width/2+road_width/2-road_mark_w*3, 0, road_mark_w, height))

    # Load images
    # place car images on the screen
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)

    # Apply changes
    pygame.display.update()

pygame.quit()
