import pygame

pygame.init()

# 创建游戏窗口 480 * 700
screen = pygame.display.set_mode((480, 650))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")
# 2.blit 绘制图像
screen.blit(bg, (100, 100))
# 3.update 更新屏幕的显示
pygame.display.update()

while True:
    pass

pygame.quit()
