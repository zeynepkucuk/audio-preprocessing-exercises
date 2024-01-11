import os
from pydub import AudioSegment
import glob
if not os.path.isdir("audio"):
    os.mkdir("audio")

#grab the audio files in "audio" directory

wavfiles = glob.glob("./audio/*.wav")
print(wavfiles)

# Loopting each file and include in Audio Segment
wavs = [AudioSegment.from_wav(wav) for wav in wavfiles]

combined = wavs[0]

#Appendin all the audio file
for wav in wavs[1:]:
    combined = combined.append(wav)


#export the merged audio file

combined.export("mergedaudio.wav", format = "wav")
