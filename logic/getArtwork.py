from dataAccess.servicesConnection import deezer_load_track

def seek_artwork(song):
    d_song = deezer_load_track(song.id)
    d_album = d_song.get_album()
    #d_image = d_album.
    from os import system
    
    art_path = "~/Music/artworks/"
    file = None
    try:
        file = open(art_path, 'r')
    except:
        file = open(art_path, 'w')
        file.close()
    
    system("wget " + d_image + " " + art_path)