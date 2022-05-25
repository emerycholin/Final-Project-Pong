import pygame
pygame.init()


window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Final Project: Pong')


class left_paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(255,255,255)
        self.rect = self.image.get_rect()

class right_paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(255,255,255)
        self.rect = self.image.get_rect()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(255,255,255)
        self.rect = self.image.get_rect()
