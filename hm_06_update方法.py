import pygame

pygame.init()

# 创建游戏窗口 480 * 700
screen = pygame.display.set_mode((480, 650))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (100, 400))

# 可以在所有绘制工作完成之后，同意调用update方法
pygame.display.update()

while True:
    pass

pygame.quit()
