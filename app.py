import os
import shutil

directory = 'C:/Users/unmes/OneDrive/Desktop/PYQ'
folder_names = set()

def rename_files(directory):
  for filename in os.listdir(directory):
      if filename.endswith('.pdf'):
          parts = filename.split(" ")
          name = " ".join(parts[:-1])
          folder_names.add(name)
  for name in folder_names:
      folder_path = os.path.join(directory, name)
      if not os.path.exists(folder_path):
          os.makedirs(folder_path)

def move_folder(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            parts = filename.split(" ")
            folder_name = " ".join(parts[:-1])
            folder_path = os.path.join(directory, folder_name)
            src = os.path.join(directory, filename)
            dest = os.path.join(folder_path, filename)
            shutil.move(src, dest)

# rename_files(directory)
move_folder(directory)
