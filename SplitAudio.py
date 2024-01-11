from pydub import AudioSegment
import os

if not os.path.isdir("splitaudio"):
    os.mkdir("splitaudio")


audio = AudioSegment.from_file("mergedaudio.wav")
lengtaudio = len(audio)
print("Length od Audio File", lengtaudio)

start = 0
threshold = 10000
end = 0
counter = 0

while start < len(audio):
    end += threshold
    print(start, end)

    chunk = audio[start:end]
    print(chunk)
    filename = f'splitaudio/chunk{counter}.wav'
    chunk.export(filename, format="wav")
    counter += 1
    start += threshold
