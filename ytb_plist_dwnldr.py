#https://pytube.io/en/latest/
import sys
import os
from pytube import YouTube
from pytube import Channel
from pytube import Playlist

def clear_name_base(docname,
                slash_replace='-',  # слэш: заменять на минус; используется в идентификаторах документов: типа № 1/2
                quote_replace='',  # кавычки: замены нет - удаляем
                multispaces_replace='\x20', # множественные пробелы на один пробел
                quotes="""“”«»'\""""  # какие кавычки будут удаляться
                ):
    
    docname = docname.replace('[' + quotes + ']', quote_replace)
    docname = docname.replace('[/]', slash_replace)
    docname = docname.replace('[|*?<>:\\\n\r\t\v]', '')  # запрещенные символы в windows
    docname = docname.replace('\\s{2,}', multispaces_replace)
    docname = docname.strip()
    docname = docname.rstrip('-') # на всякий случай
    docname = docname.rstrip('.') # точка в конце не разрешена в windows
    docname = docname.strip()    # не разрешен пробел в конце в windows
    return docname

def clear_name(docname,
                slash_replace='-'):  # слэш: заменять на минус; используется в идентификаторах документов: типа № 1/2
    
    docname = docname.replace('/', slash_replace)
    docname = docname.replace('|', slash_replace)
    docname = docname.replace(':', slash_replace)
    return docname


def list_grabber(list_link: str):
  playlist = Playlist(list_link)
  channel_name = clear_name(playlist.owner)
  playlist_name = clear_name(playlist.title)
  
  if os.path.exists('lists/' + clear_name(channel_name)):
    if os.path.exists('lists/' + clear_name(channel_name) + '/' + clear_name(playlist_name)):
      pass
    else:
      os.mkdir('lists/' + clear_name(channel_name) + '/' + clear_name(playlist_name))
  else:
    os.mkdir('lists/' + clear_name(channel_name))


  #videos_count = playlist.length

  with open('lists/' + clear_name(channel_name) + '/' + clear_name(playlist_name) + '.txt', 'w',encoding = 'utf-8') as f:
    for url in playlist.video_urls:
      f.write(url + '\n')

  with open('lists/' + clear_name(channel_name) + '/' + clear_name(playlist_name) + '.txt', 'r') as f:
    for line in f:
      yt = YouTube(line)
      ys = yt.streams.get_highest_resolution()
      print('Downloading video: ', yt.title)
      path = 'content/' + clear_name(channel_name) + '/' + clear_name(playlist_name)
      ys.download(path)
      print("Done!")

def main():
  while True:
    link = input('Введите exit для выхода или ссылку на плэйлист: ')
    if link == 'exit':
      sys.exit()
    list_grabber(link)

if __name__ == '__main__':
  main()