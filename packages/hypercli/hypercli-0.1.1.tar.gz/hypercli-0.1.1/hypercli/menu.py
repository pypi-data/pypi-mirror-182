from rich.console import Console
from rich.table import Table


class Menu:
    def __init__(self) -> None:
        self.menu = {}

    def create_menu(self, menu_name):
        self.menu[f"{menu_name}"] = {}

    def add_options(self, menu_name, option, function=None):
        self.menu[menu_name][option] = function

    def show_menu(self, menu_name=None):
        if menu_name == None:
            for k, v in self.menu.items():
                menu_name = k
                break
        table = Table(show_header=False)
        for (index, (k, v)) in enumerate(self.menu[menu_name].items()):
            table.add_row(str(index+1), str(k))
        table.add_section()
        table.add_row("0", "exit", style="red")
        console = Console()
        console.print(table)
        return self.enter_choice(menu_name)

    def enter_choice(self, menu_name):
        choice = input("\u279D ")
        for (index, (k, v)) in enumerate(self.menu[menu_name].items()):
            if int(choice) == index + 1:
                if isinstance(v, str):
                    return self.show_menu(v)
                elif v != None:
                    return v
                else:
                    return self.error()
            elif int(choice) == 0:
                return self.exit()

    def exit(self):
        print("Have a great day")
        return exit

    def error(self):
        print("Invalid input. Program is terminated.")
        return exit
