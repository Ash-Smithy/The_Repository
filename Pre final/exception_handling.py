class myError(Exception):
    def __init__(self,val):
        self.val = val
    def __str__(self):
        return repr(self.val)
try:
    raise myError(10)
except myError as e:
    print("user defined exception generated with value : ",e.val)
