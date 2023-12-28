import os
from pydub import AudioSegment
import librosa
import re

import re

def remove_special_characters(input_string):
    # Define a regular expression pattern to match special characters (excluding ":" and numbers)
    pattern = re.compile('[^a-zA-Z ]')
    
    # Use the sub() method to replace matched characters with an empty string
    result_string = re.sub(pattern, '', input_string)
    
    return result_string

def process_audio(file_path, output_dir, segment_length=30):
    # Load audio file
    audio = AudioSegment.from_file(file_path)

    # Get file name without extension for caption
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    file_name = remove_special_characters(file_name.lower().capitalize())
    file_name = f'''{file_name.replace("free", "").replace("sold", "").replace("free for profit", "").replace("not sale", "")}'''
    file_name = " ".join(file_name.split())
    file_name = file_name.replace("type beat", "type rap beat^ ")
    file_name = " ".join(file_name.split())
    delimiter = "^"

    # Use split to separate the string into parts based on the delimiter
    split_parts = file_name.split(delimiter)

    # Take the first part, which is the text before the delimiter
    file_name = split_parts[0]

    print(file_name)
    # Convert segment length to milliseconds
    segment_length_ms = segment_length * 1000

    # Set the sample rate to 32000 Hz
    audio = audio.set_frame_rate(32000)

    # Calculate the number of segments
    num_segments = (len(audio) + segment_length_ms - 1) // segment_length_ms

    # Loop through segments
    for i in range(num_segments):
        # Get start time for the segment
        start_time = i * segment_length_ms

        # If this is the last segment, adjust start_time
        if i == num_segments - 1:
            start_time = len(audio) - segment_length_ms

        # Get end time for the segment
        end_time = start_time + segment_length_ms

        # Extract the segment
        segment = audio[start_time:end_time]

        # Save the segment
        output_file_path = os.path.join(output_dir, f'{file_name}_segment_{i:03d}.wav')
        segment.export(output_file_path, format='wav')

        # Save the caption
        with open(os.path.join(output_dir, f'{file_name}_segment_{i:03d}.txt'), 'w') as f:
            f.write(str(file_name))

# Directory setup
output_directory = 'output'
# samples_directory = '/Users/zeke/Documents/Github/WaysteAI/data/training_data'
samples_directory = '/Users/zeke/Documents/Github/WaysteAI/raw'

# Check if the output directory exists, if not, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through the files in the "samples" directory
for file_name in os.listdir(samples_directory):
    if file_name.endswith('.wav') or file_name.endswith('.mp3'):
        file_path = os.path.join(samples_directory, file_name)
        process_audio(file_path, output_directory, segment_length=30)


# Directory where the WAV files are saved
output_directory = 'output'

# Iterate through the files in the directory
for file_name in os.listdir(output_directory):
    # Check if the file is a WAV file
    if file_name.endswith('.wav'):
        # Load the audio file
        file_path = os.path.join(output_directory, file_name)
        audio, sample_rate = librosa.load(file_path, sr=None)

        # Check the shape of the audio
        if audio.shape[0] == 32000 * 30:
            print(f"{file_name} has the correct shape: {audio.shape[0]}")
        else:
            print(f"{file_name} does not have the correct shape. Actual shape: {audio.shape[0]}")
