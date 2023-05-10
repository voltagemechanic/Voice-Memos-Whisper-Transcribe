# Voice-Memos-Whisper-Transcribe
Python script that handles steps to use Whisper AI to transcribe Apple Voice Memos on Mac

This script converts audio files in the M4A format to text using the OpenAI's Whisper AI Transcribe tool. The script takes a folder with M4A files as input and generates text files in a specified output folder. Processed M4A files are then moved to another folder to indicate completion.

Prerequisites

Before running the script, make sure you have the following installed on your system:

Python 3: You can download it from https://www.python.org/downloads/ or use brew. 
Whisper AI: Install and set up the Whisper AI using the setup for the command line found on the Whisper Github account - https://github.com/openai/whisper  
FFmpeg: A cross-platform solution for converting multimedia files. This will be installed as part of the Whisper setup above

