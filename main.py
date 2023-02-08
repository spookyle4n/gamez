import pygame
import sys
import math

# Initialize the game engine
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Set up the clock
clock = pygame.time.Clock()

# Load the player image
player_image = pygame.image.load("player.png").convert_alpha()

# Set up the player rectangle
player_rect = player_image.get_rect()

# Set up the player position
player_rect.x = 400
player_rect.y = 300

# Initialize the player's bullet list
bullets = []

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    # Handle player shooting
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
        bullet_rect = pygame.Rect(player_rect.x + 20, player_rect.y, 10, 10)
        bullets.append(bullet_rect)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the player
    screen.blit(player_image, player_rect)

    # Move the player's bullets
    for bullet in bullets:
        bullet.y -= 5
        pygame.draw.rect(screen, (0, 0, 0), bullet)

    # Update the display
    pygame.display.flip()

    # Limit the framerate
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()
