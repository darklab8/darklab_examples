
import pygame
import sys
import random
from dataclasses import dataclass

@dataclass
class ScreenResolution:
    width = 1080
    height = 720

    @property
    def as_tuple(self):
        return (self.width, self.height)

@dataclass
class Position:
    x: int
    y: int

    @property
    def as_tuple(self):
        return (self.x, self.y)

@dataclass
class Color:
    red: int
    green: int
    blue: int

    @property
    def as_tuple(self):
        return (self.red, self.green, self.blue)

    @classmethod
    def create_black(cls):
        return cls(0, 0, 0)

    @classmethod
    def create_red(cls):
        return cls(0, 0, 0)

class GameWindow:
    def __init__(self, resolution: ScreenResolution):
        pygame.init()
        self._screen = pygame.display.set_mode(resolution.as_tuple)
        self._font = pygame.font.Font("freesansbold.ttf", 32)

        self._fps = 60
        self._clock = pygame.time.Clock()

    def draw_circle(self, color: Color, center: Position, radius: int):
        pygame.draw.circle(self._screen, color.as_tuple, center.as_tuple, radius)

    def draw_text(self, text: str):
        text = self._font.render(text, True, "white")
        self._screen.blit(text, Position(0,0).as_tuple)
    
    def flow_time(self):
        pygame.display.update()
        self._clock.tick(self._fps)

    def paint_background(self, color: Color):
        self._screen.fill(color.as_tuple)

    def exit(self):
        pygame.quit()
        sys.exit()


class Target:
    def __init__(self, game_window: GameWindow, position: Position):
        self.position = position
        self.destroyed = False
        self.timer = 0
        self.game_window = game_window
        

    def onclick(self):
        mouse_pos = Position(*(pygame.mouse.get_pos()))
        if pygame.Rect(self.position.x - 20, self.position.y - 20, 40, 40).collidepoint(mouse_pos.x, mouse_pos.y):
            self.destroyed = True

    def _draw(self):
        if self.destroyed == False:
            self.game_window.draw_circle(
                color=Color(255, 255, 255),
                center=self.position,
                radius=20,
            )

    def update(self):
        if self.destroyed == False: self.timer += 1
        self._draw()


class TargetFactory:
    def __init__(self, game_window: GameWindow, resolution: ScreenResolution):
        self.game_window = game_window
        self.resolution = resolution

    def create_at_center(self) -> Target:
        return Target(game_window=self.game_window, position=Position(x=self.resolution.width//2,y=self.resolution.height//2))

    def create_at_random(self) -> Target:
        return Target(game_window=self.game_window, position=Position(random.randint(0, self.resolution.width), random.randint(0, self.resolution.height)))

class GameSession:
    def __init__(self):

        self.resolution = ScreenResolution()
        self.game_window = GameWindow(resolution=self.resolution)
        self.target_factory = TargetFactory(
            game_window=self.game_window,
            resolution=self.resolution,
        )
        
    def play(self):
        # TODO finish refactoring this function
        target = self.target_factory.create_at_center()

        lives = 5
        dead = False
        score = 0
        globaltimer = 0
        counting = False

        while True:
            if dead == False:
                self.game_window.paint_background(Color.create_black())
            else:
                self.game_window.paint_background(Color.create_red())

            self.game_window.draw_text(f"Score: {score}")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_window.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    target.onclick()

            if dead == False:
                target.update()

                if target.destroyed:
                    counting = True
                else:
                    if target.timer > 70:
                        target = self.target_factory.create_at_random()
                        lives -= 1
                        score -= 5
                        if score < 0: score = 0
                        if lives == 0: dead = True

                if counting:
                    globaltimer += 1
                    if globaltimer == 40 and dead == False:
                        score += 1
                        target = self.target_factory.create_at_random()
                        globaltimer = 0
                        counting = False

            self.game_window.flow_time()

def main():
    game_session = GameSession()
    game_session.play()


if __name__=="__main__":
    main()

