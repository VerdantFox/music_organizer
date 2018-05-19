#!/usr/bin/python

import os

# traverse root directory, and loop through all files
# rename (move) files to specified output folder
for root, dirs, files in os.walk("C:/Users/Teddy/Desktop/music_folders"):
    for file in files:
        if file.endswith(".mp3"):
            print(root.replace('\\', '/') + "/" + file)
            os.rename(root.replace('\\', '/') + "/" + file,
                      f"C:/Users/Teddy/Desktop/songs_output/{file}")
