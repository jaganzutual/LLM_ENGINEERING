import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()

pygame.quit()
pygame.display.quit()
import random

# Game settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_SPEED = 3
PIPE_GAP = 150
PIPE_FREQ = 1500  # milliseconds

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird Clone')
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
BROWN = (139, 69, 19)
RED = (255, 0, 0)

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.width = 34
        self.height = 24
        self.velocity = 0
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, RED, [(0,0),(self.width, self.height//2),(0,self.height)])

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 50
        self.height = SCREEN_HEIGHT
        self.gap_y = random.randint(100, SCREEN_HEIGHT - 100 - PIPE_GAP)
        self.passed = False

        # Upper pipe
        self.top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        # Lower pipe
        self.bottom_rect = pygame.Rect(self.x, self.gap_y + PIPE_GAP, self.width, self.height - self.gap_y - PIPE_GAP)

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, surface):
        pygame.draw.rect(surface, BROWN, self.top_rect)
        pygame.draw.rect(surface, BROWN, self.bottom_rect)

    def off_screen(self):
        return self.x + self.width < 0

    def collides_with(self, bird):
        return self.top_rect.colliderect(bird.get_rect()) or self.bottom_rect.colliderect(bird.get_rect())

# Main game function
def main():
    bird = Bird()
    pipes = []
    score = 0
    font = pygame.font.SysFont(None, 36)

    # Custom event for adding pipes
    ADD_PIPE = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_PIPE, PIPE_FREQ)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()
            if event.type == ADD_PIPE:
                pipes.append(Pipe(SCREEN_WIDTH))

        # Update
        bird.update()
        for pipe in pipes:
            pipe.update()

        # Collision detection
        if bird.y + bird.height > SCREEN_HEIGHT or bird.y < 0:
            running = False
        for pipe in pipes:
            if pipe.collides_with(bird):
                running = False
            if not pipe.passed and pipe.x + pipe.width < bird.x:
                pipe.passed = True
                score += 1

        # Remove off-screen pipes
        pipes = [pipe for pipe in pipes if not pipe.off_screen()]

        # Draw
        screen.fill(BLUE)
        for pipe in pipes:
            pipe.draw(screen)
        bird.draw(screen)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    # Game over
    game_over_text = font.render('Game Over', True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH//2 - 70, SCREEN_HEIGHT//2))
    pygame.display.flip()
    pygame.time.wait(2000)

if __name__ == '__main__':
    main()
    pygame.quit()
