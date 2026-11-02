import json, subprocess, numpy as np, soundfile as sf
exec(open('/tmp/ph/audio/score.py').read().split('# 1. intro')[0].replace('DUR=51.0','DUR=45.0'))
durs=json.load(open('durs.json')); X=0.6
D=[max(4.4,v+1.15) for v in durs]; D[-1]+=1.6
offs=[]; o=0
for d in D: offs.append(o); o+=d-X
total=o+X
gal='/mnt/project-files/product-hunt/gallery'
files=['01-dashboard','02-browse','03-quarantine','04-sbom','05-ai-agents','06-vibe','07-backups','08-platform']
for i,(f,d) in enumerate(zip(files,D)):
    n=int(round(d*30))
    subprocess.run(['ffmpeg','-loglevel','error','-y','-loop','1','-i',f'{gal}/{f}.png','-vf',f"scale=2540:1520,pad=2702:1520:81:0:color=0xf8fafc,scale=3840:-2,zoompan=z='min(1+0.0005*on,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1920x1080:fps=30,format=yuv420p",'-frames:v',str(n),'-c:v','libx264','-crf','20',f's{i}.mp4'],check=True)
flt=''; prev='0'
for i in range(1,8):
    off=sum(D[:i])-X*i
    flt+=f"[{prev}][{i}]xfade=transition=fade:duration={X}:offset={off:.3f}[x{i}];"; prev=f'x{i}'
args=['ffmpeg','-loglevel','error','-y']
for i in range(8): args+=['-i',f's{i}.mp4']
subprocess.run(args+['-filter_complex',flt.rstrip(';'),'-map',f'[{prev}]','-c:v','libx264','-crf','20','-pix_fmt','yuv420p','video.mp4'],check=True)
# music: calm major bed with arps
Cc=[48,55,64,71];F=[41,53,57,64];Am=[45,52,60,67];G=[43,55,59,66]
up=lambda c:[n+24 for n in c]
prog=[Cc,F,Am,G]; bar=total/8
for b in range(8):
    ch=prog[b%4]; st=b*bar
    pad(ch,st,bar+0.8,0.4,bright=2.2,fi=0.8 if b==0 else 0.4,fo=0.6)
    k=0;t=st
    while t<st+bar-0.05: pluck(up(ch)[k%4],t,0.05,dec=0.4,pan=(-1)**k*0.4); k+=1; t+=0.42
for t in np.arange(0,total-2,60/100*2): kick(t,0.05)
for i in range(1,8): noise(offs[i]-0.3,0.7,0.05,lambda x:np.sin(np.pi*x)**2)
boom(offs[-1]+0.2,0.25,2.5)
music=np.stack([L,R],1)[:int(total*SR)]
# voice
voice=np.zeros(len(music))
for i in range(8):
    v,vsr=sf.read(f'v{i}.wav'); x=np.arange(int(len(v)*SR/vsr))/SR; v=np.interp(x,np.arange(len(v))/vsr,v)
    a=int((offs[i]+0.35)*SR); voice[a:a+len(v)]+=v[:len(voice)-a]
win=int(0.05*SR); act=np.convolve(np.abs(voice),np.ones(win)/win,'same')>0.01
act=np.convolve(act.astype(float),np.ones(int(0.4*SR))/int(0.4*SR),'same'); duck=1-0.45*np.clip(act*1.5,0,1)
mix=voice[:,None]*0.9+music/np.max(np.abs(music))*0.24*duck[:,None]
mix=mix/np.max(np.abs(mix))*0.95; f=int(1.2*SR); mix[-f:]*=np.linspace(1,0,f)[:,None]
sf.write('mix.wav',mix,SR); print(round(total,2), [round(x,2) for x in offs])
