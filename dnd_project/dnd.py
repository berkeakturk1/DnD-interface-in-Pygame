import pygame
import random
import sys

pygame.init()

clock = pygame.time.Clock()

def sizeImg(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)




myfont = pygame.font.SysFont("monospace", 40)
BLACK  = 0,0,0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
RED = 255, 0, 0
GREY = 128, 128, 128
BG = pygame.image.load("C:\\Users\\Berke\\IdeaProjects\\dnd\\bg.png")
BG = sizeImg(BG, 1.5)
width = BG.get_width()
height = BG.get_height()
dis = pygame.display.set_mode((width, height))
num = myfont.render('0', 1, BLACK)
run = True


def diceUI():
    d4 = pygame.draw.rect(dis, WHITE, [10, 10, 50, 40])
    d6 = pygame.draw.rect(dis, WHITE, [90, 10, 70, 40])
    d8 = pygame.draw.rect(dis, WHITE, [180, 10, 70, 40])
    d10 = pygame.draw.rect(dis, WHITE, [280, 10, 70, 40])
    d12 = pygame.draw.rect(dis, WHITE, [370, 10, 70, 40])
    d20 = pygame.draw.rect(dis, WHITE, [460, 10, 70, 40])
    currentVal = pygame.draw.rect(dis, WHITE, [550, 10, 400, 40])
    d4text = myfont.render(str("D4"), 1, (0,0,0))
    d6text = myfont.render(str("D6"), 1, (0,0,0))
    d8text = myfont.render(str("D8"), 1, (0,0,0))
    d10text = myfont.render(str("D10"), 1, (0,0,0))
    d12text = myfont.render(str("D12"), 1, (0,0,0))
    d20text = myfont.render(str("D20"), 1, (0,0,0))
    cVal = myfont.render(str("Current Value:"), 1, (0,0,0))
    textlist = [d4text, d6text, d8text, d10text, d12text, d20text, cVal]
    x, y = 10, 10
    for i in textlist:
        dis.blit(i, (x, 10))
        x += 90
    num = 0
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if d4.collidepoint(pos):
                num = random.randint(1, 4)
            if d6.collidepoint(pos):
                num = random.randint(1, 6)
            if d8.collidepoint(pos):
                num = random.randint(1, 8)
            if d10.collidepoint(pos):
                num = random.randint(1, 10)
            if d12.collidepoint(pos):
                num = random.randint(1, 12)
            if d20.collidepoint(pos):
                num = random.randint(1, 20)
    if num == 0:
        return myfont.render("0", 1, BLACK)

    return myfont.render(str(num), 1, BLACK)


while run:
    clock.tick(60)

    dis.blit(BG, (0, 0))
    num = diceUI()

    dis.blit(num, (900, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break


    pygame.display.update()
pygame.quit()