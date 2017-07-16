from dataAccess import dataAccess
import lyricwikia

import codecs
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, USLT

TEXT_ENCODING = 'utf8'

my_songs = dataAccess.load_songs()

def set_lyrics(lyrics, file):
    
    print("Finding Lyrics For\n", file, '\n')
    
    fname = file
    
    tags = ID3(fname)
    
    if len(tags.getall(u"USLT::'en'")) == 0:    
        tags[u"USLT::'eng'"] = (USLT(encoding=3, lang=u'eng', desc=u'desc', text=lyrics))
        
        tags.save(fname)
    

def get_lyrics(artist, song):
    return lyricwikia.get_lyrics(artist, song)

for song in my_songs[0].tracks:
    try:
        lyrics = get_lyrics(song.artist.lower(), song.title.lower())
    except:
        continue
    
    set_lyrics(lyrics, song.file)
