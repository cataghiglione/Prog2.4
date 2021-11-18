

class NoExiste(Exception):
    def __init__(self, msg):
        self.msg = msg
    def mensaje(self):
        return self.msg
