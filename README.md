# Voice-Memos-Whisper-Transcribe
Python script that handles steps to use Whisper AI to transcribe Apple Voice Memos on Mac

This script converts audio files in the M4A format to plain text using the OpenAI's Whisper AI Transcribe tool. The script takes a folder with M4A files as input and generates text files in a specified output folder. Processed M4A files are then moved to another folder to indicate completion.

## Prerequisites

Before running the script, make sure you have the following installed on your system:

1. **Python 3.9.4 or above**: You can download it from https://www.python.org/downloads/ or use brew. 
2. **Whisper AI**: Install and set up the Whisper AI using the setup for the command line found on the Whisper Github account - https://github.com/openai/whisper  
3. **FFmpeg**: A cross-platform solution for converting multimedia files. This will be installed as part of the Whisper setup above


## Configuration

1. Modify the `config.ini` file replacing the paths with your own


## Usage

Run the script using the command:

python3 WhisperTranscribe.py

## How It Works

The script follows these steps to convert M4A audio files to text:

1. Read the file paths from the `config.ini` file.
2. Loop through all the files in the input directory.
3. Check if the file is an M4A file and replace spaces in the filename with underscores.
4. Use FFmpeg to convert the M4A file to MP3 format.
5. Use the Whisper ASR system to transcribe the MP3 file into a text file, and save it in the specified output folder.
6. Move the input M4A file to the transcribed directory, indicating it has been processed.
7. Delete the temporary MP3 file.


