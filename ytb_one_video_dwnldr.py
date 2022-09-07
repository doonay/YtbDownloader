# Выбор действия
#0. вводим ссылку на отдельный видос
#1. вводим ссылку на канал
#1.0 скачиваем весь канал
#1.1 выбираем плэйлист для скачивания
import sys
import os

#import ch_grabber
#import lst_grabber

from pytube import YouTube
from pytube import Channel
from pytube import Playlist

#https://www.youtube.com/watch?v=w-w7omxJuOk
def max_downloader(link: str, path: str):
  yt = YouTube(link)
  ys = yt.streams.get_highest_resolution()
  print('Downloading video: ', yt.title)
  ys.download(path)
  print("Done!")

def main():

  while True:
    # Выбор действия
    choice = input('exit или видос: ')
    if choice == '2':
      choice == 'exit'
      sys.exit()
    max_downloader(choice, 'content/')

if __name__ == '__main__':
  main()