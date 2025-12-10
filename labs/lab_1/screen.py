import pygame
pygame.init()

# *********SETUP**********
windowWidth = 600
windowHeight = 600
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()

# ---------- COLORS (RGBA with alpha) ----------
# (R, G, B, Alpha)
color_vertical = (255, 0, 0, 120)
color_horizontal = (0, 120, 255, 120)

layer = pygame.Surface((windowWidth, windowHeight), pygame.SRCALPHA)

# ---------- DRAW PLAID PATTERN ----------
# вертикальные полосы
for x in range(0, windowWidth, 50):
    width = 10 if x % 100 == 0 else 4
    pygame.draw.rect(layer, color_vertical, (x, 0, width, windowHeight))

# горизонтальные полосы
for y in range(0, windowHeight, 50):
    height = 10 if y % 100 == 0 else 4
    pygame.draw.rect(layer, color_horizontal, (0, y, windowWidth, height))


# *********GAME LOOP**********
running = True
while running:
    # EVENTS
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    # DRAW FRAME
    window.fill((255, 255, 255))
    window.blit(layer, (0, 0))

    # UPDATE SCREEN
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
