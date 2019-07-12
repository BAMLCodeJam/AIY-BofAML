import pafy, pyglet
import urllib.request
from urllib.parse import *
from bs4 import BeautifulSoup
import vlc

class Youtube_mp3():
    def __init__(self):
        self.lst = []
        self.dict = {}
        self.dict_names = {}
        self.playlist = []

    def url_search(self, search_string, max_search):
        textToSearch = search_string
        query = urllib.parse.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        i = 1
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            if len(self.dict) < max_search:
                self.dict[i] = 'https://www.youtube.com' + vid['href']
                i += 1
            else:
                break


    def get_search_items(self, max_search):

        if self.dict != {}:
            i = 1
            for url in self.dict.values():
                try:
                    info = pafy.new(url)
                    self.dict_names[i] = info.title
                    print("{0}. {1}".format(i, info.title))
                    i += 1

                except ValueError:
                    pass

    def play_media(self, num):
        url = self.dict[int(num)]
        info = pafy.new(url)
        #audio = info.m4astreams[-1]
        print(url)
        print(info)
        audio = info.getbestaudio()
        player=vlc.MediaPlayer(audio.url)
        return player
        player.play()
        
        
        return
        
        
        audio.download()
        song = pyglet.media.load('song.m4a')
        player = pyglet.media.Player()
        print(song)
        print(url)
        print(info)
        player.queue(song)
        print("Playing: {0}.".format(self.dict_names[int(num)]))
        player.play()
        stop = ''
        while True:
            stop = input('Type "s" to stop; "p" to pause; "" to play; : ')
            if stop == 's':
                player.pause()
                break
            elif stop == 'p':
                player.pause()
            elif stop == '':
                player.play()
            elif stop == 'r':
                #player.queue(song)
                #player.play()
                print('Replaying: {0}'.format(self.dict_names[int(num)]))
                

if __name__ == '__main__':
    x = Youtube_mp3()
    search = input("Youtube Search: ")
    old_search = search
    max_search = 5
    if search != '':
        print(old_search)
        print('\nFetching for: {0} on youtube.'.format(old_search.title()))
        x.url_search(search, max_search)
        x.get_search_items(max_search)
        song_number = input('Input song number: ')
        x.play_media(song_number)
