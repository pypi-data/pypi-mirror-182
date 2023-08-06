import glob
import os
import uuid

import pygame.image
from PIL import Image
from pygame import Surface


class Recorder:
    def __init__(self):
        self.identifier = uuid.uuid4()
        self.i = 0

    def reset(self):
        self.identifier = uuid.uuid4()
        self.i = 0

    def record_frame(self, screen: Surface):
        pygame.image.save(screen, f"pics/pic_{self.identifier}_{self.i:04d}.png")
        self.i += 1

    def animate_game(self):
        images = sorted(glob.glob(f"pics/pic_{self.identifier}_*.png"))
        frames = [Image.open(image) for image in images]
        frames[0].save(
            f"game_{self.identifier}.gif",
            save_all=True,
            append_images=frames[1:],
            loop=0,
        )
        for image in images:
            os.remove(image)
