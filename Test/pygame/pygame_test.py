import time
import pygame

file = r'C:\Users\XHL\Desktop\wav\「Memento Mori手游」英文版抒情诗合集（1080P⧸320K） p01 A.A. Ⅶ. THE RUST (Full Ver.).wav'
pygame.mixer.init()
musictest = pygame.mixer.Sound('C:\\Users\\XHL\\Desktop\\wav\\「Memento Mori手游」英文版抒情诗合集（1080P⧸320K） p01 A.A. Ⅶ. THE '
                               'RUST (Full Ver.).wav')
print('正在播放', musictest)
# pygame.mixer.music.load(file)
# pygame.mixer.music.play(loops=15, fade_ms=0)
# musictest.replace()
# time.sleep(130)
print(musictest.get_length())
musictest.play()
time.sleep(musictest.get_length())
# while 1:
#     print(pygame.mixer.music.get_pos())
#     print(pygame.mixer.get_busy())
#     time.sleep(5)
#     pass
# pygame.mixer.music.stop()

