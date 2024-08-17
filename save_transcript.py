import os
from yt_dlp import YoutubeDL
from googletrans import Translator

def list_subtitles(youtube_url):
    ydl_opts = {'skip_download': True}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        subtitles = info.get('subtitles')
        if subtitles:
            print("Available subtitles:")
            for lang in subtitles.keys():
                print(f" - {lang}")
        else:
            print("No subtitles found for this video.")
        return subtitles

def download_subtitles(youtube_url, lang_code='ko'):
    ydl_opts = {
        'writesubtitles': True,
        'subtitleslangs': [lang_code],
        'format': 'mp4',
        'outtmpl': 'video.mp4',
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        subtitles = info.get('requested_subtitles')
        
        if subtitles:
            subtitle_file = f"video.{lang_code}.{subtitles[lang_code]['ext']}"
            if os.path.exists(subtitle_file):
                print(f"Subtitle file {subtitle_file} downloaded successfully.")
                return subtitle_file
            else:
                print(f"Expected subtitle file {subtitle_file} not found.")
                return None
        else:
            print("No subtitles available in the specified language.")
            return None

def translate_subtitles(subtitle_file, output_file='translated_timestamps.txt'):
    if not subtitle_file:
        return
    
    with open(subtitle_file, 'r') as f:
        lines = f.readlines()

    translator = Translator()
    translated_lines = []

    for line in lines:
        if "-->" not in line and line.strip() != "":
            translated_text = translator.translate(line.strip(), src='ko', dest='en').text
            translated_lines.append(translated_text + '\n')
        else:
            translated_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(translated_lines)

    print(f"Translated transcript saved to {output_file}.")



def main(youtube_url):
    subtitles = list_subtitles(youtube_url)
    subtitle_file = download_subtitles(youtube_url, lang_code='ko')
    translate_subtitles(subtitle_file)