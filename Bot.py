from get_json import getAlbum, get_soup, make_json, setDecipher


class saavn:
    def getAlbum(self, Album_url):
        return getAlbum(self, Album_url)

    def get_soup(self, url):
        return get_soup(self, url)

    def make_json(self, json_data):
        return make_json(self, json_data)

    def setDecipher(self):
        return setDecipher(self)


s = saavn()
# print(s.getPlayList('https://www.jiosaavn.com/featured/top-jiotunes---hindi/AZNZNH1EwNjfemJ68FuXsA__'))
print(s.getAlbum('https://www.jiosaavn.com/album/kalank/Jv-F,nN0JoY_'))
