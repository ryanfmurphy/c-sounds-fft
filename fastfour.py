import numpy as np
import sys
import matplotlib.pyplot as plt
'''
def arr_from_stdin(chunk_size)
    data = sys.stdin.read(chunk_size)
    arr = np.frombuffer(data,dtype=np.uint8)
    if arr.shape != (chunk_size,):
      raise IOError("not enough bytes for a chunk")
    return arr
'''

chunk_size = 128*1024
nbins = 128

#with open('funsounds.wav','rb') as fh:
if True:
    data = sys.stdin.read(chunk_size)
    arr = np.frombuffer(data,dtype=np.uint8)
    bins = np.fft.fft(arr,n=nbins)
    plt.plot(bins)
    sys.stdout.write(data)
    plt.show()

