import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class JokeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = Label(text='Clique no botão para ver uma piada!', halign='center', valign='middle')
        self.button = Button(text='Mostrar Piada')
        self.button.bind(on_press=self.get_joke)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        return self.layout

    def get_joke(self, instance):
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        if response.status_code == 200:
            joke = response.json()
            self.label.text = f"{joke['setup']}\n\n{joke['punchline']}"
        else:
            self.label.text = 'Erro ao carregar piada.'

if __name__ == '__main__':
    JokeApp().run()
