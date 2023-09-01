class obamna_():

    def __init__(self, transport):
        self.transport = transport

        self.obamna_img = self.transport.pygame.image.load('assets/obamna.jpg')

    def exist(self):
        obamna_new = self.transport.pygame.transform.scale(self.obamna_img, (self.transport.display.x, self.transport.display.y))
        obamna_new.set_alpha(255 / 4)

        self.transport.window.blit(obamna_new, (0,0))