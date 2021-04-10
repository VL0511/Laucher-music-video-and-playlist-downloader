__author__ = 'Zury'

import platform, os
import glob
import pafy
import pydub
from moviepy.editor import *
from pytube import YouTube, Playlist

import youtube_dl

class Baixador:
    def __init__(self, name, age):
      self.url= input('[*]URL: ')
      self.os_system = platform.system()
      
    def clear(self):      
        if os_system == 'Windows':
            os.system('cls')
        elif os_system == 'Linux':
            os.system('clear')
        else:
            print('Não foi possível detectar seu sistema operacional')

    def laucher(self):
        print('''
            Escolha a baixo com opção deseja usar:
            
            1 - Baixar vídeos
            2 - Baixar músicas
            3 - Baixar playlist
        ''')

        op = int(input('[*] Qual opção deseja usar?\nR:'))
        
        while True:
            if op == 1:
<<<<<<< HEAD
                yt = YouTube(self.url)
=======
                url_video = input('URL: ')
                yt = YouTube(url_video)
>>>>>>> c14f5a9621e9774a72879d8be739ed17b60c0177
                print('VÍDEO ESTÁ SENDO BAIXADO!\n %s' %(yt.title))
                video = yt.streams.first()
                video.download()

            elif op == 2:
                params = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': 192
                    }]
                }

                music = pafy.new(self.url)
                audiostreams = music.audiostreams
                
                for i in audiostreams:
                    print('Bitrate: %s, ext: %s, size: %0.2fMb' %
                        (i.bitrate, i.extension, i.get_filesize()/1024/1024))

                audiostreams[1].download()

                list_mp4 = glob.glob('*.mp4')

                for video in list_mp4:
                    mp4 = VideoFileClip(os.path.join(video))
                    name_mp3 = video[:-4]+'.mp3'
                    mp4.audio.write_audiofile(os.path.join(name_mp3))
                    
            elif op == 3:
                pl = Playlist(self.url)
                i = 1
                
                print('INICIANDO DOWNLOAD!')
                for video in pl.videos:
                    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').get_highest_resolution().download('Playlist')
                    try:
                        title = video.title
                        print('Iniciando Download: '+ str(i) + ": " + str(title))
                    except:
                        pass
            else:
                print('Opção não encotrada!')
                
try:
    baixador = Baixador()
    baixador.clear()
    baixador.laucher()
except Exception as e:
    print(f'Error: {e}')
