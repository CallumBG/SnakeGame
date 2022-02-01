import pygame
from pygame import display
import gameLoop
from pygame.constants import QUIT

pygame.init()

white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)

gameRunning = True

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
title_font = pygame.font.SysFont("bahnschrift", 50)

dis = pygame.display.get_init()

FPS = 60

#Creates the pygame clock
clock = pygame.time.Clock()

def exitGame():
    pygame.quit()
    quit()

def startGame():
    global gameRunning
    global dis
    gameStarted = True
    gameLoop.startGameLoop(dis)
    gameOverScreen()

def showText(text, color, xPosition, yPosition):
    text = title_font.render(text, True, color)
    dis.blit(text, [xPosition, yPosition, 160, 10])

def gameOverScreen():
    print("game Over")
    onGameOverScreen = True
    quitButton = Button((50,200, 200, 50), "Exit Game", 85, red, exitGame)
    replayButton = Button((300, 200, 200, 50), "Play Again", 85, red, startGame)
    highscoreButton = Button((175, 275, 200, 50), "HighScores", 95, red, highscoreScreen)
    while onGameOverScreen:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            quitButton.get_event(event)
            replayButton.get_event(event)
            highscoreButton.get_event(event)
        dis.fill(white)
        showText("Your Score was: " + str(gameLoop.currentScore), black, 80, 100)
        quitButton.render(dis)
        replayButton.render(dis)
        highscoreButton.render(dis)
        pygame.display.update()

def startScreen(width, height, title):
    global dis
    dis= pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Snake Game')
    clock.tick(FPS)
    quitButton = Button((50,200, 200, 50), "Exit Game", 85, red, exitGame)
    startButton = Button((300, 200, 200, 50), "Start Game", 95, red, startGame)
    highscoreButton = Button((175, 275, 200, 50), "HighScores", 95, red, highscoreScreen)
    while gameRunning:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            quitButton.get_event(event)
            startButton.get_event(event)
            highscoreButton.get_event(event)
        dis.fill(white)
        showText("Snake Game!", black, 130, 70)
        highscoreButton.render(dis)
        quitButton.render(dis)
        startButton.render(dis)
        pygame.display.update()

def homeScreen():
    global dis
    quitButton = Button((50,200, 200, 50), "Exit Game", 85, red, exitGame)
    startButton = Button((300, 200, 200, 50), "Start Game", 95, red, startGame)
    highscoreButton = Button((175, 275, 200, 50), "HighScores", 95, red, highscoreScreen)
    while gameRunning:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            quitButton.get_event(event)
            startButton.get_event(event)
            highscoreButton.get_event(event)
        dis.fill(white)
        showText("Snake Game!", black, 130, 70)
        highscoreButton.render(dis)
        quitButton.render(dis)
        startButton.render(dis)
        pygame.display.update()

def highscoreScreen():
    print("Highscores")
    backButton = Button((10, 10, 100, 50), "Back", 40, black, homeScreen)
    i = 0
    screenActive = True
    while screenActive:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            backButton.get_event(event)
        dis.fill(red)
        backButton.render(dis)
        highscoreTitleText = title_font.render("Highscores!", True, yellow)
        dis.blit(highscoreTitleText, [dis.get_width()/2 - 135, dis.get_height()/2 - 125, 160, 10])
        while i <= 4:
            highscore = score_font.render(str(gameLoop.highscoreList[i]), True, yellow)
            dis.blit(highscore, [dis.get_width()/2 - 20, dis.get_height()/2  - 50 + i*50, 160, 10])
            i += 1
            pygame.display.update()

    
    
    
class Button:
    def __init__(self, rect, text, leftShift, color, command):
        text = score_font.render(text, True, yellow)
        self.color = color
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(self.color)
        self.image.blit(text, [self.rect.size[0]/2 - leftShift, self.rect.size[1]/2 - 25])
        self.command = command
    def render(self, screen):
        screen.blit(self.image, self.rect)
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.command()