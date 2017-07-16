import http.client as httplib
from dataAccess import dbConnection
import pickle
from logic import songTags
from entities import musicEntities
import jsonpickle
import json

project_path = '/home/louis_/Documents/Python/Projects/DeezerConnection/'
config_file = 'config.json'

use_db = True

def current_user():
    current_config = load_config()    
    credentials = current_config.get('credentials', None)
    
    if credentials:
        return dbConnection.User(*credentials)
    
    return None

def save_config(config):
    
    var_s = ['running', 'download', 'delete', 'paused', 'credentials']
    to_save = {}
    for x in var_s:
        to_save[x] = config[x]
    
    to_save['running'] = True
    
    with open(project_path + config_file, 'w') as file:
        js = json.dumps(to_save, indent=4)
        file.write(js)

def load_config():
    with open(project_path + config_file, 'r') as fl:
        return json.loads(fl.read())

def dump(obj):
    with open(project_path + 'playlist', 'wb') as f:
        pickle.dump(obj,f)

def load():
    with open(project_path + 'playlist', 'rb') as f:
        return pickle.loads(f.read())

def internet_connection():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def register_song(song):
    dbConnection.add_song(song)

def delete_song(song_id):
    dbConnection.delete_song(song_id)

def json_pickle(obj):
    pickled = jsonpickle.encode(obj)
    
    pretty_json = json.dumps(json.loads(pickled), indent=4)
    
    with open(project_path + 'resources/songs.json', 'w') as fl:
        fl.write(pretty_json)
    
def delete_playlist(playlist_id):
    pass

def check_download(song_id, song_list):
    if use_db:
        return dbConnection.song_exists(song_id)
    else:
        for x in song_list:
            if song_id == x.id:
                return True
        return False

def load_songs(client = None):
    if use_db and client:
        try:
            playlist_list = client.get_playlists()
            
            return playlist_list
        
        except Exception as e:
            print(e)
            return []
    else:
        try:
            with open(project_path + 'resources/songs.json', 'r') as fl:
                playlist_list = jsonpickle.decode(fl.read())
                return playlist_list
        except Exception as e:
            return []

def songs_exist(song_path):
    try:
        a= open(song_path, 'r')
        a.read()
        return True
    except FileNotFoundError as e:
        return False
