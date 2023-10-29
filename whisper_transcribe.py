import whisper
import os
import re

model = whisper.load_model("medium")
# Define the subdirectory path (change this to your desired subdirectory)
subdirectory_path = 'clips/the_art_of_thinking_clearly'

# Define the Markdown file path where you want to append the output
markdown_file_path = 'audible_highlights_the_art_of_thinking_clearly.md'

# List of file paths in Markdown bullet point format
markdown_list = []

# List all files in the subdirectory
files = os.listdir(subdirectory_path)

# Define a regular expression pattern to extract the index from the filename
pattern = r'^.*?(\d+)(?=\.[^.]+$)'

# Define a function to extract the index using regex
def get_index(filename):
    match = re.search(pattern, filename)
    if match:
        return int(match.group(1))
    return float('inf')

# Sort the files based on the extracted index
sorted_files = sorted(files, key=get_index)

# Print the relative paths of the sorted files
for file_name in sorted_files:
    relative_path = os.path.join(subdirectory_path, file_name)
    result = model.transcribe(relative_path)
    print(relative_path)
    markdown_list.append(f'- {result["text"]}')
    
# Append the Markdown list to the Markdown file
with open(markdown_file_path, 'a') as file:
    file.write('\n'.join(markdown_list) + '\n\n')

print("Output appended to", markdown_file_path)



