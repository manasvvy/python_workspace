#method overriding using multi level instance

from typing_extensions import override
class wa1:
    def msg(self):
        print("single tick")

class wa2(wa1):
    @override
    def msg(self):
        super().msg()
        print("double tick")

    def record_audio(self):    
        print("60 sec audio")

class wa3(wa2):
    @override
    def msg(self):
        super().msg()
        print("bluetick")

    @override
    def record_audio(self):
        super().record_audio()     
        print("business wa users get unlimited audio recording")      

    def gifs(self):
        print("gifs are sent")

w3=wa3()
w3.msg()
w3.record_audio()
w3.gifs()        

             