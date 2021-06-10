from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from Class.LoadWindows import LoadWindows
from threading import Thread

class Windows(Screen):

    instances = []

    link = ObjectProperty()
    proxy = ObjectProperty()
    link_text = ObjectProperty()
    proxy_text = ObjectProperty()

    def AddItem(self):

        try:
            lw = LoadWindows(self.link_text.text, self.proxy_text.text)
            lw.Process()

            # Add instances in list
            self.instances.append(lw)

            # Append Lines
            self.link.text = self.link.text + '\n{0}'.format(self.link_text.text)
            self.proxy.text = self.proxy.text + '\n{0}'.format(self.proxy_text.text)

        except Exception as e:
            print(e)

        self.link_text.text, self.proxy_text.text = '', ''

    def Start(self):
        for d in self.instances:
            t = Thread(target=d.Navigate)
            t.start()


    def ClearItems(self):
        self.instances = []
        self.link.text, self.proxy.text = '', ''