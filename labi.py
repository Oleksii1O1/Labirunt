
from pygame import * 
# Клас героя 
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (65, 65))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
     
    def reset(self): 
        main_win.blit(self.image, (self.rect.x, self.rect.y))  
#Клас Стіни 
class Wall(sprite.Sprite): 
    def __init__(self, wall_image, x, y, width, heigth): 
        super().__init__() 
        self.image = transform.scale(image.load(wall_image), (65, 65)) 
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y = y 
        self.width = width 
        self.heigth = heigth 
    def draw_wall(self): 
        main_win.blit(self.image, (self.rect.x, self.rect.y)) 
# Клас ворога 
class Enemy(GameSprite): 
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__(player_image, player_x, player_y, player_speed) 
        self.direction = 'right'   
#Рух ворога 
    def PYX(self): 
        if self.direction == 'right': 
            self.rect.x += self.speed 
            if self.rect.right >= main_width:   
                self.direction = 'left'  
        elif self.direction == 'left': 
            self.rect.x -= self.speed 
            if self.rect.left <= 0:   
                self.direction = 'right' 
#Вікно(фон) 
main_width = 700 
main_height = 600 
main_win = display.set_mode((main_width, main_height)) 
display.set_caption("Лабіринт") 
 
font.init()  
  
font_win = font.Font(None, 36)    
font_lose = font.Font(None, 36) 
 
#Спрайти 
 
background = transform.scale(image.load("background.jpg"), (main_width, main_height)) 
player = GameSprite('hero.png', main_width-80, 4, 5)   
cyborg = Enemy('cyborg.png', main_width-80, 280, 2)  
final = GameSprite('treasure.png', main_width-120, main_height-80, 0)  
#Стіни 
wall1 = Wall('wall.png', 100, 100, 50, 200) 
wall2 = Wall('wall.png', 200, 300, 50, 200) 
wall3 = Wall('wall.png', 400, 200, 50, 200) 
# Мизика 
mixer.init() 
mixer.music.load("jungles.ogg") 
mixer.music.play(-1) 
 
#Ігровий цикл 
game = True 
FPS = 60 
clock = time.Clock() 
 
while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
    #Рух гравця 
    keys = key.get_pressed() 
    if keys[K_LEFT] and player.rect.x > 0: 
        player.rect.x -= player.speed 
    if keys[K_RIGHT] and player.rect.x < main_width - player.rect.width: 
        player.rect.x += player.speed 
    if keys[K_UP] and player.rect.y > 0: 
        player.rect.y -= player.speed 
    if keys[K_DOWN] and player.rect.y < main_height - player.rect.height: 
        player.rect.y += player.speed 
 
    if player.rect.colliderect(final.rect):    
        print("YOU WIN!")  
        win_text = font_win.render("YOU WIN!", True, (255, 255, 255))    
        main_win.blit(win_text, (main_width // 2 - 80, main_height // 2))  
        mixer.Sound("money.ogg").play()    
  
    elif player.rect.colliderect(wall1.rect) or player.rect.colliderect(wall2.rect) or player.rect.colliderect(wall3.rect) or player.rect.colliderect(cyborg.rect):  
    # Гравець торкнувся стіни або ворога  
        print("YOU LOSE!")  
        player.rect.x -= -9 
        player.rect.y -= -9 
        lose_text = font_lose.render("YOU LOSE!", True, (255, 0, 0))    
        main_win.blit(lose_text, (main_width // 2 - 80, main_height // 2))  
        mixer.Sound("kick.ogg").play() 

        game = False
     
   #Виведення спрайтів 
    main_win.blit(background, (0, 0))     
    player.reset() 
    cyborg.reset() 
    final.reset()  
    cyborg.PYX() 
    wall1.draw_wall() 
    wall2.draw_wall() 
    wall3.draw_wall() 
    #Оновлення екрану 
    display.update() 
    clock.tick(FPS)
