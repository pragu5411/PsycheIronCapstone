from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from  kivy.uix.filechooser import FileChooserListView




class root(Widget):
    pass
class MainviewApp(App):
    def build(self):
        return root()


if __name__ == '__main__':
   MainviewApp().run()