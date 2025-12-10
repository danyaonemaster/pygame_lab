import pygame
import random

pygame.init()

# *********SETUP**********
windowWidth = 1150
windowHeight = 400
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("Ransom Note — FULL 4+ Edition")

# ---------- LOAD FONTS ----------
# Custom font (required for 4+)
custom_font = pygame.font.Font("dpcomic.ttf", 60)

# Extra fonts
font1 = pygame.font.SysFont("arial", 45)
font2 = pygame.font.SysFont("comicsansms", 45)
font3 = pygame.font.SysFont("timesnewroman", 45)
font4 = pygame.font.SysFont("couriernew", 45)

fonts = [custom_font, font1, font2, font3, font4]

# message (без персональных данных, школьно-безопасное)
message = "KEEP YOUR DREAMS ALIVE"

letters = []
x = 40
y = 150

# ---------- Generate ransom style letters ----------
for char in message:
    if char == " ":
        x += 60
        continue

    font = random.choice(fonts)

    # Цвет текста
    text_color = (random.randrange(50, 255), random.randrange(50, 255), random.randrange(50, 255))

    text = font.render(char, True, text_color)
    rect = text.get_rect()

    # Рандомные смещения
    rect.x = x + random.randint(-5, 5)
    rect.y = y + random.randint(-30, 30)

    # Размер бумажки
    padding = 25
    paper_rect = rect.inflate(padding, padding)

    # Цвет фона бумажки (цвет от текста отличается)
    paper_color = (
        random.randrange(80, 255),
        random.randrange(80, 255),
        random.randrange(80, 255)
    )

    angle = random.randint(-25, 25)  # наклон буквы

    letters.append({
        "text": text,
        "rect": paper_rect,
        "angle": angle,
        "paper_color": paper_color,
    })

    x += paper_rect.width - 5  # смещение следующей буквы

# *********GAME LOOP**********
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((20, 20, 20))  # фон сцены

    # draw letters
    for l in letters:
        pygame.draw.rect(window, l["paper_color"], l["rect"])  # фон-бумажка
        pygame.draw.rect(window, (0, 0, 0), l["rect"], 3)  # черная обводка

        rotated = pygame.transform.rotate(l["text"], l["angle"])
        window.blit(rotated, rotated.get_rect(center=l["rect"].center))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
