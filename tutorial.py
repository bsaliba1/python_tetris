import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")
background_colour = (255, 255, 255)
win.fill(background_colour)
pygame.display.flip()

x, y = 50, 50
width, height = 40, 60
vel = 5

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))  # rect(surface, color, (x,y,width,height))
    pygame.display.update()

pygame.quit()
