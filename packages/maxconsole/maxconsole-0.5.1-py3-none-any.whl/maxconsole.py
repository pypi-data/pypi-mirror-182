# maxconsole/maxconsole.py
from rich.console import Console
from rich.color import Color
from rich.theme import Theme
from rich.table import Table
from rich.traceback import install as install_traceback
import threading

__version__ = '0.5.1'

MAX_THEME = Theme(
    {
        "magenta": "#ff00ff",
        "purple": "#af00ff",
        "blue_violet": "#5f00ff",
        "blue": "#0000ff",
        "cyan": "#00ffff",
        "orange": "#ff8800",
        "red": "#ff0000",
        "white": "#ffffff",
        "light_grey": "#cccccc",
        "grey": "#888888",
        "dark_grey": "#444444",
        "black": "#111111",
        "debug": "#00ffff",
        "info": "italic #249df1",
        "success": "bold #00ff00",
        "warning": "bold #ffff00",
        "error": "bold #ff0000",
        "critical": "bold underline blink #ffffff on #ff0000",
        "log.time": "#249df1",
        "repr.error": "not bold #ff00ff",
        "logging.level.debug": "#00ffff",
        "logging.level.info": "italic #249df1",
        "logging.level.success": "bold #00ff00",
        "logging.level.warning": "bold #ffff00",
        "logging.level.error": "bold #000000 on #aa0000  ",
        "logging.level.critical": "bold underline blink #ffffff on #ff0000",
        "table.title": "bold #af00ff",
        "table.header": "bold #ff00ff",
        "table.border": "#5f00ff",
        "table.row.odd": "#ffffff on #444444",
        "table.row.even": "#ffffff on #000000",
        "rule.line": "bold #ffffff",
        "rule.title": "bold #af00ff",
        "panel.title": "bold #af00ff",
        "panel.border": "#5f00ff"
    }
)
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
    theme: Theme = MAX_THEME

    def __init__ (self, theme: Theme = MAX_THEME, *args, **kwargs):
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