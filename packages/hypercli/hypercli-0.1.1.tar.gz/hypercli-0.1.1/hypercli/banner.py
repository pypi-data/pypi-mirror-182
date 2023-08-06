from rich.console import Console
from rich.text import Text
from pyfiglet import Figlet
from termcolor import cprint
from os import system, name

class Banner:

    def __init__(self, title, description="", figlet_font='big') -> None:
        self.title = title
        self.description = description
        self.c = Console()
        self.f = Figlet(font=figlet_font)

    def show_banner(self, title_color='blue', descr_color='blue', show_descr=False):
        self.clear()
        self.show_title(title_color=title_color)
        if show_descr:
            self.show_description(descr_color=descr_color)

    def show_title(self, title_color='blue'):
        cprint(self.f.renderText(self.title), color=title_color)

    def show_description(self, descr_color='blue'):
        txt = Text(self.description, justify="cemter")
        txt.stylize(f"italic {descr_color}")
        self.c.print(f"{txt}\n\n")
    
    def clear(self):
        system('cls' if name == 'nt' else 'clear')
