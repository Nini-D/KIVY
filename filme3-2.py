import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class TelaBoasVindas(Screen):
    pass


class TelaSugestao(Screen):
    def set_nome(self, nome):
        self.nome = nome
        self.ids.label_boas_vindas.text = f"Olá, {nome}! Escolha um gênero de filme."

    def sugerir_filme(self):
        genero = self.ids.spinner_genero.text
        filmes = {
            "Ação": ["Matrix", "John Wick", "Vingadores", "Mad Max"],
            "Comédia": ["As Branquelas", "Click", "Se Beber Não Case", "Ace Ventura"],
            "Animação": ["Toy Story", "Shrek", "O Rei Leão", "Procurando Nemo"]
        }

        if genero in filmes:
            filme = random.choice(filmes[genero])
            self.ids.label_filme.text = f"{self.nome}, sua sugestão de {genero} é: {filme}"
        else:
            self.ids.label_filme.text = "Escolha um gênero válido!"


class GerenciadorTelas(ScreenManager):
    pass


class MeuApp(App):
    def build(self):
        sm = GerenciadorTelas(transition=FadeTransition())
        return sm


if __name__ == "__main__":
    MeuApp().run()
