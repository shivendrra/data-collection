import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

from graze import Freesound

sound = Freesound(api_key="lMKgKjaRmNMZKKxNqkjx", download_dir="audios", metrics=True)
sound(topics=["clicks", "background", "nature"])