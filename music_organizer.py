import os
import eyed3

# os.rename("tester.mp3", "tester1.mp3")






# os.rename("tester.mp3", f"{artist} - {title}")
file_count = 0
error_list = []

# https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
# This gives the directory path from which the .py file is being run
directory_path = os.path.dirname(os.path.realpath(__file__))
for file in os.listdir(directory_path):
    # print(file)
    filename = os.fsdecode(file)

    # print(filename)
    # Append not temporary (~) excel files to header_list
    if filename.endswith(".mp3"):
        audiofile = eyed3.load(filename)
        # print(f'artist: {audiofile.tag.artist}, title: {audiofile.tag.title}')
        # title = audiofile.tag.title
        artist = audiofile.tag.artist



        file_count += 1
