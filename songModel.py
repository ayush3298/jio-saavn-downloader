class songModel:
    def __init__(self, title, album, year, url, release_date, image, artist, genre):
        self.title = title
        self.album = album
        self.year = year
        self.url = url
        self.release_date = release_date
        self.image = image
        self.artist = artist
        self.genre = genre

    def __str__(self):
        return self.title



    def download(self):pass
#         todo
# 1. Download the song
# 2. Update metadata of song
# 3. save
