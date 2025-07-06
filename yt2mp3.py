import os
import yt_dlp

def youtube_to_mp3(youtube_url, output_path='.', cookies_file='www.youtube.com_cookies.txt'): #Change cookies_file parameter here to point to the name of your youtube cookies.txt file
    ydl_opts = {
        'format': 'bestaudio/best',
        'cookies': 'www.youtube.com_cookies.txt', #Change cookies value here to point to the name of your youtube cookies.txt file
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

# Example usage
youtube_url = input("Enter the YouTube URL: ")
output_path = input("Enter the output directory (or press Enter for current directory): ") or '.'
youtube_to_mp3(youtube_url, output_path)
