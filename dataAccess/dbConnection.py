import pymysql.cursors
from entities import musicEntities
from dataAccess.youtubeConnection import save_path
from dataAccess import servicesConnection
from debug.logger import Logger
import datetime

host = "localhost"
user = "root"
passwd = "1234"
database = "SgSync"

connection = pymysql.connect(
    host=host,
    user=user,
    passwd=passwd,
    database=database,
    cursorclass=pymysql.cursors.DictCursor
)

class User(object):
    
    def __init__(self, usr_name = '', usr_pass = '', usr_email = ''):
        
        self.name = usr_name
        self.password = usr_pass
        self.email = usr_email
        self.logged = False
     
    def login(self):
        result = False
        
        try:
            with connection.cursor() as cursor:
                sql = "SELECT login(%s, %s) as result"
                cursor.execute(sql, (self.name, self.password))
                result = bool(cursor.fetchone()['result'])
                
                connection.commit()
        except:
            pass
        
        return result
    
    def add_playlist(self, playlist):
        """ Register a playlist in the database, and its songs."""
        Logger.log("Adding the playlist %s to the database." % playlist.id)
        new_id = playlist.id
        new_name = playlist.name
        new_service = musicEntities.supported_services.index(playlist.service)
        new_link = playlist.link
        
        try:
            with connection.cursor() as cursor:
                sql = "insert into playlist (idplaylist, name, idservice, link) values(%s, %s, %s, %s)"
                
                cursor.execute(sql, (new_id, new_name, new_service, new_link))
        except Exception as e:
            print(e)
            connection.rollback()
        else:
            connection.commit()
        
        
        Logger.log("Adding it to the user_playlist table.")
        try:
            with connection.cursor() as cursor:
                sql = "insert into user_playlist (usrname, idplaylist) values(%s, %s)"
                
                cursor.execute(sql, (self.name, new_id))
                print("added to user_playlist")
        except Exception as e:
            print(e)
            
            connection.rollback()
        else:
            connection.commit()
        
            
        new_songs = playlist.tracks
        
        for song in new_songs:
            add_song(song, new_id)
    
    def get_playlists(self):
        with connection.cursor() as cursor:
            sql = "select * from playlist where idplaylist = %s"
            cursor.execute(sql, (str(playlist_id),))
            
            result = cursor.fetchall()
        
        list_playlist = []
        for dict_playlist in result:
            new_list = get_playlist(dict_playlist['id'])
            
            list_playlist.append(new_list)
        
        return list_playlist

    def get_playlist_songs(self, playlist_id):
        result_songs = []
        
        Logger.log("Getting playlist %s" % str(playlist_id))
        with connection.cursor() as cursor:
            
            sql = "call get_playlist_songs(%s)"
            cursor.execute(sql, (str(playlist_id),))
            
            result_songs = cursor.fetchall()
        
        return result_songs

    def get_playlist(self, playlist_id):
        """ Given a playlist's id, return a musicEntities.Playlist object with a list of songs.+"""
        playlist = musicEntities.Playlist(int(playlist_id))
        
        result = None
        
        with connection.cursor() as cursor:
            sql = "select * from playlist where idplaylist = %s"
            cursor.execute(sql, (str(playlist_id),))
            
            result = cursor.fetchone()
        
        if not result:
            return None
        
        playlist.name = result['name']
        id_service = int(result['idservice'])
        playlist.service = musicEntities.supported_services[id_service]
        playlist.link = result['link']
        
        tracks = []
        
        result_songs = self.get_playlist_songs(playlist_id)
        
        for song in result_songs:
            new_song = convert_song(song)
            tracks.append(new_song)
        
        playlist.append(tracks)
            
    
    def delete_playlist(self, playlist_id):
        """ Given a playlist's id, delete it from the database."""
        
        with connection.cursor() as cursor:
            sql = "delete from playlist_song where idplaylist=%s"
            cursor.execute(sql, (str(playlist_id)))
        

def add_artist(the_artist):
    with connection.cursor() as cursor:
        sql = "insert into artist values(%s, %s, %s)"
        cursor.execute(sql, (the_artist.id, the_artist.name, the_artist.link))
    
    connection.commit()

def get_artist(artist_id):
    pass

def delete_artist(artist_id):
    pass

def add_album(the_album, the_artist = None):
    
    artst = the_artist
    
    if not artist_exists(artst.id):
        add_artist(artst)
    
    with connection.cursor() as cursor:
        sql = "insert into album values(%s, %s, %s)"
        cursor.execute(sql, (the_album.id, the_album.title, artst.id))
    
    connection.commit()

def get_album(album_id):
    pass

def delete_album(album_id):
    pass

def add_song(the_song, playlist_id = None):
    """ Register the song in the database."""
    Logger.log("Adding song %s to the database." % str(the_song.id))
    artst = servicesConnection.deezer_load_artist(the_song.id)
    albm = servicesConnection.deezer_load_album(the_song.id)
    
    if not album_exists(albm.id):
        add_album(albm, artst)    
    
    with connection.cursor() as cursor:
        sql = "insert into song values(%s, %s, %s, %s, %s, %s)"
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute(sql, (the_song.id, the_song.title, the_song.length,
                             now, albm.id, artst.id))
    
    if playlist_id:
        with connection.cursor() as cursor:
            sql = "insert into playlist_song value(%s, %s)"
            Logger.log("Linking the song %s the playlist " + str(playlist_id))
            
            cursor.execute(sql, (str(playlist_id), str(the_song.id)))
    
    connection.commit()


def get_song(song_id):
    """ Given a song's id, return a musicEntities.Song object."""
    pass

def delete_song(song_id):
    """ Given a song's id, delete it from the database."""
    
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM playlist_song WHERE idsong = %s"
            cursor.execute(sql, (song_id))
    except Exception as e:
        connection.rollback()
    else:
        connection.commit()    
    
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM song WHERE idsong=%s"
            cursor.execute(sql, (song_id))
    except Exception as e:
        connection.rollback()
    else:
        connection.commit()
        

def convert_song(the_song):
    new_song = musicEntities.Song()
    
    new_song.id = int(the_song['idsong'])
    new_song.title = the_song['name']
    new_song.artist = the_song['arname']
    new_song.album = the_song['alname']
    new_song.length = the_song['length']
    
    new_song.file = save_path + new_song.artist + ' - ' + new_song.title + '.mp3'
    
    return new_song
    

def artist_exists(artist):
    with connection.cursor() as cursor:
        sql = "select * from artist where idartist = %s"
        
        cursor.execute(sql, (str(artist),))
        result = cursor.fetchone()
        
    connection.commit()
    return bool(result)

def playlist_exists(playlist_id):
    with connection.cursor() as cursor:
        sql = "select * from playlist where idplaylist = %s"
        
        cursor.execute(sql, (str(playlist_id),))
        result = cursor.fetchone()
    
    connection.commit()
    return bool(result)

def album_exists(album):
    with connection.cursor() as cursor:
        sql = "select * from album where idalbum = %s"
        
        cursor.execute(sql, (str(album),))
        result = cursor.fetchone()
        
        
    connection.commit()
    return bool(result)

def song_exists(song):
    with connection.cursor() as cursor:
        sql = "select * from song where idsong = %s"
        
        cursor.execute(sql, (str(song),))
        result = cursor.fetchone()
        
        
    connection.commit()
    return bool(result)

def user_exists(usr):
    with connection.cursor() as cursor:
        sql = "select * from view_users where name = %s"
        
        cursor.execute(sql, (usr,))
        result = cursor.fetchone()
        
    connection.commit()
    return bool(result)

def signup(name, email, passw):
    try:
        with connection.cursor() as cursor:
            sql = "call add_user(%s, %s, %s)"
            
            cursor.execute(sql, (name, email, passw))
            
        connection.commit()
    except:
        pass
    
if __name__== '__main__':
    my_name = 'thirduser'
    my_email = '1234@ltt.com'
    my_pass = 'realsecurepass'
    
    singup(my_name, my_email)
    
    me = User(my_name, my_pass, my_email)
    
