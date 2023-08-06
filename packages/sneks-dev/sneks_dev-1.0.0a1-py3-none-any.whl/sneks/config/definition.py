from dataclasses import dataclass
from typing import Optional, Tuple, List


@dataclass(frozen=True)
class Game:
    rows: int
    columns: int
    dynamic_food: bool
    food: int


@dataclass(frozen=True)
class Colors:
    background: Tuple[int, int, int]
    border: Tuple[int, int, int]
    invalid: Tuple[int, int, int]
    food: Tuple[int, int, int]
    snake: List[Tuple[int, int, int]]


@dataclass(frozen=True)
class Graphics:
    cell_size: int
    padding: int
    colors: Colors
    delay: int


@dataclass(frozen=True)
class Config:
    game: Game
    graphics: Optional[Graphics]
    runs: int
    turn_limit: int
