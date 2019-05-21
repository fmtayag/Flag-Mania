import pygame
import random
import os
pygame.init()

class Flag:
    def __init__(self, name):
        self.name = name
        self.image = pygame.image.load(os.path.join("flags", f"{self.name}.png"))
        self.image = pygame.transform.scale(self.image, (200, 100))
        self.image_rect = self.image.get_rect()
        self.image_rect.x = (screen_width / 2) - 100
        self.image_rect.y = 25

class Text:
    def __init__(self, text, font, size, pos_y):
        self.text = text
        self.font = pygame.font.Font(os.path.join("fonts", f"{font}"), size)
        self.label = self.font.render(text, False, WHITE)
        self.label_rect = self.label.get_rect()
        self.label_rect.x = (screen_width / 2) - 150
        self.label_rect.y = pos_y

button = pygame.Rect(100, 100, 50, 50)

WHITE = (255, 255, 255)
BLACK = (25, 25, 25)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

score = 0
question_number = 1
### INPUT MAXIMUM NUMBER OF QUESTIONS HERE >>>>>>>>>>
max_questions = 30

FPS = 60
clock = pygame.time.Clock()

os.chdir("flags")
flags = os.listdir()
print(flags)
flags = [f.replace(".png", "") for f in flags]
os.chdir("..")

screen_width, screen_height = 400, 500
screen_resolution = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_resolution)
pygame.display.set_caption("Vexill.io")

def game_loop():
    global score
    global question_number
    random.shuffle(flags)
    random.shuffle(flags)

    choices = list()
    choice_labels = list()
    correct = list()

    for i in range(3):
        flag = Flag(flags[i])
        choices.append(flag)

    rng = random.randint(0, len(choices) - 1)
    
    running = True
    
    while running == True:
        clock.tick(FPS)
        mouse_pressed = False
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True

        choice_label1 = Text(choices[0].name, "Pixelart.ttf", 22, 150)
        choice_label2 = Text(choices[1].name, "Pixelart.ttf", 22, 200)
        choice_label3 = Text(choices[2].name, "Pixelart.ttf", 22, 250)
        score_label = Text(f"Score {score}", "Pixelart.ttf", 16, 300)
        number_label = Text(f"Question {question_number} out of {max_questions}", "Pixelart.ttf", 16, 325)
        #correct_label = Text(f"Answer is {choices[rng].name}", "Pixelart.ttf", 16, 350)
        gameover_label = Text("Game Over!", "Pixelart.ttf", 32, screen_height - 30)
        
        choices_list = (choice_label1, choice_label2, choice_label3)

        for i in range(3):
            if mouse_pressed == True and choices_list[i].label_rect.collidepoint(mouse_pos) and choices_list[i].text == choices[rng].name:
                score += 1
                question_number += 1
                game_loop()
            elif mouse_pressed == True and choices_list[i].label_rect.collidepoint(mouse_pos) and choices_list[i].text != choices[rng].name:
                if score == 0:
                    question_number += 1
                    game_loop()
                elif score > 0:
                    score -= 1
                    question_number += 1
                    game_loop()
 
        if question_number > max_questions:
            screen.blit(gameover_label.label, gameover_label.label_rect)
            pygame.display.update()
            exit()
        
        screen.fill(BLACK)
        screen.blit(choices[rng].image, choices[rng].image_rect)
        screen.blit(choice_label1.label, choice_label1.label_rect)
        screen.blit(choice_label2.label, choice_label2.label_rect)
        screen.blit(choice_label3.label, choice_label3.label_rect)
        screen.blit(score_label.label, score_label.label_rect)
        screen.blit(number_label.label, number_label.label_rect)
        
        pygame.display.update()
game_loop()
exit()
