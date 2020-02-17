# set_mode方法 会返回一个窗口
import pygame
pygame.init()

# 创建游戏窗口
# set_mode  1.指定（宽， 长）
#           2.指定附加选项，如是否全屏，默认不需要
#           3.颜色的位数，（16位，32位，等等）默认自动匹配

screen = pygame.display.set_mode()

while True:
    pass

pygame.quit()