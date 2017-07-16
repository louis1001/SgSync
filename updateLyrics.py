from dataAccess import dbConnection
from dataAccess import dataAccess

the_lists = dataAccess.load_songs()

my_user = 'louis_'

my_pass = 'louiS0712'

me = dbConnection.User(my_user, my_pass)

for playlist in the_lists:
    me.add_playlist(playlist)
