import yt_dlp
import tkinter as tk
from tkinter import filedialog
import os 

def escolher_pasta():
    root = tk.Tk()
    root.withdraw()
    pasta = filedialog.askdirectory(title="Salvar como")
    return pasta if pasta else os.getcwd()

def download_mp3(link, caminho = escolher_pasta()):
    # Configurações para baixar e converter diretamente para MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': 'C:\\Users\\eduardo correa\\AppData\\Local\\ffmpeg\\bin',
        'outtmpl': f'{caminho}/%(title)s.%(ext)s',
        'quiet': False,  # Exibe o progresso
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print('\n')
        print('\t')
        ydl.download([link])
        print('\n')


os.system('cls')

print('\n------ Downloader de música do yt ------\n')
link = input('\nLink da música: ') 
download_mp3(link)

print('\n\nDownload sucefull\n\n')



acao = 0

while acao != '1' or acao !=0:
    acao = input('\nPressione (0) para sair ou (1) para baixar outra msc:  \n')
    if acao == '0':
        print('\nObrigado por usar...\n')
        break
    elif acao == '1':
        os.system('cls')
        link = input('\nLink da música: ') 
        download_mp3(link)
        print('\n\nDownload sucefull\n\n')
    else:
        print('\nErro, digite uma opção válida\n')

     
