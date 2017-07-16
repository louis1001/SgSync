from mutagen.easyid3 import EasyID3
from debug.logger import Logger
import entities.musicEntities as musicEntities
import logic.getArtwork

def set_tags(attributes):
    try:
        Logger.log("Setting tags for " + attributes.title)
        audio = EasyID3(attributes.file)
        valid = audio.valid_keys.keys()
        song_variables = attributes.__dict__
        for attr in song_variables.keys():
            if attr in valid:
                audio[attr] = song_variables[attr]
                audio.save()
        Logger.log("Tags set.")
    except Exception as e:
        print(e)
        Logger.log("[Error] Couldn't set file's tags.")

def register_download(song, set_tag = True):
    
    location = '/home/louis_/Music/'+song.artist.name+' - '+song.title+'.mp3'
        
    b = musicEntities.Song(song.id)
    b.title = song.title
    b.artist = song.artist.name
    try:
        al = song.get_album()
        b.album = al.title        
        b.date = al.release_date
    except:
        al = song.album
        b.album = al.title
        b.cover = al.cover_medium

    b.length = "{0}:{1}".format(int(song.duration / 60), song.duration % 60)
    b.added = song.time_add
    b.service = 'deezer'
    b.file = location
    
    if set_tag:
        set_tags(b)
    
    return b

def set_tag(file, tag, value):
    audio = EasyID3(file)
    valid = audio.valid_keys.keys()
    for x in valid:
        print(x)

if __name__ == '__main__':
    print(EasyID3.valid_keys.keys())

