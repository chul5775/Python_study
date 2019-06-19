'''--------------------------------------------------------------
---------------------- Singer type의 클래스 생성 ----------------------
--------------------------------------------------------------'''

class Singer:
    title_song = '아~대한민국'
    
    def sing(self):
        msg='노래는'
        print(msg, self.title_song)
        
red_velvet = Singer()
red_velvet.sing()
red_velvet.title_song = '빨간맛'

red_velvet.sing()
red_velvet.co = 'SM'
print('소속사:', red_velvet.co)

print()
twice = Singer()
twice.sing()
twice.co = 'jyp'
print('소속사', twice.co)