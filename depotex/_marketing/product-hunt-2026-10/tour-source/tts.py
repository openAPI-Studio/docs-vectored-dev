import json, soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
k=Kokoro('/tmp/tts/kokoro.onnx','/tmp/tts/voices.bin')
out=[]
for i,t in enumerate(json.load(open('lines.json'))):
    s,sr=k.create(t,voice='am_michael',speed=1.05,lang='en-us')
    nz=np.where(np.abs(s)>0.01)[0]; s=s[max(0,nz[0]-240):nz[-1]+2400]
    sf.write(f'v{i}.wav',s,sr); out.append(len(s)/sr)
print(json.dumps(out)); json.dump(out,open('durs.json','w'))
