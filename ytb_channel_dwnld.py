import sys
import os
import time

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

def playlist_downloader():
  pass

def channel_grabber(channel_link):
  channel = Channel(channel_link)
  name = channel.channel_name


  with open('lists/playlist_' + name + ".txt", 'w', encoding = 'utf-8') as f:
    for url in channel:
      #print('lists/playlist_' + name + ".txt", url)
      f.write(url + '\n')

  with open('lists/playlist_' + name + '.txt', 'r') as f:
    for count, line in enumerate(f):
      yt = YouTube(line)
      ys = yt.streams.get_highest_resolution()
      print('Downloading video: ', yt.title)
      path = 'content/channel_' + name
      ys.download(path)
      print("Done!")

def list_grabber(list_link: str):
  playlist = Playlist(list_link)

  # определим имя директории, которую создаём
  ownerpath = playlist.owner
  playlistpath = playlist.title
  try:
      os.mkdir('lists/' + ownerpath)
  except OSError:
      print ("Создать директорию %s не удалось" % ownerpath)
  else:
      print ("Успешно создана директория %s " % ownerpath)

  try:
      os.mkdir('lists/' + ownerpath + '/' + playlistpath)
  except OSError:
      print ("Создать директорию %s не удалось" % ownerpath + '/' + playlistpath)
  else:
      print ("Успешно создана директория %s " % ownerpath + '/' + playlistpath)


  path = 'lists/' + playlist.owner + '/' + playlist.title + '/playlist_' + playlist.title + '.txt'

  with open(path, 'w', encoding = 'utf-8') as f:
    for url in playlist.video_urls:
      f.write(url + '\n')

  with open(path, 'r') as f:
    for line in f:
      yt = YouTube(line)
      ys = yt.streams.get_highest_resolution()
      print('Downloading video: ', yt.title)
      path = 'content/' + playlist.owner + '/' + playlist.title + '/'
      if os.path.exists('content/' + playlist.owner + '/' + playlist.title + '/' + ys.default_filename):
        print('Уже есть')
      else:
        ys.download(path)
      print("Done!")


def main():

  while True:
    channel_link = input('Введите ссылку на канал или exit для выхода: ')
    if channel_link == 'exit':
      sys.exit()
    else:
      list_grabber(channel_link)

    



if __name__ == '__main__':
  main()