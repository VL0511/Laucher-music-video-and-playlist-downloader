__author__ = 'Zury'

import os
import glob
import pafy
import pydub
from moviepy.editor import *
from pytube import YouTube, Playlist

import youtube_dl

class Baixador():
    def __init__(self):
        pass
    
    def laucher(self):
        os.system('clear')
        print('''
            Escolha a baixo com opção deseja usar:
            
            1 - Baixar vídeos
            2 - Baixar músicas
            3 - Baixar playlist
        ''')

        op = int(input('[*] Qual opção deseja usar?\nR:'))
        
        while True:
            if op == 1:
                url_video = input('URL: ')
                yt = YouTube(url_video)
                print(f'VÍDEO ESTÁ SENDO BAIXADO!\n{yt.title}')
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
                url_musica = input('URL: ')

                music = pafy.new(url_musica)
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
                url_playlist_video = input('URL: ')
                
                pl = Playlist(url_playlist_video)
                i = 1
                
                print('INICIANDO DOWNLOAD!')
                for video in pl.videos:
                    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').get_highest_resolution().download('Playlist')
                    try:
                        title = video.title
                        print('Iniciando Download: '+ str(i) + ": " + str(title))
                    except:
                        pass
                
try:
    baixador = Baixador()
    baixador.laucher()
except Exception as e:
    print(f'Error: {e}')
