import pygame
import sys
import random
from pygame.locals import *
import math
from pygame import mixer

class Car:
    def __init__(self):
        pygame.init()
        mixer.music.load("bensound-creativeminds.mp3")
        mixer.music.play(1)
        self.screen_width = 700
        self.screen_height = 650
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        pygame.display.set_caption("Car Race.")
        icon_image= pygame.image.load("download.jpeg")
        pygame.display.set_icon(icon_image)
        self.road_image = pygame.image.load('download.jpg')
        self.net = (pygame.image.load("car.png"))
        self.bgX = 660
        self.bgX2 = -20
        self.running = True
        self.clock = pygame.time.Clock()
        self.speed = 30
        self.carX = 200
        self.carY = 450
        self.font = pygame.font.SysFont("comicsans", 100)
        self.fonts = pygame.font.SysFont("comicsans", 50)
        self.carX_change = 0
        self.carY_change = 0
        self.speed = 30
        self.show_level = 0
        self.show_levelX = 550
        self.show_levelY = 10
        self.score_value = 10
        self.show_high_scoreX = 220
        self.show_high_scoreY = 10
        self.gameoverX = 150
        self.gameoverY = 250
        self.ScoreShowX = 5
        self.ScoreShowY = 10
        self.show_game_overX = 200
        self.show_game_overY = 400
        self.show_levelsX = 200
        self.show_levelsY = 330
        self.velocity = 12
        self.net = []
        self.carrandomX = []
        self.carrandomY = []
        self.carrandomX_change = []
        self.carrandomY_change = []
        self.number = 3
        self.gameover = True
        for i in range(self.number):
            self.net.append(pygame.image.load("car.png"))
            self.carrandomX.append(i*200)
            self.carrandomY.append(i*100)
            self.carrandomX_change.append(0)
            self.carrandomY_change.append(self.velocity)
        self.Car_staus = False
        self.Road_speed = 0
    def collide_sound(self):
            self.gunhit = mixer.Sound("boom.wav")
            self.gunhit.play()
    def show_game(self,x,y):
        self.score = (self.font.render( "Game Over!" , True ,(255,255,255)))
        self.screen.blit(self.score,(x,y))

    def show_score(self,x,y):
        self.score = self.fonts.render(" Score : " + str(self.score_value), True ,(255,255,255))
        self.screen.blit(self.score,(x,y))
    def show_Levels(self,x,y):
        self.score = self.fonts.render(str(self.show_level)+ ": Level", True ,(255,255,255))
        self.screen.blit(self.score,(x,y))
    def show_high_score(self,x3,y3):
        filename = 'programming.txt'
        high_scores = open(filename, 'r+')
        previous = (high_scores.read())
        het = int(previous)
        inp = int(self.score_value)
        if inp > het:
            inp = str(inp)
            with open(filename, 'w') as file_object:
                file_object.write(inp)

        self.destroy = self.fonts.render("HighScore " + str(het) , True ,(255,255,255))
        self.screen.blit(self.destroy,(x3,y3))
    def show_game_over(self,x,y):
        self.score = self.font.render(" Score : " + str(self.score_value), True ,(255,255,255))
        self.screen.blit(self.score,(x,y))
    def show_game_Levels(self,x,y):
        self.score = self.font.render(" Level : " + str(self.show_level), True ,(255,255,255))
        self.screen.blit(self.score,(x,y))
    def random_car(self,x,y,i):
        self.screen.blit(self.net[i],(x,y))
    def iscollision(self,enemyX,enemyY,mycayX,mycayY):
        self.distance = math.sqrt((math.pow(enemyX-mycayX,2))+(math.pow(enemyY-mycayY,2)))
        if self.distance < 85:
            return True
        else:
            return False
    def recreatcar(self,enemyY):
        self.check = enemyY
        if self.check > 700:
            return True
        else:
            return False
    def road(self):
        self.road_image = pygame.image.load('download.png')
        self.screen.blit(self.road_image,(0,self.bgX))
        self.screen.blit(self.road_image,(0,self.bgX2))
 
    def car(self,x,y):
        self.car_image = pygame.image.load('car.png')
        self.screen.blit(self.car_image,(x,y))
    def run_game(self):
        while self.running:
            if self.Car_staus:
                self.bgX += 50
                self.bgX2 += 50
                if self.bgX > self.road_image.get_height() * +1:
                    self.bgX = -self.road_image.get_height()
                if self.bgX2 > self.road_image.get_height() * +1:
                    self.bgX2 = -self.road_image.get_height()
            if self.gameover:
                self.bgX += 10
                self.bgX2 += 10
                if self.bgX > self.road_image.get_height() * +1:
                    self.bgX = -self.road_image.get_height()
                if self.bgX2 > self.road_image.get_height() * +1:
                    self.bgX2 = -self.road_image.get_height()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.carX_change = -8
                        self.Road_speed = -1
                    if event.key == pygame.K_RIGHT:
                        self.carX_change = 8
                        self.Road_speed = 1
                    if event.key == pygame.K_DOWN:
                        self.carY_change = 8
                        self.Car_staus = True
                        self.Road_speed = 1
                    if event.key == pygame.K_UP:
                        self.carY_change = -1
                        self.Car_staus = True
                        self.Road_speed = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        self.carX_change = 0
                        self.carY_change = 0
                        self.Car_staus = False
                        self.Road_speed = 0
            self.road()
            self.Road_speed += self.Road_speed
            self.carY += self.carY_change
            self.carX += self.carX_change
            if self.carX <= 150:
                self.carX = 150
            elif self.carX > 470:
                self.carX = 470
            if self.carY <= 0:
                self.carY = 0
            elif self.carY > 500:
                self.carY = 500
            self.car(self.carX,self.carY)
            for i in range(self.number):
                self.recreatcars = self.recreatcar(self.carrandomY[i])
                if self.recreatcars and self.gameover:
                    self.score_value += 30
                    if self.score_value > 60:
                        self.show_level += 1
                        self.velocity += 8
                    self.carrandomX[i] = random.randint(150,500) + 40
                    self.carrandomY[i] = random.randint(-400,-200)
                self.collision = self.iscollision(self.carrandomX[i],self.carrandomY[i],self.carX,self.carY)
                if self.collision:
                    self.Car_staus = False
                    self.gameover = False
                    self.collide_sound()
                    self.show_score(self.ScoreShowX,self.ScoreShowY)
                self.carrandomY[i] += self.carrandomY_change[i]
                self.random_car(self.carrandomX[i],self.carrandomY[i],i)
                if (not self.gameover):
                    self.show_game(self.gameoverX,self.gameoverY)
                    self.show_game_Levels(self.show_levelsX,self.show_levelsY)
                    self.show_game_over(self.show_game_overX,self.show_game_overY)

            if not (self.recreatcars or self.gameover and self.collision):
              self.show_score(self.ScoreShowX,self.ScoreShowY)
              self.show_high_score(self.show_high_scoreX,self.show_high_scoreY)
              self.show_Levels(self.show_levelX,self.show_levelY)
            pygame.display.update()
            pygame.display.flip()   
            self.clock.tick(self.speed)
        
if __name__ == "__main__":
    ai_game = Car()
    ai_game.run_game()
