supported_services = ["deezer"]
class Song:
    def __init__(self, id, service='Unknown',
                 title='Unkown',artist='Unknown',
                 length='Unknown', date='Unknown',
                 added = '', album='Unknown', cover = 'Unknown',
                 file = ''):
        self.id = id
        if service in supported_services:
            self.service = service
        
        self.title = title
        self.service = service
        self.artist = artist
        self.length = length
        self.date = date
        self.added = added
        self.album = album
        self.file = file

class Playlist:
    def __init__(self, id, service='', name='', tracks = [], link = ''):
        self.id = id
        if service in supported_services:
            self.service = service
        else:
            if service:
                raise ValueError(service + ' is not a valid or compatible service.')
        self.name = name
        self.tracks = tracks
        self.link = link

if __name__ == '__main__':
    pass