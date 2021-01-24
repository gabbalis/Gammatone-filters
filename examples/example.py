import numpy as np
import matplotlib.pyplot as plt
from GTF import GTF
# from BasicTools import wav_tools

import os
import soundfile as sf

fig_dir = os.path.join('output','images','example' )
if not os.path.exists(fig_dir):
    os.makedirs(fig_dir)

def read_wav(wav_path, tar_fs=None):
    """ read wav file, implete with soundfile
    """
    wav_path = os.path.expanduser(wav_path)
    x, fs = sf.read(wav_path)
    if tar_fs is not None and tar_fs != fs:
        x = resample(x, fs, tar_fs)
        fs = tar_fs
    return [x.astype(np.float32), fs]


def main():

    wav, fs = read_wav('record.wav')
    gt_filter = GTF(fs, freq_low=80, freq_high=5e3, n_band=32)
    # wav_band_all_py = gt_filter.filter_py(wav)
    # np.save('wav_band_all_py.npy', wav_band_all_py)
    # wav_band_all_py = np.load('wav_band_all_py.npy')
    # print(np.max(wav_band_all_py))

    wav_band_all = gt_filter.filter(wav)
    print(np.max(wav_band_all))

    # print(wav_band_all)
    # print(wav_band_all[0, :, 0].T)
    for band_i in range(32):
        fig, ax = plt.subplots(2, 1)
        print('ax0 ' + str(ax[0]))
        ax[0].plot(wav_band_all[band_i, :, 0].T)
        # ax[0].plot(wav_band_all_py[band_i, :, 0].T)
        ax[0].set_xlim([5000, 5050])

        # ax[1].plot(wav_band_all_py[band_i, :, 0].T)
        ax[1].plot(wav_band_all[band_i, :, 0].T)
        ax[1].set_xlim([5000, 5050])

        fig.savefig( os.path.join(fig_dir, 'eg_'+str(band_i)+'.png'))
        plt.close(fig)


if __name__ == "__main__":
    main()
