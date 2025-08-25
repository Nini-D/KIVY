import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label


class MeuApp(App):
    def build(self):
        # layout principal
        box = BoxLayout(orientation="vertical")

        # campo nome
        self.nome = TextInput(hint_text="Digite seu nome")
        box.add_widget(self.nome)

        # escolha de gênero
        self.genero = Spinner(text="Escolha um gênero",
                              values=("Ação", "Comédia", "Animação"))
        box.add_widget(self.genero)

        # botão
        btn = Button(text="Sugerir Filme")
        btn.bind(on_press=self.sugerir)
        box.add_widget(btn)

        # mensagem
        self.msg = Label(text="")
        box.add_widget(self.msg)

        return box

    def sugerir(self, instance):
        n = self.nome.text  # pega nome digitado
        g = self.genero.text  # pega genero

        # listas de filmes
        lista1 = ["Matrix", "John Wick", "Vingadores", "Mad Max"]
        lista2 = ["As Branquelas", "Click", "Se Beber Não Case", "Ace Ventura"]
        lista3 = ["Toy Story", "Shrek", "O Rei Leão", "Procurando Nemo"]

        if n == "":
            self.msg.text = "Digite seu nome!"
        else:
            if g == "Ação":
                filme = random.choice(lista1)
                self.msg.text = "Olá, " + n + "! Sua sugestão de filme de Ação é: " + filme
            elif g == "Comédia":
                filme = random.choice(lista2)
                self.msg.text = "Olá, " + n + "! Sua sugestão de filme de Comédia é: " + filme
            elif g == "Animação":
                filme = random.choice(lista3)
                self.msg.text = "Olá, " + n + "! Sua sugestão de filme de Animação é: " + filme
            else:
                self.msg.text = "Escolha um gênero!"


MeuApp().run()
