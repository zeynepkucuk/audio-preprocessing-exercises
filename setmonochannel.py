import wave

import librosa
import numpy as np
import os

def run():

        dir = '/Users/app/Desktop/IVRP/wavfile/'
        file_names = []
        channel = 0
        for root_dir, subdir_list, file_list in os.walk(dir):
            for file_name in file_list:
                if os.path.splitext(file_name)[1].lower() == '.wav':
                    full_path = os.path.join(root_dir, file_name)

                    file_names.append(full_path)
                    for fname in file_names:
                        try:

                            wav = wave.open(fname)

                            fn = fname.split('.')[0] + '_mono.wav'

                            nch = wav.getnchannels()
                            depth = wav.getsampwidth()
                            wav.setpos(0)
                            sdata = wav.readframes(wav.getnframes())
                            typ = {1: np.uint8, 2: np.uint16, 4: np.uint32}.get(depth)
                            if not typ:
                                raise ValueError("sample width {} not supported".format(depth))
                            if channel >= nch:
                                raise ValueError("cannot extract channel {} out of {}".format(channel + 1, nch))
                            print("Extracting channel {} out of {} channels, {}-bit depth".format(channel + 1, nch,
                                                                                                  depth * 8))
                            data = np.fromstring(sdata, dtype=typ)
                            ch_data = data[channel::nch]

                            outwav = wave.open(fn, 'w')
                            outwav.setparams(wav.getparams())
                            outwav.setnchannels(1)
                            outwav.writeframes(ch_data.tostring())
                            outwav.close()
                            print("done")
                        except:

                            print('Error occurred while reading "%s" wav file' % fname)

run()








