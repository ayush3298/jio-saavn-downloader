from get_json import getAlbum, get_soup, make_song, setDecipher, getPlayList, get_song
import requests


class saavn:
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {'accept': 'application/json, text/javascript, */*; q=0.01',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9,lb;q=0.8', 'cache-control': 'no-cache',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'origin': 'https', 'pragma': 'no-cache', 'referer': 'https',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        # self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        self.session.get('https://www.jiosaavn.com')

    def getAlbum(self, Album_url):
        return getAlbum(self, Album_url)

    def get_soup(self, url):
        return get_soup(self, url)

    def make_json(self, json_data):
        return make_song(self, json_data)

    def setDecipher(self):
        return setDecipher(self)

    def getPlayList(self, link):
        return getPlayList(self, link)

    def get_song(self, link):
        return get_song(self, link)


s = saavn()
# print(s.getPlayList('https://www.jiosaavn.com/featured/top-jiotunes---hindi/AZNZNH1EwNjfemJ68FuXsA__'))
# print(s.getAlbum('https://www.jiosaavn.com/artist/indian-ocean-songs/gPMMmR0gs-4_'))
# playlist = s.getPlayList(
#     'https://www.jiosaavn.com/s/playlist/3de540de72015c76dc3dda3f56790f77/Indian_Ocean/joXCH97pnMsGSw2I1RxdhQ__')
# for play in playlist:
#     print(play.url)
l = s.get_song(
    'https://www.jiosaavn.com/song/akh-kashni/LwVeWiNWY14?referrer=svn_source%3Dshare&svn_medium=com.whatsapp&utm_source=share&utm_medium=com.whatsapp')
print(l[0].url
      )
