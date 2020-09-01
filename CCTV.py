class CameraNode :
    def __init__(self):
        print('init')
        super().__init__()

    def __new__(cls):
        print('new')
        return super().__new__(cls)
        
    def setNumber(self,number):
        self.number = number
    
    def getNumber(self):

        return self._number
