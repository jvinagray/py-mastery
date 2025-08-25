import datetime

class LogFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, 'a')
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.write(f"[{datetime.datetime.now()}] Closed log\n")
        self.file.close()