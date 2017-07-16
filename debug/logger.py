import datetime
import os

class Logger:
    
    log_path = '/home/louis_/Documents/Python/Projects/DeezerConnection/debug/'
    log_file = ("/" if not log_path.endswith('/') else "") + 'log.txt'
    def log(mssg, console = True):
        if not os.path.exists(Logger.log_path):
            Logger.create_log()
        if not os.path.exists(Logger.log_path + Logger.log_file):
            Logger.create_file()
        
        with open(Logger.log_path + Logger.log_file, 'a') as fl:
            now = datetime.datetime.now()
            
            log_time =  (""if now.day > 9 else "0") + str(now.day) +"/" +(""if now.month > 9 else "0") + str(now.month)+ "/"+ str(now.year) + " "+ (
                    ""if now.hour > 9 else "0") + str(now.hour) +":" + (""if now.minute > 9 else "0") +  str(now.minute) + ":" + (
                        "" if now.second > 9 else "0") + str(now.second)
            output_message = "[" + log_time + "]\t\t" + mssg + ("." if mssg[-1] != '.' else "") + "\n"
            
            fl.write(output_message)
            
            if console:
                print(output_message)
    def create_log():
        os.system('mkdir ' + Logger.log_path)
    
    def create_file():
        os.system('touch '+ Logger.log_path + Logger.log_file)

if __name__ == '__main__':
    Logger.log("Printing something!")