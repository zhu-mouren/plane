import pygame

# 游戏的初始化，窗口，初始位置，时钟
# 游戏循环，刷新率，与用户交互，图像的位置，屏幕更新显示

pygame.init()

# set_mode方法 会返回一个窗口
# set_mode  1.指定（宽， 长）
#           2.指定附加选项，如是否全屏，默认不需要
#           3.颜色的位数，（16位，32位，等等）默认自动匹配
# 创建游戏窗口
screen = pygame.display.set_mode((480, 852))


# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load('./images/background.png')

# 2.blit 绘制图像
screen.blit(bg, (100, 100))

# 3.update 更新屏幕显示
pygame.display.update()

# 绘制英雄飞机
hero = pygame.image.load('./images/hero1.png')
# 英雄飞机在画面上的位置
screen.blit(hero, (200, 500))
# 更新画面
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 设置变量查看循环的速度
# i = 0

# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 99, 124)
# 游戏循环，标志着游戏的正式开始！！！！
while True:
    clock.tick(1)

    # 1.修改飞机的位置
    hero_rect.y -= 50
    # att：绘制背景图案，解决残影问题
    screen.blit(bg,(0, 0))
    # 2.调用blit方法绘制图像
    screen.blit(hero, hero_rect)
    # 3.调用update方法更新显示
    pygame.display.update()

    # print(i)
    # i += 1
pygame.quit()
