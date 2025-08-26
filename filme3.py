import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label

class TelaBoasVindas(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.input_nome = TextInput(hint_text="Digite seu nome", multiline=False)
        btn_continuar = Button(text="Continuar")
        btn_continuar.bind(on_press=self.ir_para_sugestao)

        layout.add_widget(self.input_nome)
        layout.add_widget(btn_continuar)
        self.add_widget(layout)

    def ir_para_sugestao(self, instance):
        nome = self.input_nome.text
        if nome.strip() == "":
            return 
        self.manager.get_screen("sugestao").set_nome(nome)
        self.manager.current = "sugestao"

class TelaSugestao(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.label_boas_vindas = Label(text="")
        self.spinner_genero = Spinner(text="Escolha um gênero",
                                      values=["Ação", "Comédia", "Animação"])
        btn_sugerir = Button(text="Sugerir Filme")
        btn_sugerir.bind(on_press=self.sugerir_filme)
        self.label_filme = Label(text="")

        layout.add_widget(self.label_boas_vindas)
        layout.add_widget(self.spinner_genero)
        layout.add_widget(btn_sugerir)
        layout.add_widget(self.label_filme)
        self.add_widget(layout)

    def set_nome(self, nome):
        self.nome = nome
        self.label_boas_vindas.text = f"Olá, {nome}! Escolha um gênero de filme."

    def sugerir_filme(self, instance):
        genero = self.spinner_genero.text
        filmes = {
            "Ação": ["Matrix", "John Wick", "Vingadores", "Mad Max"],
            "Comédia": ["As Branquelas", "Click", "Se Beber Não Case", "Ace Ventura"],
            "Animação": ["Toy Story", "Shrek", "O Rei Leão", "Procurando Nemo"]
        }

        if genero in filmes:
            filme = random.choice(filmes[genero])
            self.label_filme.text = f"{self.nome}, sua sugestão de {genero} é: {filme}"
        else:
            self.label_filme.text = "Escolha um gênero válido!"

class GerenciadorTelas(ScreenManager):
    pass

class MeuApp(App):
    def build(self):
        sm = GerenciadorTelas()
        sm.add_widget(TelaBoasVindas(name="boasvindas"))
        sm.add_widget(TelaSugestao(name="sugestao"))
        return sm

MeuApp().run()
