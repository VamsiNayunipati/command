import sys
from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        print(f'Menu')
        listMenu = self.command_handler.listMenu()
        print("Menu", list(listMenu))
