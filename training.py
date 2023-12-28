import os

folder_path = "/Users/zeke/Documents/Github/WaysteAI/data/training_data"

# Get the list of files in the folder
files = os.listdir(folder_path)

# Count the number of files
num_files = len(files)

print(f"The number of files in the folder is: {num_files}")

