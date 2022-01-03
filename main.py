#Ребят, какой прогой скачать с Ютуба 360видос в 8к? Чтоб шлем его правильно воспроизводил?

#Важно! Сначала установить ffmpeg в систему!!! Ссылка на офф.сайт https://www.ffmpeg.org/download.html
#Сначала скачиваются два webm файла (видео и звук), потом они конвертятся в mp4.
#Думаю, что ffmpeg умеет конвертить потоки на лету, но лень сейчас читать маны по ffmpeg.
#Поэтому, нужно иметь на диске свободное пространство примерно в два раза большее,
#чем видеофайл, а это не мало. Сделал вывод размера скачанного видеофайла в консоль,
#вот нужно что бы было еще не меньше, чем примерно столько же.
#Может быть допилю этот говнокод, когда жизнь прогнёт погрузиться в ffmpeg.

from pytube import YouTube
import ffmpeg
import os
import sys

def progress_function(stream, chunk, bytes_remaining):
    print(round((1-bytes_remaining/video.filesize)*100, 3), '% done...')

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

link = input('Скопипасти сюда адрес видоса: ')

#yt = YouTube('https://www.youtube.com/watch?v=2Lq86MKesG4')
yt = YouTube(link, on_progress_callback=progress_function)

title = naming(link)

video = yt.streams.filter(adaptive=True).order_by('resolution').desc().first()
#video = yt.streams.filter(adaptive=True).order_by('resolution').first()
video_filename = 'video_' + title + '.webm'
print('Downloading "' + video_filename + '" with resolution', video.resolution)
video.download(output_path='content/', filename=video_filename)

audio = yt.streams.filter(type='audio').order_by('abr').desc().first()
#audio = yt.streams.filter(type='audio').order_by('abr').first()
print('Downloading sound with bitrate', audio.abr)
audio_filename = 'audio_' + title + '.webm'
audio.download(output_path='content/', filename=audio_filename)

video_filesize = os.path.getsize('content/' + video_filename)
audio_filesize = os.path.getsize('content/' + audio_filename)
print('Оба файла в сумме весят:', round(((video_filesize + audio_filesize) / 1e+6), 1), 'МБайт')


#Скачали видео и аудио, начинаем склеивать и перекодировать
print()


input_video = ffmpeg.input('content/' + video_filename)
input_audio = ffmpeg.input('content/' + audio_filename)

output_filename = 'content/' + title + '.mp4'

joined = ffmpeg.concat(input_video, input_audio, v=1, a=1)
out = ffmpeg.output(joined, output_filename)
out.run()


path = 'content/' + video_filename
os.remove(path)
path = 'content/' + audio_filename
os.remove(path)


