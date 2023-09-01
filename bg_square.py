import random

aaron = False

class bg_square():
    def __init__(self, transport):

        self.transport = transport

        self.size = random.randint(25, 75)

        self.width = self.size
        self.height = self.size

        self.x = random.randint(0, self.transport.display.x)
        self.y = random.randint(0 - self.size, self.transport.display.y)

        self.line_width = 5

        self.og_speed = random.randint(1, 2)
        self.speed = self.og_speed
        self.rot_speed = random.randint(3, 4)

        self.rot = random.randint(0, 360)
        self.alpha = random.randint(0, 255)

        if aaron:
            aaron_img = self.transport.aaron_img

        self.surface = self.transport.pygame.Surface((self.width, self.height), self.transport.pygame.SRCALPHA)
        self.transport.pygame.draw.rect(self.surface, (255, 255, 255, self.alpha), (0, 0, self.width, self.height), self.line_width)

        if aaron:
            aaron_tranformed = self.transport.pygame.transform.scale(aaron_img, (self.size, self.size))
            aaron_tranformed.set_alpha(self.alpha)
            self.surface.blit(aaron_tranformed, (0,0))

    def exist(self):
        if self.x + self.width <= 0:
            self.reset()

        self.speed = self.og_speed * self.transport.pygame.mixer.music.get_volume()

        self.x -= self.speed
        self.rot = (self.rot + self.rot_speed * 2) % 360

        rotated_surface = self.transport.pygame.transform.rotate(self.surface, self.rot)

        self.transport.window.blit(rotated_surface, (self.x - int(rotated_surface.get_width() / 2), self.y - int(rotated_surface.get_height() / 2)))

    def reset(self):
        self.x = self.transport.display.x + self.width
        self.y = random.randint(0, self.transport.display.y)