import pygame
import dataclasses

available_resolutions = {
   "1000x600": (1000, 600),
}


@dataclasses.dataclass
class WindowConfig:
    resolution: tuple = available_resolutions["1000x600"]


class Window:
    def __init__(self, config: WindowConfig):
        pygame.display.set_mode(config.resolution)


