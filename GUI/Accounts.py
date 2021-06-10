from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from Class.DBProvider import DBProvider

class Accounts(Screen):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(Accounts, self).__init__(**kwargs)
