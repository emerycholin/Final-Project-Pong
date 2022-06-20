print('\nWelcome to PONG. The game is very simple and easy to learn. Simply use the up and down arrows to control the '
    "right side and W   and S for the left. Your goal is to try not to let the ball past your paddle. First side to 10 "
    'points wins. Goodluck!')

start = True
while start:
    game_speed = input('\n\nWould you like to play on: easy (E), medium (M), or hard (H)?  :')
    if game_speed == 'E':
        set_speed = 5
        print('\nOpen the Pygame window to begin playing. goodluck\n')        
        start = False
    if game_speed == 'M':
        set_speed = 10
        print('\nOpen the Pygame window to begin playing. goodluck\n')
        start = False
    if game_speed == 'H':
        set_speed = 15
        print('\nOoo, a challenge. Open the Pygame window to begin playing. goodluck\n')
        start = False

import pygame
pygame.init()
window = pygame.display.set_mode((750, 500))
pygame.display.set_caption('Final Project: Pong')

white = (255,255,255)
black = (0, 0, 0)


class l_paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0        
class r_paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0      
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = set_speed
        self.dx = 1
        self.dy = 1
    
    
l_paddle = l_paddle()
l_paddle.rect.x = 10
l_paddle.rect.y = 225
l_paddle.speed = 10

r_paddle = r_paddle()
r_paddle.rect.x = 730
r_paddle.rect.y = 225
r_paddle.speed = 10

ball = Ball()
ball.rect.x = 375
ball.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(l_paddle, r_paddle, ball)

all_sprites.draw(window)
pygame.display.update()


def draw():
    window.fill(black)

    font = pygame.font.SysFont('Standard', 40)
    text = font.render('PONG', False, white)
    title_text = text.get_rect()
    title_text.center = (750 // 2, 25)
    window.blit(text, title_text)

    lp_score = font.render(str(l_paddle.points), False, white)
    lpRect = lp_score.get_rect()
    lpRect.center = (50, 50)
    window.blit(lp_score, lpRect)

    rp_score = font.render(str(r_paddle.points), False, white)
    rpRect = rp_score.get_rect()
    rpRect.center = (700, 50)
    window.blit(rp_score, rpRect)

    all_sprites.draw(window)
    pygame.display.update()


run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        l_paddle.rect.y += -10
    if key[pygame.K_s]:
        l_paddle.rect.y += 10
    if key[pygame.K_UP]:
        r_paddle.rect.y += -10
    if key[pygame.K_DOWN]:
        r_paddle.rect.y += 10

    if ball.rect.y > 490:
        ball.dy = -1
    if ball.rect.y < 1:
        ball.dy = 1
    if ball.rect.x > 740:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx = -1
        l_paddle.points += 1
    if ball.rect.x < 1:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx = 1
        r_paddle.points += 1
    if l_paddle.rect.colliderect(ball.rect):
        ball.dx = 1
    if r_paddle.rect.colliderect(ball.rect):
        ball.dx = -1
        
    ball.rect.x += ball.speed * ball.dx
    ball.rect.y += ball.speed * ball.dy
    
    draw()
    
    if l_paddle.points > 9:  
        file = open('PONG_History.txt', 'a')
        file.write('\n> left side win')
        file.close()       
        print('\nLeft side won this time. Please run the game again and having fun. If you want to see your previous'
          ' scores then go into the file where the code is located. Open the notes file called PONG_History and'
          ' see your whole game history')
        pygame.quit()
        run = False  
        
    if r_paddle.points > 9:   
        file = open('PONG_History.txt', 'a')
        file.write('\n> right side win')
        file.close()       
        print('\nRight side won this time. Please run the game again and having fun. If you want to see your previous'
          ' scores then go into the file where the code is located. Open the notes file called PONG_History and'
          ' see your whole game history')
        pygame.quit()
        run = False  
    
           
quit()
