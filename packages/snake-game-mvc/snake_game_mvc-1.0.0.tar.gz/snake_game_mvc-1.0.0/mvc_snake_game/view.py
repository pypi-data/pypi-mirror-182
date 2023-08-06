import pygame
from mvc_snake_game.model import Snake
from mvc_snake_game.controller import Input
from mvc_snake_game.path_getter import *


NUM_GRID = 20
SPACE = 100

WIN_LENGTH = 700

WHITE = (255, 255, 255)
STATIC_BOX = (120, 120, 120)
HIGHLIGHTED_BOX = (184, 184, 184)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (143, 188, 143)
HEAD_COLOUR = (120, 120, 120)
SEGMENT_COLOUR = (200, 200, 200)

def save_score(name, score):
    with open(get_path_to_file_from_root('mvc_snake_game/High_Scores.txt'), 'a') as scores:
        scores.write(str(name) + ' : ' + str(score) + '\n')


def highest(scores, names):
    try:
        x = scores[0]
        name = names[0]
    except Exception:
        x = ''
        name = ''
    index = 0
    for i, score in enumerate(scores):
        if int(score) > int(x):
            x = score
            name = names[i]
            index = i

    return x, name, index


def high_scores():
    names = []
    scoress = []
    high_scores = []
    with open(get_path_to_file_from_root('mvc_snake_game/High_Scores.txt'), 'r') as scores:
        lines = scores.readlines()

        for line in lines:
            x = line.split(" : ")
            name = x[0]
            score = x[1].strip()
            names.append(name)
            scoress.append(score)
        i = 0
        x = len(names)
        while i < x:
            score, name, index = highest(scoress, names)
            del scoress[index]
            del names[index]

            combined = str(name) + ' : ' + str(score)
            high_scores.append(combined)
            i += 1

    return high_scores


class Window:

    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        self.grid_width = (WIN_LENGTH - (2 * SPACE)) / NUM_GRID
        self.score_font = pygame.font.SysFont("arial", 40)
        self.title_font = pygame.font.SysFont("arial", 70)
        self.button_font = pygame.font.SysFont("arial", 120)
        self.window = pygame.display.set_mode((WIN_LENGTH, WIN_LENGTH))
        self.img = pygame.image.load(get_path_to_file_from_root('mvc_snake_game/assets/bg.jpg')).convert()
        pygame.display.set_caption("MVC-Snake")

        self.writing = False
        self.snake = Snake(NUM_GRID)
        self.input = Input(self.snake)
        self.name = ""
        self.submit = False
        self.menu = True
        self.gameover = False
        self.select_diff = False

    def draw_grid(self):
        i = 0
        j = 0
        x = SPACE
        y = SPACE
        grid_length = self.grid_width * NUM_GRID

        while j <= NUM_GRID:
            pygame.draw.line(self.window, WHITE, (x, y), (x + grid_length, y))
            y += self.grid_width
            j += 1
        y = SPACE
        
        while i <= NUM_GRID:
            pygame.draw.line(self.window, WHITE, (x, y), (x, y + grid_length))
            x += self.grid_width
            i += 1

    def coor_to_rect(self, x, y):
        x += (SPACE + 1 + ((self.grid_width - 1) * x))
        y += (SPACE + 1 + ((self.grid_width - 1) * y))
        return x, y

    def draw_snake(self, snake):
        x, y = self.coor_to_rect(snake.x, snake.y)
        fruitx, fruity = self.coor_to_rect(snake.fruit.x, snake.fruit.y)
        for segment in snake.tail:
            segx, segy = self.coor_to_rect(segment[0], segment[1])
            pygame.draw.rect(self.window, SEGMENT_COLOUR, (segx, segy, self.grid_width - 1, self.grid_width - 1))
        if x < WIN_LENGTH - SPACE and y < WIN_LENGTH - SPACE and x > 0 + SPACE and y > 0 + SPACE:#голова
            pygame.draw.rect(self.window, HEAD_COLOUR, (x, y, self.grid_width - 1, self.grid_width - 1))
        pygame.draw.rect(self.window, GREEN, (fruitx, fruity, self.grid_width - 1, self.grid_width - 1))

    def update(self):
        text = self.score_font.render("Score: " + str(self.snake.score), 1, WHITE)

        self.window.blit(self.img, (0, 0))
        #self.window.fill(BLACK)
        self.draw_grid()
        self.input.key_press()
        self.draw_snake(self.snake)
        self.window.blit(text, (0, 10))
        self.gameover = self.snake.update()

    def high_score_menu(self):
        self.window.fill(BLACK)
        x, y = pygame.mouse.get_pos()
        scores_text = self.title_font.render("High Scores:", 1, WHITE)
        self.window.blit(scores_text, (WIN_LENGTH / 2 - scores_text.get_width() / 2, 10))
        high_scores_str = high_scores()[0:5]
        i = 80
        for score in high_scores_str:
            score_text = self.score_font.render(score, 1, WHITE)
            self.window.blit(score_text, (WIN_LENGTH / 2 - score_text.get_width() / 2, i))
            i += 50

        pygame.draw.rect(self.window, WHITE, (WIN_LENGTH / 2 - 220, WIN_LENGTH / 2 + 200, 300, 50))
        pygame.draw.rect(self.window, STATIC_BOX, (WIN_LENGTH / 4 - 45, WIN_LENGTH / 2 + 100, 180, 50))
        pygame.draw.rect(self.window, STATIC_BOX, (WIN_LENGTH / 4 + 200, WIN_LENGTH / 2 + 100, 180, 50))
        pygame.draw.rect(self.window, STATIC_BOX, (WIN_LENGTH / 2 + 80, WIN_LENGTH / 2 + 200, 125, 50))
        pygame.draw.rect(self.window, STATIC_BOX, (WIN_LENGTH / 4 - 45, WIN_LENGTH - 75, 425, 50))
        
        if x > WIN_LENGTH / 4 - 45 and x < WIN_LENGTH / 2 + 380 and y > WIN_LENGTH - 75 and y < WIN_LENGTH - 25:
            pygame.draw.rect(self.window, HIGHLIGHTED_BOX, (WIN_LENGTH / 4 - 45, WIN_LENGTH - 75, 425, 50))
            if pygame.mouse.get_pressed()[0]:
                self.menu = True

        elif x > WIN_LENGTH / 2 - 220 and x < WIN_LENGTH / 2 + 70 and y > WIN_LENGTH / 2 + 200 and y < WIN_LENGTH / 2 + 250:
            pygame.draw.rect(self.window, HIGHLIGHTED_BOX, (WIN_LENGTH / 2 - 220, WIN_LENGTH / 2 + 200, 300, 50))
            if pygame.mouse.get_pressed()[0]:
                self.writing = True

        elif x > WIN_LENGTH / 2 + 80 and x < WIN_LENGTH / 2 + 205 and y > WIN_LENGTH / 2 + 200 and y < WIN_LENGTH / 2 + 250:
            pygame.draw.rect(self.window, HIGHLIGHTED_BOX, (WIN_LENGTH / 2 + 80, WIN_LENGTH / 2 + 200, 125, 50))
            if pygame.mouse.get_pressed()[0] and not self.submit:
                save_score(self.name, self.snake.score)
                self.snake.dead()
                self.name = ""
                self.submit = True

        elif x > WIN_LENGTH / 4 - 45 and x < WIN_LENGTH / 4 + 135 and y > WIN_LENGTH / 2 + 100 and y < WIN_LENGTH / 2 + 150:
            pygame.draw.rect(self.window, HIGHLIGHTED_BOX, (WIN_LENGTH / 4 - 45, WIN_LENGTH / 2 + 100, 180, 50))
            if pygame.mouse.get_pressed()[0]:
                self.gameover = False
                self.snake.dead()
                self.snake.x = NUM_GRID / 2
                self.snake.y = NUM_GRID / 2
                self.snake.direction = (1, 0)

        elif x > WIN_LENGTH / 4 + 200 and x < WIN_LENGTH / 4 + 380 and y > WIN_LENGTH / 2 + 100 and y < WIN_LENGTH / 2 + 150:
            pygame.draw.rect(self.window, HIGHLIGHTED_BOX, (WIN_LENGTH / 4 + 200, WIN_LENGTH / 2 + 100, 180, 50))
            if pygame.mouse.get_pressed()[0]:
                quit()
                
        if self.writing:
            pygame.draw.rect(self.window, HIGHLIGHTED_BOX, (WIN_LENGTH / 2 - 220, WIN_LENGTH / 2 + 200, 300, 50))
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():
                        if len(self.name) < 12:
                            self.name += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:len(self.name) - 1]
                    elif event.key == pygame.K_RETURN:
                        save_score(self.name, self.snake.score)

            name = self.score_font.render(self.name, 1, WHITE)
            self.window.blit(name, (WIN_LENGTH / 2 - 200, WIN_LENGTH / 2 + 210, 300, 50))
        
        text1 = self.score_font.render("Play Again", 1, WHITE)
        self.window.blit(text1, (WIN_LENGTH / 4 - 35, WIN_LENGTH / 2 + 100))
        text2 = self.score_font.render("Quit", 1, WHITE)
        self.window.blit(text2, (WIN_LENGTH / 4 + 255, WIN_LENGTH / 2 + 100))
        text3 = self.score_font.render("Submit", 1, WHITE)
        self.window.blit(text3, (WIN_LENGTH / 2 + 90, WIN_LENGTH / 2 + 200))
        text4 = self.score_font.render("Back to menu", 1, WHITE)
        self.window.blit(text4, (WIN_LENGTH / 4 + 65, WIN_LENGTH - 75))

    def main_menu(self):
        self.window.fill(BLACK)
        x, y = pygame.mouse.get_pos()

        pygame.draw.rect(self.window, STATIC_BOX, (WIN_LENGTH / 2 - 90, WIN_LENGTH / 2 - 75, 180, 50))
        pygame.draw.rect(self.window, STATIC_BOX, (WIN_LENGTH / 2 - 90, WIN_LENGTH / 2 + 25, 180, 50))

        if x > WIN_LENGTH / 2 -90 and x < WIN_LENGTH / 2 + 90 and y > WIN_LENGTH / 2 - 75 and y < WIN_LENGTH / 2 - 25:
            pygame.draw.rect(self.window, HIGHLIGHTED_BOX, (WIN_LENGTH / 2 - 90, WIN_LENGTH / 2 - 75, 180, 50))
            if pygame.mouse.get_pressed()[0]:
                self.snake.dead()
                self.snake.x = NUM_GRID / 2
                self.snake.y = NUM_GRID / 2
                self.snake.direction = (1, 0)
                self.gameover = False
                self.menu = False
                self.select_diff = True

        elif x > WIN_LENGTH / 2 -90 and x < WIN_LENGTH / 2 + 90 and y > WIN_LENGTH / 2 + 25 and y < WIN_LENGTH / 2 + 75:
            pygame.draw.rect(self.window, HIGHLIGHTED_BOX, (WIN_LENGTH / 2 - 90, WIN_LENGTH / 2 + 25, 180, 50))
            if pygame.mouse.get_pressed()[0]:
                quit()
        
        text1 = self.score_font.render("Play", 1, WHITE)
        self.window.blit(text1, (WIN_LENGTH / 2 - 30, WIN_LENGTH / 2 - 75))
        text2 = self.score_font.render("Exit", 1, WHITE)
        self.window.blit(text2, (WIN_LENGTH / 2 - 30, WIN_LENGTH / 2 + 25))

    def select_difficult(self, game):
        self.window.fill(BLACK)
        x, y = pygame.mouse.get_pos()

        pygame.draw.rect(self.window, STATIC_BOX, (WIN_LENGTH / 2 - 90, WIN_LENGTH / 2 - 125, 180, 50))
        pygame.draw.rect(self.window, STATIC_BOX, (WIN_LENGTH / 2 - 90, WIN_LENGTH / 2 - 25, 180, 50))
        pygame.draw.rect(self.window, STATIC_BOX, (WIN_LENGTH / 2 - 90, WIN_LENGTH / 2 + 75, 180, 50))

        if x > WIN_LENGTH / 2 -90 and x < WIN_LENGTH / 2 + 90 and y > WIN_LENGTH / 2 - 125 and y < WIN_LENGTH / 2 - 75:
            pygame.draw.rect(self.window, HIGHLIGHTED_BOX, (WIN_LENGTH / 2 - 90, WIN_LENGTH / 2 - 125, 180, 50))
            if pygame.mouse.get_pressed()[0]:
                #print('Easy')
                game.fps = 60
                self.select_diff = False
        
        elif x > WIN_LENGTH / 2 -90 and x < WIN_LENGTH / 2 + 90 and y > WIN_LENGTH / 2 - 25 and y < WIN_LENGTH / 2 + 25:
            pygame.draw.rect(self.window, HIGHLIGHTED_BOX, (WIN_LENGTH / 2 - 90, WIN_LENGTH / 2 - 25, 180, 50))
            if pygame.mouse.get_pressed()[0]:
                #print('Normal')
                game.fps = 120
                self.select_diff = False

        elif x > WIN_LENGTH / 2 -90 and x < WIN_LENGTH / 2 + 90 and y > WIN_LENGTH / 2 + 75 and y < WIN_LENGTH / 2 + 125:
            pygame.draw.rect(self.window, HIGHLIGHTED_BOX, (WIN_LENGTH / 2 - 90, WIN_LENGTH / 2 + 75, 180, 50))
            if pygame.mouse.get_pressed()[0]:
                #print('Hard')
                game.fps = 200
                self.select_diff = False

        text1 = self.score_font.render("Easy", 1, WHITE)
        self.window.blit(text1, (WIN_LENGTH / 2 - 35, WIN_LENGTH / 2 - 125))
        text2 = self.score_font.render("Normal", 1, WHITE)
        self.window.blit(text2, (WIN_LENGTH / 2 - 50, WIN_LENGTH / 2 - 25))
        text3 = self.score_font.render("Hard", 1, WHITE)
        self.window.blit(text3, (WIN_LENGTH / 2 - 35, WIN_LENGTH / 2 + 75))