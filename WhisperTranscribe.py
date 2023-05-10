import os
import shutil
import configparser

# Read in file paths from config file. 
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        input_dir = config.get('PATHS', 'input_dir')
        output_dir = config.get('PATHS', 'output_dir')
        transcribed_dir = config.get('PATHS', 'transcribed_dir')
    except configparser.NoSectionError:
        print("Error: 'PATHS' section is missing in the config.ini file.")
        exit(1)

    return input_dir, output_dir, transcribed_dir

# Read in file paths from config
input_dir, output_dir, transcribed_dir = read_config() 

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if file is an M4A file
    if filename.endswith(".m4a"):
        # Replace spaces in the filename with underscores
        new_filename = filename.replace(" ", "_")
        if new_filename != filename:
            os.rename(os.path.join(input_dir, filename), os.path.join(input_dir, new_filename))
            filename = new_filename
        
        # Generate the input and output file paths
        input_file = os.path.join(input_dir, filename)
        print(input_file)
        output_file = output_dir
        print(output_file)
        # Use FFmpeg to convert the MP4 file to mp3 format
        mp3_file = os.path.join(input_dir, os.path.splitext(filename)[0] + ".mp3")
        print(mp3_file)
        os.system(f"ffmpeg -i {input_file} -acodec libmp3lame -ab 192k {mp3_file}")
        
        # Run the Whisper command to transcribe the mp3 file
        os.system(f"whisper {mp3_file} --model base --output_format txt --output_dir {output_file}")
        
        # Move the input file to the transcribed directory
        transcribed_file = os.path.join(transcribed_dir, filename)
        shutil.move(input_file, transcribed_file)

        # Delete the temporary mp3 file
        os.remove(mp3_file)
