from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_path, x, y, size_x=50, size_y=50, speed=4):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, image_path, x, y, size_x= 50, size_y=150, speed=4, left=True):
        super().__init__(image_path, x, y, size_x, size_y, speed)
        self.left = left

    def move(self):
        if self.left:
            self.update_l()
        else:
            self.update_r()

    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_length - self.rect.height - 5:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_length - self.rect.height - 5:
            self.rect.y += self.speed


win_width = 858
win_length = 525
window = display.set_mode((win_width, win_length))
display.set_caption("Ping-Pong")

ball_speed_x = 3
ball_speed_y = 3
FPS = 60
game = True
finish = False
clock = time.Clock()

left_paddle = Player("paddle.png", 30, 200, 10, 150, 4, True)
right_paddle = Player("paddle.png", 780, 200, 10, 150, 4, False)
ball = GameSprite("ball.png", 400, 250, 50, 50, 0)

font.init()
style = font.SysFont(None, 40)
lose1= style.render("PLAYER 1 LOSES!", True, (180, 0, 0))
lose2= style.render("PLAYER 2 LOSES!", True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill((0, 0, 0))
        left_paddle.move()
        right_paddle.move()

        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if sprite.collide_rect(left_paddle, ball) or sprite.collide_rect(right_paddle, ball):
            ball_speed_x *= -1.01

        if ball.rect.y > win_length - ball.rect.height or ball.rect.y < 0:
            ball_speed_y *= -1.0001

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (294, 262))
        if ball.rect.x > win_width - ball.rect.width:
            finish = True
            window.blit(lose2, (294, 262))


        left_paddle.reset()
        right_paddle.reset()
        ball.reset()

        display.update()
        clock.tick(FPS)
        display.update()

        clock.tick(FPS)
