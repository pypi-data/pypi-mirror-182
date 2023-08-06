import glob
import os
import pathlib
import uuid

import pygame.image
from pygame import Surface
import moviepy.video.io.ImageSequenceClip

from sneks.config.config import config


class Recorder:
    def __init__(self):
        self.identifier = uuid.uuid4()
        self.i = 0
        self.prefix = pathlib.Path(config.graphics.record_prefix)
        (self.prefix / "pics").mkdir(exist_ok=True)
        (self.prefix / "movies").mkdir(exist_ok=True)

    def reset(self):
        self.identifier = uuid.uuid4()
        self.i = 0

    def record_frame(self, screen: Surface):
        pygame.image.save(
            screen, self.prefix / "pics" / f"pic_{self.identifier}_{self.i:04d}.png"
        )
        self.i += 1

    def animate_game(self):
        images = sorted(self.prefix.glob(f"pics/pic_{self.identifier}_*.png"))

        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(images, fps=24)
        clip.write_videofile(self.prefix / "movies" / f"game_{self.identifier}.mp4")

        for image in images:
            os.remove(image)
