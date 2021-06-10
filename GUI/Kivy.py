from kivy.app import App
from kivy.lang import Builder
from GUI.Container import Container
from GUI.Windows import Windows
from GUI.Menu import *
from kivy.config import Config

from os import listdir
kv_path = 'GUI/kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

class MainApp(App):
    def build(self):
        self.title = 'SNEAKERS'
        Config.set('graphics', 'width', '1024')
        Config.set('graphics', 'height', '768')
        return Container()
