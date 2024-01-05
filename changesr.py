import os
import numpy as np
import librosa
from scipy.io.wavfile import write
from pydub import AudioSegment


from Libraries.resemblyzer.audio import preprocess_wav

def trim_silence_with_normalization(sound_path, save_path, percentage):

    for root, people, _ in os.walk(sound_path):
        length = len(people)
        for index in range(length):
            person = people[index]
            print(person)
            os.makedirs(os.path.join(save_path, person), exist_ok=True)
            for person_root, _, sound_files in os.walk(os.path.join(root, person)):
                length = len([x for x in sound_files if
                              x.lower().endswith(".wav") or x.lower().endswith(".mp3") or x.lower().endswith(
                                  ".flac")])
                print(length)
                rate = int(length * percentage / 100)
                count = 0
                for sound_file in (x for x in sound_files if
                                   x.lower().endswith(".wav") or x.lower().endswith(".mp3") or x.lower().endswith(
                                       ".flac")):
                    try:
                        audioFilePath = os.path.join(person_root, sound_file)
                        y, sr = librosa.load(audioFilePath, sr=None)
                        #audio = preprocess_wav(fpath_or_wav=audioFilePath, samplingRate=sr)


                        #Change Sample Rate
                        #audio = librosa.core.resample(y, sr, 16000)
                        #whitenoise

                        sound = AudioSegment.from_file(audioFilePath)

                        sound = sound.set_frame_rate(16000)
                        print(sr)

                        ''''

                        noise_factor = 0.001
                        mean = 0
                        std = 1
                        audio = audio + noise_factor * np.random.normal(mean, std, len(audio))

                        #adding noise
                        noise, sr = librosa.load('/Users/app/Downloads/noise.wav', sr= None)

                        if len(audio) >= len(noise):
                            while len(audio) >= len(noise):
                                noise = np.append(noise, noise)
                        # uzatılan ikinci ses verisi birinci ses verisi ile eşit uzunluğa getirilir.
                        sound2_cropped = noise[0: len(audio)]

                        # iki sesin overlap işlemleri
                        sound1_power = np.sum(audio ** 2) #4 e 2 dene
                        sound2_power = np.sum(sound2_cropped ** 2)
                        audio = audio + np.sqrt(sound1_power / sound2_power) * sound2_cropped
                        '''
                        '''
                        #Short Time Fourier Transform
                        SPEECH_LOW_BAND = 200
                        SPEECH_UPPER_BAND = 3400

                        short_time_fourier_transform = librosa.core.stft(y=audio)

                        # Clear out speech bands
                        # TODO(jonluca) is there a better way of doing this? Feels hacky
                        short_time_fourier_transform[:SPEECH_LOW_BAND] = 0
                        short_time_fourier_transform[SPEECH_UPPER_BAND: len(short_time_fourier_transform)] = 0
                        reconstructed_time_series = librosa.core.istft(short_time_fourier_transform)
                        '''


                        #export audio to file
                        sound.export(os.path.join(save_path, person, sound_file), format="wav")

                        #write(os.path.join(save_path, person, sound_file), sr, sound)
                        count += 1

                    except Exception as e:
                        print("\nError: ", e)
                        print("person: {0}, filename: {1}".format(person_root, sound_file))
                        y, sr = librosa.load(audioFilePath, sr=None)
                        print("duration: {0}".format(librosa.get_duration(y=y, sr=sr)))


trim_silence_with_normalization(sound_path="/Users/app/Downloads/clean_wav_files/",save_path="/Users/app/Downloads/clean_wav_files_changedSR/", percentage=100)



