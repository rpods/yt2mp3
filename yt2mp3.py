import os
import yt_dlp

def youtube_to_mp3(youtube_url, output_path='.'):
    ydl_opts = {
        'format': 'bestaudio/best',
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