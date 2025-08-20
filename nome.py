from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.tinput = TextInput(hint_text='Digite como gostaria de ser chamado.')
        self.botao = Button(text='Enviar')
        self.label = Label(text='')

        self.botao.bind(on_press=self.mostrarMensagem)

        self.layout.add_widget(self.tinput)
        self.layout.add_widget(self.botao)
        self.layout.add_widget(self.label)

        return self.layout

    def mostrarMensagem(self, instance):
        nome = self.tinput.text.strip()
        if nome:
            self.label.text = f'Olá, {nome}!'
        else:
            self.label.text = 'Digite como gostaria de ser chamado.'

MeuApp().run()
