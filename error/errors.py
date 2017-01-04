class KGError(Exception):
    def __init__(self, *, code='', msg='', info=[]):
        self.code = code
        self.msg = msg
        if len(info) == 2:
            self.code = info[0]
            self.msg = info[1]
