# maxconsole/maxconsole.py
from rich.console import Console
from rich.color import Color
from rich.theme import Theme
from rich.table import Table
from rich.traceback import install as install_traceback
import threading

__version__ = '0.5.0'

class Singleton(type):
    _instance_lock = threading.Lock()
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with Singleton._instance_lock:
                cls.__instance = super().__call__(*args, **kwargs)
                return cls.__instance
        else:
            return cls.__instance

class MaxConsole(Console, metaclass=Singleton):
    """A custom themed console class that inherits from rich.console.Console"""
    theme: Theme = Theme.read('max_theme.ini')

    def __init__ (self, theme: Theme = Theme.read('max_theme.ini'), *args, **kwargs):
        super().__init__(*args, **kwargs, theme=theme)
        install_traceback(console=self)

    def __call__(self, *args, **kwargs):
        return self

def print_theme_colors():
    console = MaxConsole()
    color_sample = '◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎'
    theme_colors = Table(
        title="Theme Colors",
        show_header=True,
        show_lines=False,
        show_edge=False,
        width=80,
        # padding=(1,1)
    )
    theme_colors.add_column("Color", justify="left", no_wrap=True, ratio=1)
    theme_colors.add_column("Color Example", justify="center", no_wrap=True, ratio=3)
    theme_colors.add_row("magenta", f"[magenta]{color_sample}[/]")
    theme_colors.add_row("purple", f"[purple]{color_sample}[/]")
    theme_colors.add_row("blue_violet", f"[blue_violet]{color_sample}[/]")
    theme_colors.add_row("blue", f"[blue]{color_sample}[/]")
    theme_colors.add_row("cornflower_blue", f"[cornflower_blue]{color_sample}[/]")
    theme_colors.add_row("cyan", f"[cyan]{color_sample}[/]")
    theme_colors.add_row("green", f"[green]{color_sample}[/]")
    theme_colors.add_row("yellow", f"[yellow]{color_sample}[/]")
    theme_colors.add_row("orange", f"[orange]{color_sample}[/]")
    theme_colors.add_row("red", f"[red]{color_sample}[/]")
    theme_colors.add_row("white", f"[white]{color_sample}[/]")
    theme_colors.add_row("light_grey", f"[light_grey]{color_sample}[/]")
    theme_colors.add_row("grey", f"[grey]{color_sample}[/]")
    theme_colors.add_row("dark_grey", f"[dark_grey]{color_sample}[/DARK_GREY]")
    theme_colors.add_row("black", f"[black]{color_sample}[/]")
    console.clear()
    console.print("\n\n")
    console.print(theme_colors, justify="center")
    console.print("\n\n\n\n")

if __name__ == "__main__":
    print_theme_colors()