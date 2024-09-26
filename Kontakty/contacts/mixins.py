from datetime import datetime



class LoggingMixin:
    def log_action(self, action):
        #print(f"{action} action performed at {datetime.now()}")
        with open('media/file/test.txt', 'a', ) as f:
            f.write(f"{action} action performed at {datetime.now()}\n")

