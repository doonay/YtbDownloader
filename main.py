from pytube import YouTube

import os
import sys
import subprocess

def progress_function(stream, chunk, bytes_remaining):
    print('Downloading', round((1-bytes_remaining/video.filesize)*100, 3), '% done...')

def naming(old_name):
    #https://www.youtube.com/watch?v=V5zYRSwIQIQ&t=434s
    if old_name.rfind('&t=\d+s'):
        x = old_name.rfind('&')
        name_without_t = old_name[:x]
        y = name_without_t.rfind('=')
        return(old_name[y+1:x])
    else:
        x = old_name.rfind('=')
        return(old_name[x:])

def tests():
    link = input('Скопипасти сюда адрес видоса: ')

    # yt = YouTube('https://www.youtube.com/watch?v=2Lq86MKesG4')
    yt = YouTube(link, on_progress_callback=progress_function)

    title = naming(link)

    video = yt.streams.filter(adaptive=True).order_by('resolution').desc().first()
    # video = yt.streams.filter(adaptive=True).order_by('resolution').first()
    video_filename = 'video_' + title + '.webm'
    print('Downloading "' + video_filename + '" with resolution', video.resolution)
    # video.download(output_path='content/', filename=video_filename)

    audio = yt.streams.filter(type='audio').order_by('abr').desc().first()
    # audio = yt.streams.filter(type='audio').order_by('abr').first()
    print('Downloading sound with bitrate', audio.abr)
    # audio_filename = 'audio_' + title + '.webm'
    # audio.download(output_path='content/', filename=audio_filename)

    # video_filesize = os.path.getsize('content/' + video_filename)
    # audio_filesize = os.path.getsize('content/' + audio_filename)
    # print('Оба файла в сумме весят:', round(((video_filesize + audio_filesize) / 1e+6), 1), 'МБайт')


if __name__ == '__main__':
    tests()