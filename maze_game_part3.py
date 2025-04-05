from pygame import *

#parent class for other sprites
class GameSprite(sprite.Sprite):
    #class constructors
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        # Calling the class constructor (Sprite):
        sprite.Sprite.__init__(self)
        # each sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        # each sprite must store the rect property - the rectangle which it's inscribed in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # the method that draws the character in the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#class of the main player
class Player(GameSprite):
    #the method in which the sprite is controlled by the arrow keys of the keyboard
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        # Calling the class constructor (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        ''' moves the character by applying the current horizontal and vertical speed'''
        # horizontal movement first
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
            
        # if we go behind the wall, we'll stand right up to it
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: # we're going to the right, the character's right edge appears right up to the left edge of the wall
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) # if several walls were touched at once, then the right edge is the minimum possible
        elif self.x_speed < 0: # we're going to the left, then put the character's left edge right up to the right edge of the wall
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) # if several walls have been touched, then the left edge is the maximum
        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        # if we go behind the wall, we'll stand right up to it
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: # going down
            for p in platforms_touched:
                self.y_speed = 0
                # We're checking which of the platforms is the highest from the ones below, aligning with it, and then take it as our support:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: # going up
            for p in platforms_touched:
                self.y_speed = 0 # the vertical speed is dampened when colliding with the wall
                self.rect.top = max(self.rect.top, p.rect.bottom) # aligning the upper edge along the lower edges of the walls that were touched
    # the "shot" method (we use the player's place to create a bullet there)
    def fire(self):
        bullet = Bullet('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/bullet.png', self.rect.right, self.rect.centery, 15, 20, 15)
        bullets.add(bullet)


# the enemy sprite class   
class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Calling the class constructor (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    #movement of an enemy horizontally
    def update(self):
        if self.rect.x <= 540: #w1.wall_x + w1.wall_width
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
    #movement of an enemy vertically
    # side = "up"
    # def vertical(self):
    #     if self.rect.y <= 20: #w1.wall_x + w1.wall_width
    #         self.side = "down"
    #     if self.rect.y >= 100:
    #         self.side = "up"
    #     if self.side == "up":
    #         self.rect.y -= self.speed
    #     else:
    #         self.rect.y += self.speed

# the bullet sprite's class  
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Calling the class constructor (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    #movement of an enemy
    def update(self):
        self.rect.x += self.speed
        # disappears after reaching the edge of the screen
        if self.rect.x > win_width+10:
            self.kill()
    
#Creating a window
win_width = 1000
win_height = 700
display.set_caption("Maze Game")
window = display.set_mode((win_width, win_height))
back = (120, 200, 100)#setting the color according to the RGB color scheme

#creating a group for the walls
barriers = sprite.Group()

#creating a group for the bullets
bullets = sprite.Group()

#creating a group for the monsters
monsters = sprite.Group()
monsters_v = sprite.Group()

#creating wall pictures
# w1 = GameSprite('D:/Data Scientist/Algoritmics/Python Pro/Modul 6/aksesori_game/platform2.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
# w2 = GameSprite('D:/Data Scientist/Algoritmics/Python Pro/Modul 6/aksesori_game/platform2_v.png', 370, 100, 50, 400)
w3 = GameSprite("C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20241210.135312.0\\data\\student\\100085841\\1170577\\platform2_v.png" , 0, 550, 400, 50)
w6 = GameSprite("C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20241210.135312.0\\data\\student\\100085841\\1170577\\platform2_v.png" , 100, 400, 400, 50)
w7 = GameSprite("C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20241210.135312.0\\data\\student\\100085841\\1170577\\platform2_v.png" , 0, 250, 400, 50)
w8 = GameSprite("C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20241210.135312.0\\data\\student\\100085841\\1170577\\platform2_v.png" , 100, 100, 400, 50)
w9 = GameSprite("C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20241210.135312.0\\data\\student\\100085841\\1170577\\platform2_v.png" , 650, 0, 50, 90)
w10 = GameSprite("C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20241210.135312.0\\data\\student\\100085841\\1170577\\platform2_v.png" , 800, 0, 50, 90)
w11 = GameSprite("C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20241210.135312.0\\data\\student\\100085841\\1170577\\platform2_v.png" , 950, 0, 50, 90)
w12 = GameSprite("C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20241210.135312.0\\data\\student\\100085841\\1170577\\platform2_v.png" , 0, 0, 50, 50)
w13 = GameSprite("C:\\Program Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20241210.135312.0\\data\\student\\100085841\\1170577\\platform2_v.png" , 870, 600, 50, 100)
w14 = GameSprite(" , 700, 600, 50, 100)

#adding walls to the group
# barriers.add(w1)
# barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)
barriers.add(w7)
barriers.add(w8)
barriers.add(w9)
barriers.add(w10)
barriers.add(w11)
# barriers.add(w12)
barriers.add(w13)
barriers.add(w14)

from random import *


#creating sprites
packman = Player('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/hero.png', 5, win_height - 80, 80, 80, 0, 0)
final_sprite = GameSprite('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/pac-1.png', win_width - 85, win_height - 100, 80, 80)


monster1 = Enemy('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/cyborg.png', win_width - 80, 100, 80, 80, randint(15, 50))
monster2 = Enemy('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/cyborg.png', win_width - 80, 180, 80, 80, randint(15, 50))
monster3 = Enemy('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/cyborg.png', win_width - 70, 260, 80, 80, randint(15, 50))
monster4 = Enemy('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/cyborg.png', win_width - 70, 340, 80, 80, randint(15, 50))
monster5 = Enemy('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/cyborg.png', win_width - 70, 420, 80, 80, randint(15, 50))
monster6 = Enemy('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/cyborg.png', win_width - 70, 500, 80, 80, randint(15, 50) )
monster7 = Enemy('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/cyborg.png', 20, 20, 80, 80, randint(15, 50) )



#adding a monster to the group
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)
monsters.add(monster6)
monsters_v.add(monster7)



#the variable responsible for how the game has ended
finish = False
#game loop
run = True
while run:
    #the loop is triggered every 0.05 seconds
    time.delay(50)
    #iterating through all the events that could have happened
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = - 15
            elif e.key == K_RIGHT:
                packman.x_speed = 15
            elif e.key == K_UP:
                packman.y_speed = -15
            elif e.key == K_DOWN:
                packman.y_speed = 15
            elif e.key == K_SPACE:
                packman.fire()


        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0


    #checking that the game is not finished yet
    if not finish:
        #updating the background every iteration
        window.fill(back)# fill the window with color
        
        #launching sprite movements
        packman.update()
        bullets.update()

        #updating them in a new location at each iteration of the loop
        packman.reset()
        #drawing the walls 2
        #w1.reset()
        #w2.reset()
        bullets.draw(window)
        barriers.draw(window)
        final_sprite.reset()


        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        # sprite.groupcollide(monsters_v, bullets, True, True)
        # monsters_v.
        # monsters_v.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)


        #Checking the character's collision with the enemy and walls
        if sprite.spritecollide(packman, monsters, False):
            finish = True
            #calculate the ratio
            img = image.load('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/game-over_1.png')
            d = img.get_width() // img.get_height()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))


        if sprite.collide_rect(packman, final_sprite):
            finish = True
            img = image.load('D:/Data Scientist/Algoritmics/Python Pro I/Modul 6/Executable File/aksesori_game/thumb.jpg')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

    display.update()
