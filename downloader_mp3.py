import yt_dlp
import os 

def download_mp3(link, caminho = 'C:\\downloader_mp3yt\\music'):
    # Configurações para baixar e converter diretamente para MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{caminho}/%(title)s.%(ext)s',
        'quiet': False,  # Exibe o progresso
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Baixando de: {link}")
        ydl.download([link])


os.system('cls')

link = input('Link da música: ') 
download_mp3(link)
print('\nDownload sucefull\n')