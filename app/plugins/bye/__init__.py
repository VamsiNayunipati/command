from app.commands import Command


class ByeCommand(Command):
    def execute(self):
        print("See you around!")
