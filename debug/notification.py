import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def show(message):
    Notify.init("Song Downloader")
    
    # Create the notification object and show once
    notification = Notify.Notification.new("Song Downloader", message)
    Notify.Notification.new(message)
    
    notification.show()