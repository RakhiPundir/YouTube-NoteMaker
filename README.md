# YouTube NoteMaker

YouTube NoteMaker is a Python-based application that extracts frames and transcripts from a YouTube video, processes them, and creates a well-organized `.docx` file. The final document contains both the extracted frames and their corresponding transcript text, making it easy to take notes from video lectures, tutorials, and more.

## Features

- **Download and Extract**: Downloads a YouTube video, extracts frames, and timestamps.
- **Transcription**: Retrieves the transcript of the video and aligns it with the corresponding frames.
- **Duplicate Removal**: Identifies and removes duplicate frames to avoid redundancy.
- **Document Generation**: Compiles the frames and corresponding transcript text into a `.docx` file.
- **Streamlit GUI**: Provides a user-friendly GUI that allows users to input a YouTube URL and download the final `.docx` file, with the option to view it directly on the page.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/RakhiPundir/YouTube-NoteMaker.git
   cd YouTube-NoteMaker
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv notemaker_env
   source notemaker_env/bin/activate
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the Streamlit app**:

   ```bash
   streamlit run main.py
   ```

2. **Using the App**:
   - Enter the YouTube video URL into the input field.
   - Click the "Start Processing" button.
   - A progress bar will indicate the status of the processing.
   - Once processing is complete, you can download the `.docx` file or view it directly in the app.

### Project Structure

```
YouTube-NoteMaker/
│
├── frames/                   # Folder to save frames from the video
├── save_frames.py            # Script to download the video and extract frames
├── save_transcript.py        # Script to extract the transcript with timestamps
├── delete_duplicate_frames.py # Script to remove duplicate frames
├── merge_notes.py            # Script to merge frames and transcript into a .docx file
├── main.py                   # Streamlit app for the project
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation (this file)
└── output.docx               # Generated document (output)
```

### Scripts

- **`save_frames.py`**: Downloads the YouTube video and extracts frames with timestamps as image names.
- **`save_transcript.py`**: Extracts the transcript from the YouTube video and saves it in a `.txt` file with timestamps.
- **`delete_duplicate_frames.py`**: Deletes duplicate frames from the extracted images.
- **`merge_notes.py`**: Compiles the sorted video frames and matching transcript into a `.docx` file.
- **`main.py`**: The main Streamlit application that integrates all scripts into a GUI.

### Example

1. Input: YouTube video URL.
2. Process:
   - Download video.
   - Extract frames and transcript.
   - Remove duplicate frames.
   - Create a `.docx` file with frames and transcript.
3. Output: A `.docx` file containing all relevant frames and text, ready for note-taking.

### Troubleshooting

- **Video not downloading**: Ensure the URL is correct and the video is accessible.
- **Transcript not found**: The video might not have a transcript available. Consider adding subtitles manually.
- **Infinite loop or performance issues**: Check if there are large transcript files or excessive duplicate frames. Ensure no circular dependencies in the code.

### Contributing

Feel free to fork this project, submit pull requests, or open issues for discussion. Contributions are always welcome!
