import atexit
import os
import time

import dataAccess.dataAccess as dataAccess
import debug.notification as notification
import dataAccess.servicesConnection as servicesConnection
import dataAccess.youtubeConnection as youtubeConnection
from logic.songTags import register_download
from debug.logger import Logger
from dataAccess import dbConnection

download = True
delete = True
running = True
connected = False
paused = False
restart = False

prev_time = time.time()

#"Loggin"
credentials = ('louis1100', '1234')
my_user = dbConnection.User(*credentials)
my_user.login()

services = ['deezer', 'spotify']
methods_to_load = {'deezer': servicesConnection.deezer_load_list, 'spotify':servicesConnection.spotify_load_list}

def exit_handler():
    Logger.log("Exiting the app")
    notification.show("Closing App")

atexit.register(exit_handler)

def main_process(local_playlist):    
    global download, delete
    
    if not my_user:
        return None
    # notification.show("Starting downloads")
    
    song_list = local_playlist.tracks
    
    playlist = methods_to_load[local_playlist.service](local_playlist.id)
    
    tracks = []
    if not playlist:
        return None
    else:
        tracks = playlist.tracks[:]    
    
    transformed_playlist = servicesConnection.convert_deezer_playlist(playlist)
    if not dbConnection.playlist_exists(transformed_playlist.id):
        my_user.add_playlist(transformed_playlist)    
    
    del playlist
    
    Logger.log("Analizing  list for changes.")
    for x in tracks[:]:
        song_id = x.id
        if dataAccess.check_download(song_id, song_list):
            # notification.show(deezerConnection.make_str(x.title) + " has already been downloaded.\n")
            continue
        else:
            Logger.log(x.title + " isn't downloaded. Starting Download")
        artist = servicesConnection.make_str(x.artist.name)
        song = servicesConnection.make_str(x.title)
        
        notification.show("Downloading " + song.title() + "\nby " + artist + "\n{0}/{1}".format(tracks.index(x)+1, len(tracks)))
        
        if download:
            # vids = youtubeConnection.get_videos(artist, song)
            if youtubeConnection.download_audio(artist, song):
                Logger.log(song + " has been downloaded succesfully. Registering the file.")
                result_song = register_download(x)
                song_list.append(result_song)
                dbConnection.add_song(result_song, local_playlist.id)
                # notification.show(song.title() + " downloaded!")
                #dataAccess.json_pickle(song_list)
            else:
                Logger.log("[Error] Download of " + song + " failed. Aborting.")
    
    max_iter = len(song_list)
    x = 0
    while x < max_iter:
        if not servicesConnection.contains(tracks, song_list[x]):
            Logger.log(song_list[x].title + " isn't on the list anymore. Proceding to delete it")
            Logger.log("Deleting "+song_list[x].title)
            os.system('rm "' + song_list[x].file + '"')
            Logger.log("Deleted " + song_list[x].title)
            notification.show("Deleting " + song_list[x].title)
            
            dbConnection.delete_song(song_list[x].id)
            
            del song_list[x]
            max_iter -= 1
        x += 1
    #dataAccess.json_pickle(song_list)

def main_loop():
    global connected, prev_time, running
    notification.show("Starting Proccess!")
    Logger.log("Starting up program.")
    playlist_list = dataAccess.load_songs()
    while running:        
        if not paused:
            if connected:
                for playlist in playlist_list:
                    main_process(playlist)
                    dataAccess.json_pickle(playlist_list)
                    #dataAccess.load_song(playlist_list)
                prev_time = time.time()
            
            if not dataAccess.internet_connection():
                if connected:
                    notification.show("No Internet Connection")
                    Logger.log("Disconnected from internet")
                    connected = False
            else:
                if not connected:
                    notification.show("Connected")
                    Logger.log("Connected to the internet")
                    connected = True
        
        loaded_config = dataAccess.load_config()
        current_globals = globals()
        for con_vars in loaded_config.keys():
            current_globals[con_vars] = loaded_config[con_vars]
        
        if restart:
            import commands
            commands.start()
            running = False
                    
        # running = 0
    
        time.sleep(5)
    
if __name__ == '__main__':

    loaded_config = dataAccess.load_config()
    
    for var in loaded_config.keys():
        globals()[var] = loaded_config[var]
    
    main_loop()
    
    dataAccess.save_config(globals())
