import sys, pygame
pygame.init()

size = width, height = 520, 540
speed = [2, 2]
black = 0, 0, 0
circlepos = [width/2, height/2]
screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
            ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        if pygame.key.get_pressed()[pygame.K_LEFT]==True:
            circlepos[0] -=30
        print(pygame.key.get_pressed()[pygame.K_RIGHT]==True)
        print(pygame.key.get_pressed()[pygame.K_UP]==True)
        print(pygame.key.get_pressed()[pygame.K_DOWN]==True)
        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.draw.circle(screen, (250, 40, 50),circlepos, 10)
        pygame.display.flip()
                                                                    
