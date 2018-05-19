import os
import eyed3


def rename_mp3_files(abs_path_to_folder):
    files_changed = 0
    title_author_error_count = 0
    title_author_error_list = []
    already_exists_error_count = 0
    already_exists_error_list = []
    OsError_count = 0
    OsError_list = []

    # traverse root directory, and loop through all files
    # rename (move) all files in those folders
    for root, dirs, files in os.walk(abs_path_to_folder):
        for file in files:
            if file.endswith(".mp3"):
                # Path to file directory and file itself
                dir_path = root.replace('\\', '/')
                file_path = dir_path + "/" + file

                # Get mp3 meta data for title and artist
                audiofile = eyed3.load(file_path)
                title = audiofile.tag.title
                artist = audiofile.tag.artist

                if title and artist:
                    new_name = f'{audiofile.tag.artist} - {audiofile.tag.title}.mp3'
                    print(new_name)
                    try:
                        os.rename(file_path, f"{dir_path}/{new_name}")
                        files_changed += 1
                    except FileExistsError:
                        print(f"fileExistsError for: {file}")
                        already_exists_error_list.append(file_path)
                        already_exists_error_count += 1
                        continue
                    except OSError:
                        print(f"OsError for: {file}")
                        OsError_list.append(file_path)
                        OsError_count += 1
                        continue

                else:
                    print(f"title or author missing: {file}")
                    title_author_error_list.append(file_path)
                    title_author_error_count += 1

    print(f"files changed count: {files_changed}")

    if title_author_error_count:
        print(f"Error count for no title/author: {title_author_error_count}")
        print(f"files with errors due to no title/author:")
        for file in title_author_error_list:
            print(file)

    if already_exists_error_count:
        print(f"'file already exists' error count: {already_exists_error_count}")
        print(f"files with errors due to 'already exists':")
        for file in already_exists_error_list:
            print(file)
    if OsError_count:
        print(f"'OsError (syntax error) count: {OsError_count}")
        print(f"files with OsErrors (syntax errors)':")
        for file in OsError_list:
            print(file)


if __name__ == '__main__':
    music_folder_path = "C:/Users/Teddy/Desktop/Electronica"
    rename_mp3_files(music_folder_path)