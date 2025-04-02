from pydub import AudioSegment

from pydub.playback import play

song = AudioSegment.from_wav('C:\\Users\\XHL\\Desktop\\q6koz-nckgy.wav')

play(song)
