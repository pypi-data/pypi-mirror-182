from sneks.config.definition import Config, Game, Graphics, Colors


config = Config(
    game=Game(rows=120, columns=240, dynamic_food=False),
    graphics=Graphics(
        cell_size=8,
        padding=1,
        colors=Colors(
            background=(0, 0, 0),
            border=(100, 100, 100),
            invalid=(240, 50, 50),
            food=(0, 100, 0),
        ),
        delay=20,
    ),
    runs=100,
    turn_limit=10000,
)
