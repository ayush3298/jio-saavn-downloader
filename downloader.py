import os

import eyed3
import requests
from pydub import AudioSegment


def set_attributes(self, song):
    audiofile = eyed3.load(song)
    audiofile.tag.artist = "Nobunny"
    audiofile.tag.album = "Love Visions"
    audiofile.tag.title = "I Am a Girlfriend"
    audiofile.tag.track_num = 4
    with open('35163665790_d182d84f5e_k.jpg', 'rb') as f:
        image = f.read()
    audiofile.tag.images.set(3, image, "image/jpeg", u"Description")
    audiofile.tag.images.set(2, image, "image/jpeg", u"Description")
    audiofile.tag.images.set(1, image, "image/jpeg", u"Description")
    audiofile.tag.images.set(0, image, "image/jpeg", u"Description")
    audiofile.tag.save()


def convert_to_mp3(self, filename):
    new_filename = filename.replace('m4a', 'mp3')
    sound = AudioSegment.from_file(filename, 'm4a')
    os.remove(filename)
    sound.export(new_filename, format="mp3", bitrate="320k")
    return new_filename


def download(self, url, filename):
    with requests.get(url, stream=True) as res:
        res.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in res.iter_content(chunk_size=1000):
                if chunk:
                    f.write(chunk)
    return filename


set_attributes('self', '1 - Hamari Adhuri kahani - Hamari Adhuri kahani -  Songspk.CC .mp3')
