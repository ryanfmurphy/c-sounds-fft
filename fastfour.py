import numpy as np
with open('funsounds.wav','rb') as fh:
    data = fh.read()
    arr = np.frombuffer(data,dtype=np.uint8)

