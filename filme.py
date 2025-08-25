import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.campo_nome = TextInput(hint_text="Digite seu nome", multiline=False)
        layout.add_widget(self.campo_nome)

        botao = Button(text="Sugerir Filme")
        botao.bind(on_press=self.sugerir_filme)
        layout.add_widget(botao)

        self.mensagem = Label(text="")
        layout.add_widget(self.mensagem)

        return layout

    def sugerir_filme(self, instance):

        filmes = ["Matrix", "Toy Story", "Avatar", "O Rei Leão", "Homem-Aranha"]
        nome = self.campo_nome.text.strip()  
        if nome == "":  
            self.mensagem.text = "Por favor, digite seu nome."
        else:
            filme_escolhido = random.choice(filmes) 
            self.mensagem.text = f"Olá, {nome}! Sua sugestão de filme é: {filme_escolhido}."


MeuApp().run()
