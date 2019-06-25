import os

import eyed3
import requests
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TRCK, TALB, USLT, error

def set_attributes(self, song):
    pic_file = '35163665790_d182d84f5e_k.jpg' # pic file
    audio = MP3(song, ID3=ID3)
    try:
        audio.add_tags()
    except Exception as e:
        print(e)
    # audio.tags.add(APIC(
    #     encoding=3,
    #     mime='image/jpeg',
    #     type=3,
    #     desc=u'Cover Picture',
    #     data=open(pic_file,'rb').read()
    # ))
    audio.tags.add(TIT2(encoding=3, text='title'))
    audio.tags.add(TALB(encoding=3, text='testalbum'))
    audio.tags.add(TPE1(encoding=3, text='testartist'))
    audio.tags.add(TRCK(encoding=3, text='5'))
    # audio.tags.add(USLT(encoding=3, lang=u'eng', desc=u'desc', text=item['lyric'].decode('utf-8')))
    audio.save()


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


set_attributes('self','tete.mp3')
