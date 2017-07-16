import deezer
import requests
from entities import musicEntities
from deezer import Client
from debug.logger import Logger

cl = deezer.Client()

def make_str(value):
    return Client.make_str(value)

def deezer_load_list(LIST_ID):
    """Just Loads a List"""
    Logger.log("Getting the playlist #{} from deezer".format(LIST_ID))
    lis = None
    try:
        lis = cl.get_playlist(LIST_ID)
    except:
        Logger.log("[Error] Couldn't get the list.")
    else:
        Logger.log("Succesfully loaded the list.")
    return lis

def deezer_load_artist(TRACK_ID):
    Logger.log("Getting the artist from song #%s from deezer")
    trck = deezer_load_track(TRACK_ID)
    
    if trck:
        
        art = trck.get_artist()
    
    return art

def deezer_load_track(TRACK_ID):
    Logger.log("Getting the track #%d from deezer" % TRACK_ID)
    
    trck = None
    try:
        trck = cl.get_track(TRACK_ID)
    except:
        Logger.log("[Error] Couldn't get the track.")
    else:
        Logger.log("Succesfully loaded the track.")
    
    return trck

def deezer_load_track_api(TRACK_ID):
    # https://api.deezer.com/version/service/id/method/?parameters
    response = requests.api('GET', 'https://api.deezer.com/version/service/id/{}/?{}')

def deezer_load_album(TRACK_ID):
    
    trck = deezer_load_track(TRACK_ID)
    
    if trck:
        albm = cl.get_album(trck.album.id)
    
    return albm

def convert_deezer_playlist(playlist):
    
    new_playlist = musicEntities.Playlist(playlist.id, service = 'deezer', name = playlist.title, link=playlist.link)
    
    raw_tracks = playlist.tracks
    
    new_tracks = []
    for track in raw_tracks:
        a = convert_deezer_song(track)
        new_tracks.append(a)
    
    new_playlist.tracks = new_tracks
    
    return new_playlist
    
    

def convert_deezer_song(song):
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

    return b

def spotify_load_list(LIST_ID):
    Logger.log("Getting the playlist {} from spotify".format(LIST_ID))
    lis = None
    try:
        pass
    except:
        Logger.log("[Error] Couldn't get the list.")
    else:
        Logger.log("Succesfully loaded the list.")
    
    return lis

def contains(lis, elem):
    for x in lis:
        if x.id == elem.id: return True
    return False