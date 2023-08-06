from dataclasses import dataclass


@dataclass(frozen=True)
class Game:
    rows: int
    columns: int
    dynamic_food: bool


@dataclass(frozen=True)
class Colors:
    background: tuple[int, int, int]
    border: tuple[int, int, int]
    invalid: tuple[int, int, int]
    food: tuple[int, int, int]


@dataclass(frozen=True)
class Graphics:
    cell_size: int
    padding: int
    colors: Colors
    delay: int


@dataclass(frozen=True)
class Config:
    game: Game
    graphics: Graphics | None
    runs: int
    turn_limit: int
