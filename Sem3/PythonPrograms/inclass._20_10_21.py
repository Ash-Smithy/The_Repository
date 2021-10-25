class myError(Exception):
    def __init__(self,c):
        self.val=c
    def __str__(self):
        return repr(self.val)
try:
    raise myError(10)
except myError as e:
    print('USer defined exception generated with value: ', e.val)