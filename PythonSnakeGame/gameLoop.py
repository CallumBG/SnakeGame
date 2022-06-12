import random
import pygame

pygame.init()

white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)

currentScore = 0

#Sets the standard refresh rate of the window
FPS = 60

clock = pygame.time.Clock()

highscoreList = [0, 0, 0, 0, 0]

score_font = pygame.font.SysFont("comicsansms", 35)

def startGameLoop(dis):
    print("Game Loop Started!")

    game_over = False

    snake_block = 10
    snake_speed = 10

    #current snake coord
    x1 = dis.get_width()/2
    y1 = dis.get_height()/2

    yChange = 0
    xChange = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis.get_width() - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(50, dis.get_height() - snake_block) / 10.0) * 10.0

    #checks if the game is over, if not the game tracks any event that occurs
    while not game_over:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -snake_block
                    yChange = 0
                elif event.key == pygame.K_RIGHT:
                    xChange = snake_block
                    yChange = 0
                elif event.key == pygame.K_DOWN:
                    yChange = snake_block
                    xChange = 0
                elif event.key == pygame.K_UP:
                    yChange = -snake_block
                    xChange = 0
                if event.key == pygame.K_ESCAPE:
                    pauseMenu(dis)


        if x1 >= dis.get_width() or x1 < 0 or y1 >= dis.get_height() or y1 < 50:
            game_over = True
        x1 = x1 + xChange
        y1 = y1 + yChange
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True
        draw_snake(snake_block, snake_List, dis)
        pygame.draw.rect(dis, red, [0,0,dis.get_width(), 50])
        text = score_font.render("Highscore: " + str(highscoreList[0]), True, yellow)
        dis.blit(text, [300, 0, 160, 10])
        show_score(Length_of_snake - 1, dis)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis.get_width() - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(50, dis.get_height() - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)
        global currentScore
        currentScore = Length_of_snake - 1
        
    updateHighscores(Length_of_snake-1)

def draw_snake(snake_block, snake_list, dis):
    i = 0
    for x in snake_list:
        if i == len(snake_list) - 1:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

            i += 1
        else:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
            i += 1

def show_score(score, dis):
    score_font = pygame.font.SysFont("comicsansms", 35)
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [10,0])

def updateHighscores(score):
    global highscoreList
    i = 0
    while  i <= 4:
        if highscoreList[i] < score:
            j = 4
            while j >= i:
                if j == i:
                    highscoreList[j] = score
                    break
                else:
                    highscoreList[j] = highscoreList[j - 1]
                j -= 1
            break
        else:
            i += 1
        
def pauseMenu(dis):
    print("Paused")
    gamePaused = True
    title_font = pygame.font.SysFont("bahnschrift", 50)
    value = title_font.render("Game Paused" , True, yellow)
    while gamePaused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamePaused = False
        dis.blit(value, [dis.get_width()/2 - 150,100])
        pygame.display.update()
    