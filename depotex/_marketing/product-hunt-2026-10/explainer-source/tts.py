import json, soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
k=Kokoro('/tmp/tts/kokoro.onnx','/tmp/tts/voices.bin')
lines=json.load(open('script.json')); SR=24000
out=[]; t=1.2; timeline=[]; prev=None
audio=[np.zeros(int(1.2*SR))]
for i,(scene,text) in enumerate(lines):
    gap=0.9 if (prev and scene!=prev) else 0.35
    if i==0: gap=0
    if scene=='logo': gap=1.6
    audio.append(np.zeros(int(gap*SR))); t+=gap
    s,sr=k.create(text,voice='am_michael',speed=0.98,lang='en-us'); assert sr==SR
    # trim silence
    nz=np.where(np.abs(s)>0.01)[0]; s=s[max(0,nz[0]-240):nz[-1]+2400]
    timeline.append({"scene":scene,"text":text,"start":round(t,3),"end":round(t+len(s)/SR,3)})
    audio.append(s); t+=len(s)/SR; prev=scene
audio.append(np.zeros(int(3.5*SR))); t+=3.5
a=np.concatenate(audio); sf.write('voice.wav',a,SR)
json.dump({"duration":round(t,3),"lines":timeline},open('timeline.json','w'),indent=1)
print(round(t,2))
