import os

def move_mp3(start_folder, end_folder):
    # traverse root directory, and loop through all files
    # rename (move) files to specified output folder
    for root, dirs, files in os.walk(start_folder):
        for file in files:
            if file.endswith(".mp3"):
                print(root.replace('\\', '/') + "/" + file)
                os.rename(root.replace('\\', '/') + "/" + file,
                          f"{end_folder}/{file}")


if __name__ == 'main':
    start_folder = "C:/Users/Teddy/Desktop/music_folders"
    end_folder = "C:/Users/Teddy/Desktop/songs_output"
    move_mp3(start_folder, end_folder)