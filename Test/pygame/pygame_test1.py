# 引入扩展库
import os
import sys
import pygame


def move(event, key):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if key[pygame.K_RIGHT]:
        print("right")
    if key[pygame.K_LEFT]:
        print("left")
    if key[pygame.K_UP]:
        print("up")
    if key[pygame.K_DOWN]:
        print("down")
    # if key[pygame.K_q]:
    #     print("up")


path = "C://Users//XHL//Desktop//wav//"
song_list = []  # 歌曲列表


# 加载歌曲列表
def load_songs():
    songs = os.listdir(path)
    songs = [path + song for song in songs]
    song_list.extend(songs)
    for songss in song_list:
        print(songss)


def play(index):  # index当前歌曲的索引
    pygame.mixer.music.stop()
    # 播放音乐
    pygame.mixer.music.load(song_list[index])
    pygame.mixer.music.play()


indexs = 2
# 歌曲文件
file = r'C:\Users\XHL\Desktop\wav\「Memento Mori手游」英文版抒情诗合集（1080P⧸320K） p01 A.A. Ⅶ. THE RUST (Full Ver.).wav'
# 初始化pygame显示库
pygame.display.init()
# 打开一个窗口
screen = pygame.display.set_mode([200, 100])
# 初始化pygame声音库
pygame.mixer.init(frequency=44100)
print("播放音乐-绒花")
# 载入音乐文件
# pygame.mixer.music.load(file)
load_songs()
play(indexs)
# 保存当前音量
v = pygame.mixer.music.get_volume()
print(v)
# 设置为静音，防止开始的爆破音
pygame.mixer.music.set_volume(0)
# 播放声音
# pygame.mixer.music.play()
# pygame.mixer.music.queue(
#     r'C:\Users\XHL\Desktop\wav\「Memento Mori手游」英文版抒情诗合集（1080P⧸320K） p02 A.A. Ⅶ. THE RUST (Full Ver.).wav')
# pygame.mixer.music.queue(r'C:\Users\XHL\Desktop\wav\「Memento Mori手游」英文版抒情诗合集（1080P⧸320K） p03 Natasha X. THE '
#                          r'FLOWER (Special Ver.).wav')
# 延时0.2秒打开声音，避过爆破音
pygame.time.delay(200)
pygame.mixer.music.set_volume(v)
# 自定义一条消息(一个事件)用于表示播放结束
# pygame.USEREVENT是pygame中预定义的用户消息起始值

MUSIC_END = pygame.USEREVENT + 1
MUSIC_START = pygame.USEREVENT + 2
# 设置当前音乐播放完成后，发送自定义的消息
pygame.mixer.music.set_endevent(MUSIC_END)

# 定义一个退出程序标志
requireQuit = False
# 程序主循环
while not requireQuit:
    # 循环接受各种事件
    pos = pygame.mixer.music.get_pos()
    for event in pygame.event.get():
        # 如果是自定义的播放完成消息
        if event.type == MUSIC_END:
            if indexs < 6:
                indexs += 1
                # pygame.mixer.music.queue(song_list[indexs])
                print(indexs)
                # print(pygame.mixer.music.get_endevent())
                pygame.mixer.music.set_endevent(MUSIC_START)
                print(pygame.mixer.music.get_endevent())
                play(indexs)
                pygame.time.delay(200)
                pygame.mixer.music.set_endevent(MUSIC_END)
            # else:
            #     requireQuit = True  # 退出
            #     break
        # 界面窗口菜单关闭申请
        elif event.type == pygame.QUIT:
            requireQuit = True
            break
        # 有键盘抬起
        elif event.type == pygame.KEYUP:
            # q键
            if event.key == pygame.K_q:
                requireQuit = True
                break
            elif event.key == pygame.K_LEFT:
                pygame.mixer.music.set_pos(pos / 1000 - 10)
            # 如果是向左键，则后跳10秒
            elif event.key == pygame.K_RIGHT:
                pygame.mixer.music.set_pos(pos / 1000 + 10)
        if event.type == pygame.KEYUP:
            # q键
            if event.key == pygame.K_k:
                pygame.mixer.music.pause()
        if event.type == pygame.KEYUP:
            # q键
            if event.key == pygame.K_l:
                pygame.mixer.music.unpause()
    if not pygame.mixer.music.get_busy():
        print("Playlist completed")

        # When the playlist has
        # completed playing successfully
        # we'll go out of the
        # while-loop by using break
        requireQuit = True
        break
    # # 显示
    # print("Playing:", pos, end='')
# while 1:
#     for event in pygame.event.get():
#         key = pygame.key.get_pressed()
#     move(event, key)
#     pygame.display.update()
# ... 退出操作 ...

# while 1:
#     pass
