# File Separator

import os, shutil

# Note: You can write every single extension inside tuple
dict_extensions = {
    'audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac'),
    'video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'document_extensions' : ('.docx', '.pdf', '.txt')
}

folderpath = input('Enter folder path: ')

def file_finder(folder_path, file_extensions):
    # files = []
    # for file in os.listdir(folder_path):
    #     for extension in file_extensions:
    #         if file.endswith(extension):
    #             files.append(file)
    # return files
    return [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]

for extension_type, extension_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] + ' files'
    folder_path = os.path.join(folderpath, folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath, extension_tuple):
        item_path = os.path.join(folderpath, item)
        shutil.move(item_path, os.path.join(folder_path, item))

