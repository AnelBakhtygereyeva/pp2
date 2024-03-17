import pygame
import datetime
import pytz

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y, is_minutes=False):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0
        self.is_minutes = is_minutes

    def update(self):
        almaty = pytz.timezone('Asia/Almaty')
        current_time = datetime.datetime.now(almaty)
        minutes = current_time.minute
        seconds = current_time.second
        if self.is_minutes:
            if self.angle == 270:
                minutes = (minutes + 1) % 60
            self.angle = (minutes + seconds / 60) * (360 / 60) * -1
        else:
            self.angle = seconds * (360/60) * -1

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mickey mouse clock!")
pygame.display.set_icon(pygame.image.load("images/mickeyIcon.jpg"))
clock = pygame.time.Clock()

clock_image = pygame.image.load("images/main-clock.png")
right_hand_minutes = pygame.image.load("images/right-hand.png")
left_hand_seconds = pygame.image.load("images/left-hand.png")

player1 = Player(right_hand_minutes, *screen.get_rect().center, is_minutes=True)
all_sprites1 = pygame.sprite.Group(player1)

player2 = Player(left_hand_seconds, *screen.get_rect().center)
all_sprites2 = pygame.sprite.Group(player2)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprites1.update()
    all_sprites2.update()

    screen.fill((255, 255, 255))
    screen.blit(clock_image, clock_image.get_rect(center = screen.get_rect().center))
    all_sprites1.draw(screen)
    all_sprites2.draw(screen)
    pygame.display.flip()

pygame.quit()
exit()