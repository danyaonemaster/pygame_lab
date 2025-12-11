# collage_sailor_centered_strict.py
import pygame
import random
import math

pygame.init()
W, H = 1000, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.display.set_caption("Sailor Moon Collage (Perfect Center)")

IMAGE_FILES = [
    "images/img.png",
    "images/HD-wallpaper-sailor-moon-usagi-tsukino-full-moon-serena-flowers-bunny.jpg",
    "images/pastel-sailor-moon-hch4pze9qnnu0gt7.png",
    "images/sailor-moon-crystal-lupr7qj5eobl66d4.jpg"
]

# ---------------- load images ----------------
surfaces = []
for path in IMAGE_FILES:
    try:
        img = pygame.image.load(path).convert_alpha()

        # reduce size if too large
        w, h = img.get_size()
        scale = min(550/w, 550/h, 1)
        img = pygame.transform.smoothscale(img, (int(w*scale), int(h*scale)))

        surfaces.append(img)
        print()
    except:
        print()

if not surfaces:
    pygame.quit()
    raise SystemExit

# ---------------- создаём объекты ровно по центру ----------------
items = []
center = (W // 2, H // 2)

for s in surfaces:
    items.append({
        "surf": s,
        "angle": random.uniform(-10, 10),
        "phase": random.uniform(0, math.pi * 2),
        "speed": random.uniform(0.3, 1.0),
        "scale": random.uniform(0.9, 1.1)
    })

# ---------------- game loop ----------------
running = True
start_t = pygame.time.get_ticks() / 1000

while running:
    dt = clock.tick(60) / 1000
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    t = pygame.time.get_ticks() / 1000 - start_t

    screen.fill((18, 18, 20))

    # draw slight background noise
    for i in range(60):
        xx = (i * 37 + int(t * 30)) % W
        yy = (i * 53 + int(t * 20)) % H
        pygame.draw.circle(screen, (25, 25, 30), (xx, yy), 2)

    # draw all images EXACTLY centered
    for it in items:
        surf = it["surf"]

        # optional gentle floating animation
        dx = math.sin(t * it["speed"] + it["phase"]) * 6
        dy = math.cos(t * it["speed"] + it["phase"]) * 6

        # scaling
        sw = int(surf.get_width() * it["scale"])
        sh = int(surf.get_height() * it["scale"])
        scaled = pygame.transform.smoothscale(surf, (sw, sh))

        # rotation
        ang = it["angle"] + math.sin(t * 0.5 + it["phase"]) * 4
        rotated = pygame.transform.rotate(scaled, ang)

        rect = rotated.get_rect(center=(center[0] + dx, center[1] + dy))

        # shadow
        shadow = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow, (0, 0, 0, 120), (0, 0, rect.width, rect.height))
        screen.blit(shadow, (rect.x + 6, rect.y + 6))

        screen.blit(rotated, rect.topleft)

    pygame.display.flip()

pygame.quit()
