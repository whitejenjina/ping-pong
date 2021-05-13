#there be game
from pygame import *

speed = 5 
w, h = 1080, 750
window = display.set_mode((w,h))
display.set_caption("pp ro")
bg = transform.scale(image.load("phon.jpg"), (w,h))

class GameSprite(sprite.Sprite):
    # Конструктор
    def __init__(self, img, x, y, speed,w2,h2):
        self.image = transform.scale(image.load(img), (w2,h2))
        self.speed = speed
        # Для контроля столкновений
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class p2(GameSprite):
    def update(self):
        kjenjina = key.get_pressed()

        if kjenjina[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if kjenjina[K_s] and self.rect.y < h - 150:
            self.rect.y += self.speed

class p1(GameSprite):
    def update(self):
        kjenjina = key.get_pressed()

        if kjenjina[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if kjenjina[K_DOWN] and self.rect.y < h - 150:
            self.rect.y += self.speed

    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class ball(GameSprite):
    dx = 1
    dy = 5
    def update(self):
        if self.dx == 1:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        
        if self.dy == 5:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

# Создание персонажей
P2 = p2("pl2.png", 30, 375, 5,30,150)
P1 = p1("pl2.png", 1030, 375, 5,30,150)
myach = ball("ball.png",540,375,4,40,40)
# Переменные игрового цикла
game = True
clock = time.Clock()
FPS = 120

# Настраиваем фоновую музыку
mixer.init()
mixer.music.load("beat.mp3")
mixer.music.play()

font.init()
font = font.Font(None,70)
winp1 = font.render("P1 WIN",True,(75,0,130))
winp2 = font.render("P2 WIN",True,(75,0,130))


# Игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if sprite.collide_rect(P1,myach):
        myach.dx = 2

    if sprite.collide_rect(P2,myach):
        myach.dx = 1 

    if sprite.collide_rect(P2,myach) or sprite.collide_rect(P1,myach):
        myach.speed += 0.2

    if myach.rect.y >= 710:
        myach.dy = 10

    if myach.rect.y <= 0:
        myach.dy = 5    

    if myach.rect.x > 1030:
        Finish = False 

    if myach.rect.x < 0:
        Finish = False

    if e.key == K_r:
        P1.empty()
        P2.empty()
        myach.empty()





    window.blit(bg, (0,0))
    P1.update()
    P2.update()
    myach.update()
    P1.reset()
    P2.reset()
    myach.reset()

    
    display.update()
