import random

class bg():
    def __init__(self, transport):
        self.top_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.bot_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.og_top_color = self.top_color
        self.og_bot_color = self.bot_color

        self.t_top_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.t_bot_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.current_frame = 0
        self.target_frame = 120

        self.current_color = self.top_color

        self.transport = transport

    def lerp(self, start, end, t):
        return int(start + (end - start) * t)
    
    def lerp_color(self, start_color, end_color, t):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * t)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * t)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * t)
        return (r,g,b)

    def exist(self):

        if self.current_frame >= 121:
            self.current_frame = 0

            self.og_top_color = self.top_color
            self.og_bot_color = self.bot_color


            self.t_top_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.t_bot_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        t = round(self.current_frame / self.target_frame, 2)

        self.top_color = self.lerp_color(self.og_top_color, self.t_top_color, t)
        self.bot_color = self.lerp_color(self.og_bot_color, self.t_bot_color, t)

        # this code is very unoptimized and fucks
        # the framerate when in fullscreen mode,
        # may fix later but unlikely
        for row in range(self.transport.display.y + 1):
            t = row / self.transport.display.y
            
            self.current_color = self.lerp_color(self.top_color, self.bot_color, t)

            self.transport.pygame.draw.line(self.transport.window, self.current_color, (0, row - 1), (self.transport.display.x, row - 1), 1)

        self.current_frame += 1