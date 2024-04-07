import pygame 
import random
import math
pygame.init()

#basic
W, H = 1200, 800
FPS = 60

#some settings
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
paused = False
bg = (100, 100, 100)
main_menu_bg = (0,0,0)
overlay_surface = pygame.Surface((W, H), pygame.SRCALPHA)
overlay_surface.fill((50, 50, 50, 0)) 
DARK_GRAY = (50, 50, 50)

#to reset the game when pressing the key -> n
def reset_game():
    global paddleW, paddleH, paddleSpeed, paddle, ball, dx, dy, game_score
    paddleW = 150
    paddleH = 25
    paddleSpeed = 20
    paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)
    ball = pygame.Rect(random.randrange(20, W - 20), H // 2, 20, 20)
    dx, dy = 1, -1
    game_score = 0

    # Reinitialize block settings
    block_list.clear()
    color_list.clear()

    rows = 4
    columns = 10

    for j in range(rows):
        for i in range(columns):
            if i % 4 == 3:
                block = pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50)
                color = DARK_GRAY
            else:
                block = pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50)
                color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
                if ((i > random.randrange(0,11) and i < random.randrange(0,11)) and j > random.randrange(0,4)) or ((i > random.randrange(0,4) and i < random.randrange(0,11)) and j > random.randrange(0,7)):
                    color = (255, 255, 0)
            block_list.append(block)
            color_list.append(color)
            paused = False

#paddle base
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball base
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#sound
collision_sound = pygame.mixer.Sound('ackanoid/catch.mp3')

#detecting the collision
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings initializing
block_list = []
color_list = []

rows = 4
columns = 10

for j in range(rows):
    for i in range(columns):
        if i % 4 == 3:
            block = pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50)
            color = DARK_GRAY
        else:
            block = pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50)
            color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
            if ((i > random.randrange(0,11) and i < random.randrange(0,11)) and j > random.randrange(0,4)) or ((i > random.randrange(0,4) and i < random.randrange(0,11)) and j > random.randrange(0,7)):
                color = (255, 255, 0)
        block_list.append(block)
        color_list.append(color)



#game over screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#win screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

initial_paddle_width = paddleW
shrink_rate = 3

last_time = pygame.time.get_ticks()

#drawing star on special bricks
def draw_star(surface, color, center, size=20):
    #draw a star with given color, center position, and size
    x, y = center
    outer_radius = size / 2
    inner_radius = outer_radius / 2

    # define angles for each point of the star
    angles = [math.radians(angle) for angle in range(0, 360, int(360 / 10))]

    #calculate coordinates for each point
    points = []
    for index, angle in enumerate(angles):
        if index % 2 == 0:
            points.append((x + math.cos(angle) * outer_radius, y + math.sin(angle) * outer_radius))
        else:
            points.append((x + math.cos(angle) * inner_radius * 0.7, y + math.sin(angle) * inner_radius * 0.7))

    pygame.draw.polygon(surface, color, points)

#game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = True
            elif event.key == pygame.K_m:
                paused = True
#game screen
    if not paused:
        screen.fill(bg)

        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - last_time) / 1000  # Convert milliseconds to seconds
        last_time = current_time

    #increase ball speed after time
        ballSpeed += elapsed_time * 0.1

    #shrink paddle after time
        paddleW -= elapsed_time * shrink_rate
        paddleW = max(paddleW, ballRadius * 4) 

    #update paddle rectangle
        paddle.width = int(paddleW)
        paddle.x = max(min(paddle.x, W - paddle.width), 0) # -> Keep paddle within screen bounds
    

    #drawing the blocks
        for color, block in enumerate (block_list):
            pygame.draw.rect(screen, color_list[color], block)
            #draw star in the center of yellow blocks
            if color_list[color] == (255, 255, 0):
                draw_star(screen, (0, 0, 0), block.center)

    #drawing the paddle
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    #drawing the ball
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)


    #ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

    #collision left and right borders 
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
    #collision the top border
        if ball.centery < ballRadius + 50: 
            dy = -dy
    #collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

    #collision with blocks
        hitIndex = ball.collidelist(block_list)

        if hitIndex != -1:
            hitRect = block_list[hitIndex]
            hitColor = color_list[hitIndex]
            if hitColor != DARK_GRAY:
                block_list.pop(hitIndex)
                color_list.pop(hitIndex)
                dx, dy = detect_collision(dx, dy, ball, hitRect)
                game_score += 1
                collision_sound.play()
            #check if the hit block is gold (yellow)
                if hitColor == (255, 255, 0):
                #increase paddle width
                    paddleW += 40
                    paddle.width = int(paddleW)
            else:
                dx, dy = detect_collision(dx, dy, ball, hitRect)
        
    #game score text
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)

        game_score_text_win = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))

#main and pause menu screens
    else:
        key = pygame.key.get_pressed()
        #pause menu
        if key[pygame.K_p]:
            screen.blit(overlay_surface, (0,0))
            font = pygame.font.SysFont('comicsansms', 40)
            pause_text = font.render("Pause Menu", True, (0, 255, 255))
            PauseRect = pause_text.get_rect()
            PauseRect.center = (W // 2, H // 2 - 100)
            screen.blit(pause_text, PauseRect)

            continue_text = font.render("Continue (Press C)", True, (255, 255, 255))
            continueRect = continue_text.get_rect()
            continueRect.center = (W // 2, H // 2 - 20)
            screen.blit(continue_text, continueRect)

            new_game_text = font.render("New Game (Press N)", True, (255, 255, 255))
            newGameRect = new_game_text.get_rect()
            newGameRect.center = (W // 2, H // 2 + 30)
            screen.blit(new_game_text, newGameRect)

            help_text = font.render("Help (Press H)", True, (255, 255, 255))
            helpTextRect = help_text.get_rect()
            helpTextRect.center = (W // 2, H // 2 + 80)
            screen.blit(help_text, helpTextRect)

            exit_text = font.render("Exit (Press ESC)", True, (255, 255, 255))
            exitRect = exit_text.get_rect()
            exitRect.center = (W // 2, H // 2 + 130)
            screen.blit(exit_text, exitRect)

        #main menu
        elif key[pygame.K_m]:
            screen.fill(main_menu_bg)
            font = pygame.font.SysFont('comicsansms', 40)
            pause_text = font.render("Main menu", True, (0, 255, 255))
            PauseRect = pause_text.get_rect()
            PauseRect.center = (W // 2, H // 2 - 100)
            screen.blit(pause_text, PauseRect)

            continue_text = font.render("Continue (Press C)", True, (255, 255, 255))
            continueRect = continue_text.get_rect()
            continueRect.center = (W // 2, H // 2 - 20)
            screen.blit(continue_text, continueRect)

            new_game_text = font.render("New Game (Press N)", True, (255, 255, 255))
            newGameRect = new_game_text.get_rect()
            newGameRect.center = (W // 2, H // 2 + 30)
            screen.blit(new_game_text, newGameRect)

            exit_text = font.render("Exit (Press ESC)", True, (255, 255, 255))
            exitRect = exit_text.get_rect()
            exitRect.center = (W // 2, H // 2 + 80)
            screen.blit(exit_text, exitRect)


 
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
        screen.blit(game_score_text, game_score_rect)
    elif not len(block_list) - 8:
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
        screen.blit(game_score_text_win, game_score_rect)
    
    #paddle control and setting keys
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed
    if key[pygame.K_n]:
        paused = False
        reset_game()
    if key[pygame.K_c]:
        paused = False
    if key[pygame.K_ESCAPE]:
        done = True
    if key[pygame.K_h]:
        paddleW = 200
        ballSpeed = 3
        paused = False
    
    #screen update
    pygame.display.flip()
    clock.tick(FPS)