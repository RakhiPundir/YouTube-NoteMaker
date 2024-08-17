import cv2
import os
from yt_dlp import YoutubeDL

def download_video(youtube_url, output_path='new_video.mp4'):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Ensures .mp4 format
        'outtmpl': output_path,
        'merge_output_format': 'mp4',  # Merge video and audio into mp4 format
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    return output_path

def extract_frames(video_path, output_folder='frames'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    vidcap = cv2.VideoCapture(video_path)
    
    if not vidcap.isOpened():
        print("Error: Could not open video file.")
        return
    
    success, image = vidcap.read()
    count = 0
    
    while success:
        timestamp = int(vidcap.get(cv2.CAP_PROP_POS_MSEC))
        frame_filename = os.path.join(output_folder, f"{timestamp}.jpg")
        cv2.imwrite(frame_filename, image)
        print(f"Saved frame {count} at {timestamp} ms as {frame_filename}")
        
        success, image = vidcap.read()
        count += 1
    
    vidcap.release()
    print(f"Extraction completed. {count} frames saved.")

# youtube_url = "https://www.youtube.com/watch?v=NtyU6aKZ-cY"
def main(youtube_url):
    video_path = download_video(youtube_url)
    extract_frames(video_path)
