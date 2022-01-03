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

'''
#вариант с исходником
if len(sys.argv) < 1:
    print('Синтаксис командной строки: python main.py [прямая ссылка на видос]')
    print('Например python main.py https://www.youtube.com/watch?v=2Lq86MKesG4')
    sys.exit()
elif len(sys.argv) > 1:
    print('Можно только одну ссылку за раз')
    print('Синтаксис командной строки: python main.py [прямая ссылка на видос]')
    print('Например python main.py https://www.youtube.com/watch?v=2Lq86MKesG4')
'''

#Вариант с экзешником
#link = input("Ссылка на видос: ")

main_dir = 'os.getcwd()'
print('Текущая директория')
os.mkdir(main_dir + '/content/')

yt = YouTube('https://www.youtube.com/watch?v=2Lq86MKesG4')
title = yt.title
print(title)

adaptive_video = yt.streams.filter(adaptive=True).order_by('resolution').desc().first()
print('Downloading', adaptive_video)
video_filename = str(main_dir) + '/content/video_temp.webm'
adaptive_video.download(video_filename)

audio = yt.streams.filter(type='audio').order_by('abr').desc().first()
print('Downloading', audio)
audio_filename = str(main_dir) + '/content/audio_temp.webm'
audio.download(audio_filename)

print('Скачанные видео и аудио в сумме занимают:', os.path.getsize(video_filename) + os.path.getsize(audio_filename))


#Скачали видео и аудио, начинаем склеивать и перекодировать

#Создаём файл
file = open('content/' + yt.title + '.mp4', 'w')
file.close()

filename = file.name


#Склеиваем в него дорожки

input_video = ffmpeg.input('content/video_temp.webm')
input_audio = ffmpeg.input('content/audio_temp.webm')



try:
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(filename).run()
except ffmpeg.Error as e:
    print("output")
    print(e.stdout)
    print("err")
    print(e.stderr)

print('Итоговый файл', filename,'занимает', os.path.getsize(filename))

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'content/video_temp.webm')
os.remove(path)
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'content/audio_temp.webm')
os.remove(path)