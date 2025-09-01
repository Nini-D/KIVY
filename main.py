from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout  # Adicionei isso
from kivy.storage.jsonstore import JsonStore

# Cria o arquivo para salvar o nome
store = JsonStore('dados.json')

class TelaInicial(Screen):
    def salvar_nome(self):
        nome = self.ids.nome_input.text  # Pega o texto do campo
        if nome:  # Só salva se tiver algo escrito
            store.put('usuario', nome=nome)  # Salva o nome no JSON
            self.manager.current = 'boas_vindas'  # Muda para a outra tela
        else:
            self.ids.nome_input.text = "Digite um nome!"  # Mostra erro se vazio

class TelaBoasVindas(Screen):
    def on_pre_enter(self):
        if store.exists('usuario'):  # Verifica se tem nome salvo
            nome = store.get('usuario')['nome']  # Pega o nome
            self.ids.mensagem.text = f"Bem-vindo, {nome}!"  # Mostra na tela
        else:
            self.ids.mensagem.text = "Nenhum nome salvo!"  # Caso não tenha nome

class GerenciadorTelas(ScreenManager):
    pass

class MeuApp(App):
    def build(self):
        return GerenciadorTelas()

if __name__ == '__main__':
    MeuApp().run()