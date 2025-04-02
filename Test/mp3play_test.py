import mp3play
import time

# 需要PY2
# filename = u"D:\\music.mp3"
filename = u"C:\\Users\\XHL\\Desktop\\q6koz-nckgy.wav"
clipss = mp3play.load(filename)
clipss.play()
duration = clipss.milliseconds()  # 返回mp3文件共多少毫秒，注意这里的单位是毫秒

time.sleep(duration)  # 现在就可以在后台播放完整的mp3了
clipss.stop()
