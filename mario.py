import pygame as pg

pg.init()

class GameSprite(pg.sprite.Sprite):
    def __init__(self, image, x, y, width, height, step=4):
        super().__init__()
        self.width = width
        self.height = height
        self.image = image
        self.sprite = pg.transform.scale(pg.image.load(self.image), (self.width, self.height)).convert_alpha()
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.step = step
        
    def reset(self):
        self.sprite = pg.transform.scale(pg.image.load(self.image), (self.width, self.height)).convert_alpha()
        window.blit(self.sprite, self.rect)


class Player(GameSprite):
    def __init__(self, image, x, y, width, height, step=4):
        super().__init__(image, x, y, width, height)
        self.jumped = False
    
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.rect.x += self.step
        if keys[pg.K_a]:
            self.rect.x -= self.step
        if keys[pg.K_SPACE] and not self.jumped:
            self.image = 'jump.png'
            self.jumped = True
        if self.rect.y > 400 and self.jumped:
            self.rect.y -= 10
        else:
            self.jumped = False
        if not self.jumped:
            self.rect.y += 10
            if self.rect.y > 575:
                self.rect.y = 575 
                self.image = 'mario.png'          
        


height = 700
width = 700
FPS = 40

window = pg.display.set_mode((height, width))
bg_sprite = GameSprite('bg.png', 0, 0, width, height, 0)
pg.display.set_caption('TIPAMARIO')

clock = pg.time.Clock()


player = Player('mario.png', 100, 575, 70, 100)



game = True
while game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
    
    bg_sprite.reset()

    player.reset()
    player.move()
    
    pg.display.update()
    clock.tick(FPS)
    