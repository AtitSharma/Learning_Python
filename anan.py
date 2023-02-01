# def a(func):
#     print("I am a")
#     def b():
#         print("I am b")
#         func()
#     print("I am done")
#     # b()
# @a
# def show():
#     pass
# show()


import pygame , sys
pygame.init()
screen=pygame.display.set_mode((400,500))
clock=pygame.time.Clock()
while True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
