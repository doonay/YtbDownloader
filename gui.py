import main
import os

from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.list import MDList, OneLineListItem
from pytube import YouTube

size = Window.size
print(size)
Window.size = (800, 400)
size = Window.size
print(size)

class GameCard(MDCard):
    source = StringProperty()
    text = StringProperty()
    shadow = StringProperty()

class Screen(FloatLayout):
    cards = []
    img_count = 0

    def get_thumb(self):
        yt = YouTube('https://www.youtube.com/watch?v=lEAjwY5TAsE')
        print(yt.thumbnail_url)

    def find_video(self, link):
        print(link.text)

    def scan_games(self, year='22'):
        #year = self.textinput.text
        #finalCardList = pyParser.parsing('20' + year)
        #print('20' + year)
        #for i in finalCardList:
        #    print(i)
        pass

    def get_games_from_db(self):
        #self.cards = db_full.db_select_all_data('games')
        #filename = 'assets/' + self.cards[self.img_count][0] + '.jpg'

        #for card in self.cards:
        #    self.ids.list_wgt.add_widget(
        #        OneLineListItem(text=str(card[0]))
        #    )

        #if os.path.exists(filename):
        #    self.game_img.source = filename
        ##    self.game_name.text = self.cards[self.img_count][0]
        #    pass
        ##else:
        #    # this would throw the exception
        ##    print('Downloading', filename, '...', end='')
        #    print('Done')
        #    pyParser.img_downloader(self.cards[self.img_count][0], self.cards[self.img_count][2])
        #    self.game_img.source = filename
        #    self.game_name.text = self.cards[self.img_count][0]
        #    pass
        pass
    def next_game(self):
        '''
        #получить список ссылок из базы и по нему итерироваться меняя глобальный счётчик
        self.img_count += 1
        filename = 'assets/' + self.cards[self.img_count][0] + '.jpg'

        if os.path.exists(filename):
            self.game_img.source = filename
            self.game_name.text = self.cards[self.img_count][0]
        else:
            # this would throw the exception
            print('Downloading', filename, '...', end='')
            print('Done')
            pyParser.img_downloader(self.cards[self.img_count][0], self.cards[self.img_count][2])
            self.game_img.source = filename
            self.game_name.text = self.cards[self.img_count][0]
        '''
    def prev_game(self):
        '''
        #получить список ссылок из базы и по нему итерироваться меняя глобальный счётчик
        self.img_count -= 1
        filename = 'assets/' + self.cards[self.img_count][0] + '.jpg'

        if os.path.exists(filename):
            self.game_card.source = filename
            self.game_card.text = self.cards[self.img_count][0]
        else:
            # this would throw the exception
            print('Downloading', filename, '...', end='')
            print('Done')
            pyParser.img_downloader(self.cards[self.img_count][0], self.cards[self.img_count][2])
            self.game_card.source = filename
            self.game_card.text = self.cards[self.img_count][0]
        '''
class GuiApp(MDApp):
    def build(self):
        return Screen()

    def on_start(self, **kwargs):
        #self.root.textinput.text = '22'
        #self.root.get_games_from_db()
        pass

if __name__ == '__main__':
	GuiApp().run()