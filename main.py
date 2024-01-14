import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1000, 700
SPEED = 50
GRAVITY = 0.5
JUMP_HEIGHT = 10
PIPE_WIDTH = 50
PIPE_HEIGHT = 300
PIPE_GAP = 175

WHITE = (255, 255, 255)
RED = (255, 0, 0)

bird_rect = pygame.Rect(50, HEIGHT // 2, 30, 30)
bird_velocity = 0
pipes = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

def draw_pipe(x, height):
    pygame.draw.rect(screen, RED, (x, 0, PIPE_WIDTH, height))
    pygame.draw.rect(screen, RED, (x, height + PIPE_GAP, PIPE_WIDTH, HEIGHT - height - PIPE_GAP))

def game_over():
    screen.fill((0,0,0))
    font = pygame.font.SysFont("consolas", 40)
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()
    sys.exit()

# Run Game
def run_game():
    global bird_velocity, bird_rect, pipes

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = -JUMP_HEIGHT

    bird_rect.y += bird_velocity
    bird_velocity += GRAVITY

    # Generate pipes
    if len(pipes) == 0 or pipes[-1][0] < WIDTH - 300:
        pipe_height = random.randint(50, HEIGHT - 50 - PIPE_GAP)
        pipes.append((WIDTH, pipe_height))

    pipes = [(x - 5, y) for x, y in pipes]

    # Remove off-screen pipes
    pipes = [(x, y) for x, y in pipes if x > -PIPE_WIDTH]

    # Check for collisions
    for pipe in pipes:
        pipe_upper = pygame.Rect(pipe[0], 0, PIPE_WIDTH, pipe[1])
        pipe_lower = pygame.Rect(pipe[0], pipe[1] + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe[1] - PIPE_GAP)

        if bird_rect.colliderect(pipe_upper) or bird_rect.colliderect(pipe_lower) or bird_rect.y < 0 or bird_rect.y > HEIGHT - bird_rect.height:
            game_over()

    screen.fill((0, 0, 0))

    # Draw pipes
    for pipe in pipes:
        draw_pipe(pipe[0], pipe[1])

    pygame.draw.rect(screen, WHITE, bird_rect)
    pygame.display.flip()
    clock.tick(SPEED)


if __name__ == "__main__":
    while True:
        run_game()       