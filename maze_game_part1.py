from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        spritce.Sprite.__init__(self)  
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

win_width = 700
win_height = 500
display.set_caption("Maze")
window = display.set_mode((win_width, win_height))
back = (150, 100, 50)  # OPTIONAL FOR YOU

w1 = GameSprite('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/L2/platform2.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = GameSprite('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/L2/platform2_v.png', 370, 100, 50, 400)
w3 = GameSprite('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/L2/platform2.png', 400, 100, 400, 50)
# player = GameSprite('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/L2/pac-1.png', 630, 20, 80, 80)

packman = Player('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/L2/hero.png', 5, win_height - 80, 80, 80, 0, 0)

run = True
while run:
    time.delay(50)
    window.fill(back)
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -20
            elif e.key == K_RIGHT:
                packman.x_speed = 20
            elif e.key == K_UP:
                packman.y_speed = -20
            elif e.key == K_DOWN:
                packman.y_speed = 20
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
    w1.reset()
    w2.reset()
    w3.reset()
    packman.reset()
  
    packman.move()
    display.update()























