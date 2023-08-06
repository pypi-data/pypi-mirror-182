from sneks.config.config import config
from sneks.engine.state import State


def main():
    runs = 0
    state = State()
    state.reset()
    if config.graphics:
        from sneks.gui.graphics import Painter
        from sneks.gui.recorder import Recorder

        recorder = None  # Recorder()
        painter = Painter(recorder=recorder)
        painter.initialize()
        while runs < config.runs:
            painter.clear()
            painter.draw_boarders()
            for snake in state.active_snakes:
                painter.draw_snake(snake.cells, True, snake.color)
            for snake in state.ended_snakes:
                painter.draw_snake(snake.cells, False, snake.color)
            for food in state.food:
                painter.draw_food(food)
            if state.should_continue(config.turn_limit):
                painter.draw(delay=config.graphics.delay)
                state.step()
            else:
                painter.draw(delay=1000)
                print(f"Run complete: {runs}")
                if recorder:
                    recorder.animate_game()
                    recorder.reset()
                state.report()
                runs += 1

                state.reset()
    else:
        while runs < config.runs:
            if state.should_continue(config.turn_limit):
                state.step()
            else:
                state.reset()
                runs += 1
                if runs % (config.runs / 20) == 0:
                    print("{}% complete".format(100 * runs / config.runs))


if __name__ == "__main__":
    main()
