from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        titulo = Label(text='App de Boas-Vindas', font_size=20)

        self.tinput = TextInput(hint_text='Digite como gostaria de ser chamado.')
        self.input = TextInput(hint_text='Agora digite a sua idade.', input_filter='int')

        self.botao = Button(text='Enviar', font_size=16)
        self.botao.bind(on_press=self.mostrarMensagem)

        self.label = Label(text='', font_size=16)

        layout.add_widget(titulo)
        layout.add_widget(self.tinput)
        layout.add_widget(self.input) 
        layout.add_widget(self.botao)
        layout.add_widget(self.label)

        return layout

    def mostrarMensagem(self, instance):
        nome = self.tinput.text.strip()
        idade_texto = self.input.text.strip()

        if not nome:
            self.label.text = 'Por favor, digite como gostaria de ser chamado.'
            return

        if not idade_texto:
            self.label.text = 'Por favor, digite sua idade.'
            return

        try:
            idade = int(idade_texto)
            if idade >= 60:
                self.label.text = f'Olá, {nome}! Você é idoso e merece muito respeito ❤️.'
            elif idade >= 18:
                self.label.text = f'Olá, {nome}! Você é de maior.'
            else:
                self.label.text = f'Olá, {nome}! Você é de menor.'
        except ValueError:
            self.label.text = 'Idade inválida. Digite um número.'

MeuApp().run()
