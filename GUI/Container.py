from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class TaskButton(Button):
    pass

class WindowsButton(Button):
    pass

class AccountsButton(Button):
    pass

class ProxiesButton(Button):
    pass
class ExitButton(Button):
    pass

class Container(GridLayout):

    def ExitButton(self):
        exit()