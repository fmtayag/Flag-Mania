## Import all needed libraries
import csv
import os
import pygame
import random
import re
from datetime import date

## Import local libraries
from constants import *
from class_label import Label
from class_image import Image

## The 'Game' class
class Game:

    ## 'Constructor' method
    def __init__(self):

        ## Screen declarations
        self.screen_width = 800
        self.screen_height = 600
        self.screen_size =  (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Flag Mania v2 by Etherflux")
        #pygame.display.set_icon(pygame.image.load(os.path.join("Resources", "Images", "Icon.png")))

        ## Clock, and FPS constant
        self.clock = pygame.time.Clock()
        self.FPS = 30

        ## 'game_state', accepts values: "start", "game", "gameover", and "highscores"
        self.game_state = "start"

        ## 'running' loop
        self.running = True

        ## Score, and date
        self.score = int()
        self.timer = float()
 
    ## 'Game loop' method, this is where most of the game actually happens
    def game_loop(self):

        while self.running:

            if self.game_state == "start":

                self.start_screen()

            elif self.game_state == "game":

                self.game_screen()

            elif self.game_state == "gameover":

                self.gameover_screen()

            elif self.game_state == "highscores":

                self.highscores_screen()

    ## 'Start' screen of the game
    def start_screen(self):

        ## 'loop' boolean
        loop = True

        ## Labels
        label_title = Label("Flag Mania (v2.0)", "NONSTOP", 32, WHITE, (20, 50))
        label_author = Label("by Etherflux", "NONSTOP", 24, WHITE, (20, 100))
        label_play = Label("Play", "NONSTOP", 28, WHITE, (550, 400))
        label_highscores = Label("High Scores", "NONSTOP", 28, WHITE, (550, 450))
        label_quit = Label("Quit", "NONSTOP", 28, WHITE, (550, 500))
        image_globe = Image("Globe", (50, 150))

        """ While loop """
        
        while loop == True:

            ## Locks the FPS
            self.clock.tick(self.FPS)

            ## Gets the mouse's position
            mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    loop = False
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if label_author.rendered_rect.collidepoint(mouse_position):

                        label_author.change_text("by Francis Tayag")

                    elif label_play.rendered_rect.collidepoint(mouse_position):

                        loop = False
                        self.game_state = "game"

                    elif label_highscores.rendered_rect.collidepoint(mouse_position):

                        loop = False
                        self.game_state = "highscores"

                    elif label_quit.rendered_rect.collidepoint(mouse_position):

                        loop = False
                        self.running = False

            ## Fills the screen with color
            self.screen.fill(PURE_BLACK)

            ## Runs 'depress' method of labels
            label_author.depress(mouse_position)
            label_play.depress(mouse_position)
            label_highscores.depress(mouse_position)
            label_quit.depress(mouse_position)

            ## Blits label, and image objects
            self.screen.blit(label_title.render(), label_title.position)
            self.screen.blit(label_author.render(), label_author.position)
            self.screen.blit(label_play.render(), label_play.position)
            self.screen.blit(label_highscores.render(), label_highscores.position)
            self.screen.blit(label_quit.render(), label_quit.position)
            self.screen.blit(image_globe.render(), image_globe.position)

            ## Updates, or 'flips' the display
            pygame.display.flip()

    ## 'Game' screen of the game
    def game_screen(self):

        ## 'Loop' boolean
        loop = True

        ## Gets the randomized flags list
        flags_list = self.load_flags()

        ## 'flag_rng' variable
        flag_rng = random.randint(0, len(flags_list) - 1)

        ## Sets timer to 60 seconds
        self.timer = 1 * self.FPS
        timer_start = False

        """ While loop """

        while loop:

            ## Labels, the slice index removes the .png file
            label_score = Label(f"Score: {self.score}", "NONSTOP", 32, WHITE, (20, 50))
            label_timer = Label(f"Time: {self.timer // self.FPS}", "NONSTOP", 32, WHITE, (600, 50))
            label_choice1 = Label(f"{flags_list[0][:-4]}", "NONSTOP", 24, WHITE, (70, 250))
            label_choice2 = Label(f"{flags_list[1][:-4]}", "NONSTOP", 24, WHITE, (70, 300))
            label_choice3 = Label(f"{flags_list[2][:-4]}", "NONSTOP", 24, WHITE, (70, 350))

            ## Flag image, the slice index removes the .png file (lazy solution I know lol)
            flag_path = os.path.join("Flags", flags_list[flag_rng][:-4])
            image_flag = Image(flag_path, [500, 265])

            ## Resizes the flag
            image_flag.resize((200, 100))

            ## Locks the FPS
            self.clock.tick(self.FPS)

            ## Starts timer if 'timer_start' is True
            if timer_start == True and self.timer >= 0:

                self.timer -= 1

            elif self.timer <= 0:

                self.game_state = "gameover"
                loop = False

            ## Gets the mouse's position
            mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    loop = False
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if label_choice1.text == flags_list[flag_rng][:-4] and label_choice1.rendered_rect.collidepoint(mouse_position):

                        self.score += 1
                        flags_list = self.load_flags()
                        flag_rng = random.randint(0, len(flags_list) - 1)
                        timer_start = True

                    elif label_choice2.text == flags_list[flag_rng][:-4] and label_choice2.rendered_rect.collidepoint(mouse_position):

                        self.score += 1
                        flags_list = self.load_flags()
                        flag_rng = random.randint(0, len(flags_list) - 1)
                        timer_start = True

                    elif label_choice3.text == flags_list[flag_rng][:-4] and label_choice3.rendered_rect.collidepoint(mouse_position):

                        self.score += 1
                        flags_list = self.load_flags()
                        flag_rng = random.randint(0, len(flags_list) - 1)
                        timer_start = True

                    elif label_choice1.text != flags_list[flag_rng][:-4] and label_choice1.rendered_rect.collidepoint(mouse_position):

                        self.score -= 1
                        flags_list = self.load_flags()
                        flag_rng = random.randint(0, len(flags_list) - 1)
                        timer_start = True

                    elif label_choice2.text != flags_list[flag_rng][:-4] and label_choice2.rendered_rect.collidepoint(mouse_position):

                        self.score -= 1
                        flags_list = self.load_flags()
                        flag_rng = random.randint(0, len(flags_list) - 1)
                        timer_start = True

                    elif label_choice3.text != flags_list[flag_rng][:-4] and label_choice3.rendered_rect.collidepoint(mouse_position):

                        self.score -= 1
                        flags_list = self.load_flags()
                        flag_rng = random.randint(0, len(flags_list) - 1)
                        timer_start = True

            ## Fills the screen with color
            self.screen.fill(PURE_BLACK)

            ## Runs 'depress' method of labels
            label_choice1.depress(mouse_position)
            label_choice2.depress(mouse_position)
            label_choice3.depress(mouse_position)

            ## Blits label, and image objects
            self.screen.blit(label_score.render(), label_score.position)
            self.screen.blit(label_timer.render(), label_timer.position)
            self.screen.blit(image_flag.render(), image_flag.position)
            self.screen.blit(label_choice1.render(), label_choice1.position)
            self.screen.blit(label_choice2.render(), label_choice2.position)
            self.screen.blit(label_choice3.render(), label_choice3.position)

            ## Updates, or 'flips' the display
            pygame.display.flip() 

    ## 'Game over' screen of the game
    def gameover_screen(self):

        ## Declarations for storing player name
        name_list = list()

        ## Labels
        label_gameover = Label("Game over!", "NONSTOP", 32, WHITE, [50, 100])
        label_totalscore = Label(f"You scored {self.score} under 60 seconds!", "NONSTOP", 32, WHITE, [50, 150])
        label_typename = Label(f"Type your name: {str().join(name_list)}", "NONSTOP", 32, WHITE, [50, 250])

        ## 'loop' boolean
        loop = True

        """ While loop """

        while loop == True:

            ## Ticks the clock, locks the FPS to <= 30
            self.clock.tick(self.FPS)

            ## Retrieves, and then stores the mouse's position
            mouse_position = pygame.mouse.get_pos()

            ## Loops through the 'event' sequence
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    loop = False
                    self.running = False

                elif event.type == pygame.KEYDOWN:

                    if re.match(r'^[A-Za-z0-9_]+$', chr(event.key)) and len(name_list) <= 16:

                        name_list.append(chr(event.key))

                    elif event.key == pygame.K_BACKSPACE and len(name_list) > 0:

                        name_list.pop()

                    elif event.key == pygame.K_RETURN:

                        with open(os.path.join("Resources", "High Scores", "highscores.txt"),
                            mode = "a", newline = "") as csv_file:

                            writer = csv.writer(csv_file, delimiter = "|")
                            writer.writerow([self.score, str().join(name_list), date.today().strftime("%b-%d-%Y")])

                        self.game_state = "start"
                        loop = False


            ## Updates the 'typename' label's text
            label_typename.text = f"Type your name: {str().join(name_list)}"

            ## Fills the background with black
            self.screen.fill(PURE_BLACK)

            ## Blits surfaces onto the screen surface
            self.screen.blit(label_gameover.render(), label_gameover.position)
            self.screen.blit(label_totalscore.render(), label_totalscore.position)
            self.screen.blit(label_typename.render(), label_typename.position)

            ## Updates, or "flips" the screen
            pygame.display.flip()

    ## 'High scores' screen of the game
    def highscores_screen(self):

        ## High scores list
        highscore_list = list()
        highscore_labels_list = list()
        y_offset = 0

        ## Labels
        label_header = Label("High Scores (Top 10)", "NONSTOP", 32, WHITE, [50, 100])
        label_nohighscores = Label("No high scores set, yet! Play the game!", "NONSTOP", 24, WHITE, [50, 150])
        label_goback = Label("Go Back", "NONSTOP", 24, WHITE, [600, 500])

        ## 'loop' boolean
        loop = True

        ## 'appended' boolean
        appended = False

        ## Special effect
        list_specialeffect = list()

        ## Opens the 'highscores.txt' file, and appends the contents into a list
        if os.stat(os.path.join("Resources", "High Scores", "highscores.txt")).st_size != 0:

            with open(os.path.join("Resources", "High Scores", "highscores.txt")) as csv_file:

                reader = csv.reader(csv_file, delimiter = "|")

                for row in reader:

                    highscore_list.append(row)

            ## Turns the 0th element in the current iteration of the highscore list into an integer
            for i in range(len(highscore_list)):

                highscore_list[i][0] = int(highscore_list[i][0])

            ## Sorts the highscore list in ascending order
            highscore_list.sort(reverse = True)

        """ While loop """

        while loop == True:

            ## Ticks the clock, locks the FPS to <= 30
            self.clock.tick(self.FPS)

            ## Retrieves, and then stores the mouse's position
            mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    loop = False
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if label_goback.rendered_rect.collidepoint(mouse_position):

                        self.game_state = "start"
                        loop = False

            ## Runs the 'depress' method
            label_goback.depress(mouse_position)

            ## Fills the background with black
            self.screen.fill(PURE_BLACK)

            ## Checks if 'highscores.txt' file's length is 0 (zero)
            if os.stat(os.path.join("Resources", "High Scores", "highscores.txt")).st_size == 0:

                self.screen.blit(label_nohighscores.render(), label_nohighscores.position)

            if appended == False:

                for highscore in highscore_list:

                    label_highscore = Label(f"{highscore[0]} | {highscore[1]} | {highscore[2]}", 
                        "NONSTOP", 24, WHITE, [50, 150 + y_offset])
                    highscore_labels_list.append(label_highscore)

                    y_offset += 30

                appended = True

            ## Checks if the length of the high scores list is less than 10, then blits the high score list
            if len(highscore_labels_list) <= 10:

                for label in highscore_labels_list:

                    self.screen.blit(label.render(), label.position)

            ## Blits only the top 10 high scores if list is above 20
            elif len(highscore_labels_list) > 10:

                for i in range(10):

                    self.screen.blit(highscore_labels_list[i].render(), highscore_labels_list[i].position)

            ## Blits surfaces onto the screen surface
            self.screen.blit(label_header.render(), label_header.position)
            self.screen.blit(label_goback.render(), label_goback.position)

            ## Updates, or "flips" the screen
            pygame.display.flip()

    ## Loads, and randomizes the flags 
    def load_flags(self):

        ## Reads all the flags in the directory
        path = os.path.join("Resources", "Images", "Flags")
        flags_list = os.listdir(path)

        ## Shuffles the flags list
        random.shuffle(flags_list)

        ## Returns first three flags from the list
        return flags_list[:3]

