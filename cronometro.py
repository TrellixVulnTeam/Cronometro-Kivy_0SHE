from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock
from kivy.core.window import Window

class Principal(MDBoxLayout):
    cronoValue = NumericProperty()
    cronoValueText = StringProperty()
    habilitaContagem = BooleanProperty()

    habilitaContagem = False

    def update(self, *args):
        self.cronoValueText = str(self.cronoValue)
        if self.habilitaContagem == True:
            self.cronoValue += 1

    def zerar(self):
        if self.habilitaContagem == False:
            self.cronoValue = 0

    def iniciar(self):
        self.cronoValue = 0
        self.habilitaContagem = True

    def parar(self):
        self.habilitaContagem = False

    def reiniciar(self):
        if self.habilitaContagem == False:
            self.habilitaContagem = True


class Cronometro(MDApp):
    def build(self):
        Window.size = (300, 500)
        self.icon = 'icon.png'
        self.title = 'Cronômetro'
        crono = Principal()
        crono.cronoValue = 0
        Clock.schedule_interval(crono.update, 0.1)
        return crono


if __name__ == '__main__':
    Cronometro().run()
