# Импортируем библиотеку pygame
import pygame
from pygame import *
from player import Player
from blocks import Platform

#Объявляем переменные окна
WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота создаваемого окна
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400" # Цвет фона

#Объявляем переменные уровней
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окно
    pygame.display.set_caption("Super Pig")  # Шапка программы
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
                           # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # заливаем поверхность сплошным цветом

    hero = Player(55, 55)  # создаем героя по (x, y) координатам
    up, left, right = False, False, False  # по умолчанию — стоим

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    entities.add(hero)

    # объявляем уровень
    level = [
        "-------------------------",
        "-                       -",
        "-                       -",
        "-                       -",
        "-            --         -",
        "-                       -",
        "--                      -",
        "-                       -",
        "-                   --- -",
        "-                       -",
        "-                       -",
        "-      ---              -",
        "-                       -",
        "-   -----------         -",
        "-                       -",
        "-                -      -",
        "-                   --  -",
        "-                       -",
        "-                       -",
        "-------------------------"]

    timer = pygame.time.Clock()

    x, y = 0, 0  # координаты
    for row in level:  # каждая строка
        for col in row:  # каждый символ
            if col == "-":
                # создаем блок, заливаем его цветом и рисуем его
                '''pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))'''
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    while 1:  # основной цикл программы
        timer.tick(60)

        for e in pygame.event.get():  # обрабатываем события
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == QUIT:
                raise SystemExit("QUIT")

        screen.blit(bg, (0, 0))  # каждую итерацию необходимо всё перерисовывать

        hero.update(up, left, right, platforms)  # передвижение
        entities.draw(screen)  # отображение всего
        pygame.display.update()  # обновление и вывод всех изменений на экран



if __name__ == "__main__":
    main()