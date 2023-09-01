class menu_opt():

    def __init__(self, str, x, y, on_click, transport):

        self.text = str
        
        self.x = x
        self.y = y

        self.over = False
        self.og_over = False

        self.width = 20 * len(str)
        self.height = 20

        self.on_click = on_click

        self.transport = transport

    def render_text(self, str, pos, color, center=False):
        font = self.transport.pygame.font.Font('assets/default_font.ttf')
        text = font.render(str, 1, self.transport.pygame.Color(color))
        if center:
            text_width = text.get_width()
            text_height = text.get_height()

            pos = (self.transport.self.transport.display.x / 2 - text_width / 2, self.transport.display.y / 2 - text_height / 2)
        self.transport.window.blit(text,pos)

    def exist(self):
        mx, my = self.transport.pygame.mouse.get_pos()
        color = 'black'

        if mx >= self.x and mx <= self.x + self.width:
            if my >= self.y and my <= self.y + self.height:
                color = 'blue'

                for event in self.transport.pygame.event.get():
                    if event.type == self.transport.pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.on_click()

        self.render_text(self.text, (self.x, self.y), color)