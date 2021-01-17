import pygame
wind_width = 800
wind_height = 550
white = (200, 200, 200)
red = (255, 0, 0)
white1 = (255, 255, 255)
green = (124,252,0)
blue = (0,0,128)
pygame.init()
screen = pygame.display.set_mode([wind_width, wind_height])
clock = pygame.time.Clock()
clock.tick(30)
running = True
done = False
size = 15
NoStart = False
pressed_keys = [False, False]
def draw_grid():
    for x in range(wind_width):
        for y in range(wind_height):
            rect = pygame.Rect(x*size, y*size, size, size)
            pygame.draw.rect(screen, white, rect, 1)
def fill_square(color):
    x = int(pygame.mouse.get_pos()[0] / size) * size
    y = int(pygame.mouse.get_pos()[1] / size) * size
    pygame.draw.rect(screen, color, (x, y, size, size), 0)
draw_grid()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 115:
                fill_square(green)
            if event.key == 101:
                fill_square(blue)
    click = pygame.mouse.get_pressed()
    if click[2] == True:
        fill_square(red)
    pygame.display.flip()
    pygame.display.update()
    pressed_keys[0] = False
pygame.quit()

