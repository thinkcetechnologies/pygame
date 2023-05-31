import pygame
from math import *

class MyGame:
    def __init__(self):
        pygame.init()
        self.width = 600
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tennis (BANANA TECHNOLOGIES)")
        self.clock = pygame.time.Clock()
        self.bw = 300
        self.bh = 250
        self.center = self.bw, self.bh
        self.top = 250, 20
        self.running = True
        self.gameover = False
        self.white = (0, 255, 255)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.yellow = (255, 255, 0)
        self.pwidth = 250
        self.win = ""
        self.ewidth = 250
        self.pheight = 480
        self.eheight = 0
        self.velocity = 8
        self.ball_x = -self.velocity
        self.ball_y = self.velocity
        self.background = self.white
        self.velocity = 8
        self.player1_score = 0
        self.player2_score = 0
        self.gameLoop()

    def gameLoop(self):
        while self.running:
            self.clock.tick(30)
            self.gameOver()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.pwidth > 0:
                self.pwidth = self.pwidth - 10
            if keys[pygame.K_RIGHT] and self.pwidth < 500:
                self.pwidth = self.pwidth + 10
            if keys[pygame.K_a] and self.ewidth > 0:
                self.ewidth = self.ewidth - 10
            if keys[pygame.K_d] and self.ewidth < 500:
                self.ewidth = self.ewidth + 10
            if keys[pygame.K_SPACE]:
                self.ball_x = 0
                self.ball_y = 0
                self.test("PAUSED PRESS C TO RESUME", 140, 230, self.green, 35)
                pygame.display.update()
            if keys[pygame.K_c]:
                self.ball_x = self.velocity
                self.ball_y = self.velocity

            self.getUI()
            self.move()
            
            self.collide = self.collision(self.pwidth, (self.pheight-10), self.bw, self.bh)
            if self.collide:
                self.ball_y = -self.velocity
            elif self.bh >= 490:
                # self.bw = 300
                # self.bh = 250
                self.player2_score += 1

            self.collided = self.collision2(self.ewidth, (self.eheight+30), self.bw, self.bh)
            if self.collided:
                self.ball_y = self.velocity
            elif self.bh <= 0:
                # self.bw = 300
                # self.bh = 250
                self.player1_score += 1

            if self.player1_score == 10 or self.player2_score == 10:
                if self.player2_score > self.player1_score:
                    self.win = "PLAYER 2 WINS"
                    self.player1_score = 0
                    self.player2_score = 0
                    self.ewidth = 250
                    self.pwidth = 250
                    self.gameover = True
                else:
                    self.win = "PLAYER 1 WINS"
                    self.player1_score = 0
                    self.player2_score = 0
                    self.gameover = True

    def move(self):
        self.bw = self.bw + self.ball_x
        self.bh = self.bh + self.ball_y
        if self.bw <= 0:
            self.ball_x = self.velocity
        if self.bw >=590:
            self.ball_x = -self.velocity
        if self.bh <= 0:
            self.ball_y = self.velocity
        if self.bh >= 490:
            self.ball_y = -self.velocity

    def getUI(self):
        self.screen.fill(self.background)
        self.drawUI()
        self.test("Player 2 Score: " + str(self.player2_score), 30, 30, self.black, 25)
        self.test("Player 1 Score: " + str(self.player1_score), 30, 450, self.black, 25)
        pygame.display.update()

    def drawUI(self):
        self.ball = pygame.draw.circle(self.screen, self.red, (self.bw, self.bh), 8)
        pygame.draw.rect(self.screen, self.blue, (self.ewidth, self.eheight, 100, 20))
        self.prayer = pygame.draw.rect(self.screen, self.green, (self.pwidth, self.pheight, 100, 20))

    def collision(self, playerX,playerY,ballX,ballY):
        if (ballY >= playerY) and (ballX <= (playerX+100)):
            if (ballX >= playerX) and (ballY >= playerY):
                return True
        return False
        
    def collision2(self, playerX,playerY,ballX,ballY):
        if (ballY <= playerY) and (ballX <= (playerX+100)):
            if (ballX >= playerX) and (ballY <= playerY):
                return True
        return False

    def pause():
        self.ball_x = 0
        self.ball_y = 0
        self.test("PAUSED PRESS C TO RESUME", 140, 230, self.green, 35)
        pygame.display.update()

    def gameOver(self):
        while self.gameover:
            self.screen.fill(self.background)
            self.test("GAME OVER: " + self.win, 130, 200, self.red,35)
            self.test("PRESS C TO CONTINUE OR Q TO QUIT", 120, 250, self.yellow,30)
            self.test("DESIGN AND DEVELOPED BY AFARI SAMUEL ADUSEI", 40, 370, self.blue,30)
            self.test("(THE CEO OF BANANA TECHNOLOGIES)", 120, 400, self.blue,30)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                    self.gameover = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_c]:
                self.running = True
                self.gameover = False
            if keys[pygame.K_q]:
                self.gameover = False
                self.running = False
            pygame.display.update()

    def test(self,text,posX,posY,color,size):
        font = pygame.font.SysFont(None, size) 
        img = font.render(text, True, color)
        self.screen.blit(img,(posX,posY))


MyGame()
