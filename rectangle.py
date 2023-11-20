import sys
# from random import randint  # генерация рандомного числа в диапазоне
import pygame

clock = pygame.time.Clock()  # экземпляр класса времены
pygame.init()  # инициализация новой игры

screen_width, screen_height = 800, 600
rect_width, rect_height = 100, 200
rect_x, rect_y = screen_width/2 - rect_width/2, screen_height/2 - rect_height/2
STEP = 10

screen = pygame.display.set_mode((screen_width, screen_height))  # рисуем рабочее пространство для игры
pygame.display.set_caption("My Pygame")  # даем название игре

while True:  # работать пока пользователь не закроет окно
    for event in pygame.event.get():  # получение события
        print(event)
        if event.type == pygame.QUIT:  # если событие типа Quit -> выходим из игры
            sys.exit()
        # двигаем прямоугольник
        if event.type == pygame.KEYDOWN:  # проверка нажата ли какая-то клавиша на экране
            if event.key == pygame.K_UP and rect_y >= STEP:  # если клавиша вверх нажата и координата у >= шага
                rect_y -= STEP
            if event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:
                rect_y += STEP
            if event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP
            if event.key == pygame.K_RIGHT and rect_x <= screen_width - rect_width - STEP:
                rect_x += STEP
    # screen.fill((255,0,0))  # изменения фона игры
    screen.fill(pygame.Color('yellow'))

    #screen.fill((randint(0,255), randint(0,255), randint(0,255)))
    pygame.draw.rect(screen, (0,255,0), (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()  # применяем изменения в игре

    # влияем на скорость выполнения того, что в цикле
    # clock.tick(1)  # 5 обновлений экрана за 1 секунду