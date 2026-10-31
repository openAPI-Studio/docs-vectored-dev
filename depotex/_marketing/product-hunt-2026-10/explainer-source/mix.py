import numpy as np, json, wave, soundfile as sf
exec(open('/tmp/ph/audio/score.py').read().split('# 1. intro')[0].replace('DUR=51.0','DUR=128.0'))
tl=json.load(open('tl.json')); sc={s['id']:s for s in tl['scenes']}
st=lambda k:sc[k]['start']; en=lambda k:sc[k]['end']
def bed(chords,a,b,gain,bright=2.2,arp=True,rate=0.5,arpg=0.05):
    n=len(chords); seg=(b-a)/n
    for i,(ch,ar) in enumerate(chords):
        pad(ch,a+i*seg,seg+0.8,gain,bright=bright,fi=0.8,fo=0.8)
        if arp:
            k=0; t=a+i*seg
            while t<a+(i+1)*seg-0.1:
                pluck(ar[k%len(ar)],t,arpg,dec=0.45,pan=(-1)**k*0.4); k+=1; t+=rate
C=[48,55,64,71];F=[41,53,57,64];Am=[45,52,60,67];G=[43,55,59,66]
Dm=[38,50,53,57];Bb=[46,53,58,62];A7=[45,52,55,61];Gm=[43,50,55,58]
up=lambda c:[n+24 for n in c]
bed([(C,up(C)),(F,up(F)),(Am,up(Am)),(G,up(G))]*2,0,st('crack'),0.38)
bed([(Dm,[62,65,69,72]),(Bb,[62,65,70,74]),(Gm,[62,67,70,74]),(A7,[61,64,69,73])]*3,st('crack'),st('rope'),0.36,bright=1.9,rate=0.75,arpg=0.035)
for t in np.arange(st('secret'),st('rope'),60/76): pluck(26,t,0.10,dec=0.3)
pad([38,45,49,52,56],st('rope'),en('rope')+0.6,0.4,bright=1.6,fi=0.3,fo=0.6)
noise(st('rope')+0.5,2.8,0.06,lambda x:x**2)
boom(st('depot')+0.2,0.4,2.2)
bed([(F,up(F)),(C,up(C)),(G,up(G)),(Am,up(Am))]*4,st('depot'),st('logo'),0.38,rate=0.42,arpg=0.05)
for t in np.arange(st('checkin'),st('outro'),60/96*2): kick(t,0.08)
boom(st('logo')+0.2,0.45,3.0); pad([36,48,55,60,64,67,71,74],st('logo')+0.2,5.2,0.5,bright=2.0,fi=0.05,fo=3.0)
for i,n in enumerate([84,88,91,96]): bell(n,st('logo')+0.2+0.08*i,0.07)
music=np.stack([L,R],1).copy()
# SFX bus
L[:]=0;R[:]=0
def blip(t,n=84,g=0.12): pluck(n,t,g,dec=0.12)
def whoosh(t,g=0.06): noise(t,0.6,g,lambda x:np.sin(np.pi*x)**2)
def ding(t,g=0.10): bell(91,t,g)
def buzz(t,g=0.10):
    d=0.35;n=int(d*SR);tt=np.arange(n)/SR;y=np.sign(np.sin(2*np.pi*110*tt))*np.exp(-tt/0.15)*0.6;add(np.convolve(y,np.ones(20)/20,'same'),t,g)
a=st('intro'); [blip(a+x,n) for x,n in [(0.2,79),(0.6,84),(0.9,88),(2.6,76),(8.3,86),(9.6,91)]]
for i in range(12): whoosh(a+3+i*0.72,0.03)
a=st('world'); [blip(a+0.9+i*0.3,84+(i%5)*2,0.05) for i in range(12)]; blip(a+2.2,79); whoosh(a+5.3)
a=st('crack'); [blip(a+1.9+i*0.22,86,0.05) for i in range(9)]; glitch(a+3.2,0.08)
a=st('secret'); whoosh(a); ding(a+1.4,0.08); whoosh(a+3.6,0.05)
a=st('package'); [blip(a+x,81) for x in (0.3,2.0,4.6)]; kick(a+7.75,0.4); glitch(a+8.6,0.1)
a=st('hidden'); whoosh(a+2.2); glitch(a+6.0,0.08)
a=st('broken'); [kick(a+2.3+i*0.12,0.18) for i in range(6)]; whoosh(a+4.4); [blip(a+7.2+i*0.35,90,0.03) for i in range(9)]
a=st('depot'); whoosh(a+0.1,0.06); blip(a+3.0,84); blip(a+3.3,88); blip(a+3.6,91)
a=st('checkin'); [ (whoosh(a+x,0.04), blip(a+x+0.85,86+i*2)) for i,x in enumerate((2.6,3.7,4.9,6.2))]; kick(a+7.6,0.3); ding(a+7.9,0.08)
a=st('gate'); reach=(900-40)/380
ding(a+0.2+reach); buzz(a+1.9+reach); buzz(a+3.6+reach); ding(a+6.6+reach); blip(a+7.9+reach,76,0.15); blip(a+7.9+reach+0.1,72,0.15)
a=st('rollback'); [blip(a+0.6+i*0.25,86+i*2) for i in range(4)]; buzz(a+2.4); ding(a+3.8); whoosh(a+5.6); blip(a+7.4,91)
a=st('mcp'); [blip(a+6.5+i*0.25,86+i*2) for i in range(3)]; [blip(a+6.6+i*0.85,79,0.06) for i in range(3)]
a=st('outro'); ding(a+1.6,0.1); noise(a+1.8,1.2,0.04,lambda x:np.exp(-x*4))
sfx=np.stack([L,R],1).copy()
v,vsr=sf.read('voice.wav'); x=np.arange(int(len(v)*SR/vsr))/SR; v=np.interp(x,np.arange(len(v))/vsr,v)
n=min(N,len(v)); voice=np.zeros(N); voice[:n]=v[:n]
# ducking envelope from voice activity
win=int(0.05*SR); act=np.convolve(np.abs(voice),np.ones(win)/win,'same')>0.01
act=np.convolve(act.astype(float),np.ones(int(0.4*SR))/int(0.4*SR),'same'); duck=1-0.45*np.clip(act*1.5,0,1)
def norm(x): return x/np.max(np.abs(x))
mix=voice[:,None]*0.9*np.ones((1,2)) + norm(music)*0.22*duck[:,None] + norm(sfx)*0.20
mix=mix/np.max(np.abs(mix))*0.95
mix[-int(SR):]*=np.linspace(1,0,int(SR))[:,None]
sf.write('mix.wav',mix,SR); print('ok')
