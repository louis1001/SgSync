from __future__ import unicode_literals
import urllib
from bs4 import BeautifulSoup
import youtube_dl
import sys
from debug.logger import Logger

working_dir = sys.path[0]

save_path = '/home/louis_/Music/'

_search_prefix = "https://www.youtube.com/results?search_query="

_video_prefix = 'https://www.youtube.com//watch?v='

def is_ascii(st):
    try:
        st.encode('ascii')
    except:
        return False
    else:
        return True

def format_query(*args):
    good_query = ""
    
    for a in args:
        b = a.lower()
        x = ""
        for y in b:
            if is_ascii(y):
                x += y
        x = x.replace(' ', '+')
        good_query += x + '+'
    
    return good_query
    
    # print("Good Query\n" + good_query)

def download_audio(artist, song, video_id = None):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': u'/home/louis_/Music/'+ artist + ' - ' + song+'.%(ext)s'
    }

    try:
        open(save_path + artist + ' - ' + song +'.mp3', 'r')
    except:
        pass
    else:
        return True
    
    if not video_id:
        video_id = get_videos(artist, song)[0]
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            Logger.log("Downloading the audio for " + song + " with video id " + video_id)
            ydl.download(['http://www.youtube.com/watch?v=' + video_id])
            return True
    except youtube_dl.DownloadError as e:
        Logger.log("Error downloading " + song + " - " + video_id)
        return False

def get_videos(*textToSearch):
    Logger.log("Getting youtube links for " + textToSearch[1])
    
    good_query = format_query(*textToSearch) + "official+lyrics"
    url = _search_prefix + good_query
    response = urllib.request.urlopen(url)
    flhtml = response.read()
    soup = BeautifulSoup(flhtml, "lxml")
    
    vids = []
    
    parsed_html = soup.findAll(attrs={'class':'yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix'})
    
    for vid in parsed_html:
        vids.append(vid['data-context-item-id'])
    
    return vids
    
if __name__ == '__main__':
    
    print('Builded')
    
