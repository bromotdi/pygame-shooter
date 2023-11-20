import sys
import pygame
from random import randint

pygame.init()

game_font = pygame.font.Font(None, 30)  # шрифт для игры размером 300

screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Awesome Shooter Game")
game_is_running = True
game_score = 0

'''FIGHTER'''
fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()  # возращаем кортеж с размерами
fighter_x = screen_width / 2 - fighter_width / 2
fighter_y = screen_height - fighter_height

# непрерывное перемещение корабля при нажатии клавише: нужно отслеживать когда клавиша была нажата и когда отпущена
fighter_is_moving_left, fighter_is_moving_right = False, False
FIGHTER_STEP = 0.3

'''ROCKET'''
rocket_image = pygame.image.load('images/rocket.png')
rocket_width, rocket_height = rocket_image.get_size()
rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2
rocket_y = fighter_y - rocket_height

# флаг указывает на то, находиться ли ракета в игре
rocket_was_fired = False
ROCKET_STEP = 0.3

'''ALIEN'''
alien_image = pygame.image.load('images/alien.png')
alien_width, alien_height = alien_image.get_size()
alien_x, alien_y = randint(0, screen_width - alien_width), alien_height

ALIEN_STEP = 0.05
alien_speed = ALIEN_STEP

while game_is_running:
    for event in pygame.event.get(): # обработка событий
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:  # key down = клавиша нажата -> движение начинается
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                rocket_was_fired = True
                rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2
                rocket_y = fighter_y - rocket_height

        if event.type == pygame.KEYUP:  # key up - клавиша отпущена -> движение прекращается
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    if rocket_was_fired and rocket_y + rocket_height < 0:
        rocket_was_fired = False
    if rocket_was_fired:
        rocket_y -= ROCKET_STEP

    alien_y += alien_speed
    if alien_y < rocket_y < alien_y + alien_height \
            and alien_x < rocket_x < alien_x + alien_width:
        rocket_was_fired = False
        alien_x, alien_y = randint(0, screen_width - alien_width), alien_height
        alien_speed += ALIEN_STEP / 2
        game_score += 1

    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))  # наложение ракеты на экран (поверхности на поверхность)
    screen.blit(alien_image, (alien_x, alien_y))

    if rocket_was_fired:
        screen.blit(rocket_image, (rocket_x, rocket_y))

    game_score_text = game_font.render(f"Your Score: {game_score}", True, 'white')
    screen.blit(game_score_text, (20, 20))
    pygame.display.update()

    if alien_y + alien_height > fighter_y:  # завершение игры если инопланетянин достиг корабля
        game_is_running = False

'''GAME OVER'''
game_over_text = game_font.render("Game Over", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width/2, screen_height/2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(1000)

pygame.quit()

