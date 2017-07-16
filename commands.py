import os
import sys
import json
import time
import loadUI

project_path = '/home/louis_/Documents/Python/Projects/DeezerConnection/'
config_file = 'config.json'

def save_config(config):

    var_s = ['running', 'download', 'delete', 'paused']
    to_save = {}
    for x in var_s:
        to_save[x] = config[x]

    with open(project_path + config_file, 'w') as file:
        js = json.dumps(to_save)
        file.write(js)

def load_config():
    with open(project_path + config_file, 'r') as fl:
        return json.loads(fl.read())


def change_config(var, val):
    con = load_config()
    con[var] = val
    save_config(con)

def stop():
    change_config('running', False)

def start():
    os.system('python3 ' + project_path + 'mainConnection.py & disown')

def restart():
    stop()

def pause():
    change_config('paused', True)

def continue_():
    change_config('paused', False)

def addPlaylist():
    print('adding')
    loadUI.add_playlist()
def removePlaylist():
    print('removing')
    loadUI.delete_playlist()

comm = {'0': start, '1': stop, '2': restart, '3': pause, '4': continue_}

if __name__ == '__main__':
    try:
        comm[sys.argv[1]]()
    except KeyError as e:
        print("The command '" + sys.argv[1] + "' is not valid.\n", 
              "Available commands: ")
        
        
        for x in comm.keys():
            print(x + " " + str(comm[x].__name__))
