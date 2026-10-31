import numpy as np, wave
SR=44100; DUR=51.0; N=int(SR*DUR)
L=np.zeros(N); R=np.zeros(N)
rng=np.random.default_rng(3)
def hz(n): return 440*2**((n-69)/12)
def env(n,a,d,s=0.0):  # attack, exponential decay
    t=np.arange(n)/SR; e=np.minimum(1,t/max(a,1e-4))*np.exp(-t/d) if s==0 else np.minimum(1,t/max(a,1e-4))
    return e
def tone(f,dur,harm=6,roll=1.6,det=0.0):
    t=np.arange(int(dur*SR))/SR; y=np.zeros_like(t)
    for k in range(1,harm+1):
        y+=np.sin(2*np.pi*f*k*t*(1+det*(k%2)))/k**roll
    return y
def add(y,start,gain=1.0,pan=0.0):
    i=int(start*SR); j=min(N,i+len(y)); y=y[:j-i]*gain
    L[i:j]+=y*np.sqrt((1-pan)/2); R[i:j]+=y*np.sqrt((1+pan)/2)
def fade(y,fi,fo):
    n=len(y); a=np.ones(n); fi=int(fi*SR); fo=int(fo*SR)
    if fi: a[:fi]=np.linspace(0,1,fi)
    if fo: a[-fo:]*=np.linspace(1,0,fo)
    return y*a
def pad(notes,start,dur,gain,bright=2.2,fi=1.5,fo=1.5):
    for i,n in enumerate(notes):
        y=tone(hz(n),dur,harm=5,roll=bright,det=0.0015)+tone(hz(n)*1.003,dur,harm=4,roll=bright)
        lfo=1+0.15*np.sin(2*np.pi*0.2*np.arange(len(y))/SR+i)
        add(fade(y*lfo,fi,fo),start,gain/len(notes),pan=(i/(len(notes)-1)-0.5)*0.8 if len(notes)>1 else 0)
def pluck(n,start,gain,dec=0.35,pan=0):
    y=tone(hz(n),dec*4,harm=8,roll=1.3)*env(int(dec*4*SR),0.003,dec); add(y,start,gain,pan)
def bell(n,start,gain,pan=0):
    d=2.5; t=np.arange(int(d*SR))/SR
    y=(np.sin(2*np.pi*hz(n)*t)+0.5*np.sin(2*np.pi*hz(n)*2.76*t)*np.exp(-t/0.4)+0.3*np.sin(2*np.pi*hz(n)*5.4*t)*np.exp(-t/0.2))*env(len(t),0.002,0.8)
    add(y,start,gain,pan)
def kick(start,gain):
    d=0.5; t=np.arange(int(d*SR))/SR; f=50+90*np.exp(-t/0.04)
    y=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t/0.15); add(y,start,gain)
def noise(start,dur,gain,shape):
    n=int(dur*SR); y=rng.standard_normal(n)
    y=np.convolve(np.convolve(y,np.ones(24)/24,'same'),np.ones(24)/24,'same')*4*shape(np.linspace(0,1,n)); add(y,start,gain,pan=0)
    add(rng.standard_normal(n)*0.0,start,0)
def glitch(start,gain):
    d=0.35; n=int(d*SR); t=np.arange(n)/SR
    y=np.sign(np.sin(2*np.pi*(180+rng.random()*120)*t))*(rng.random(n)>0.3)*np.exp(-t/0.08)
    y+=np.convolve(rng.standard_normal(n),np.ones(12)/12,'same')*np.exp(-t/0.05)*1.2
    add(y,start,gain,pan=rng.uniform(-.6,.6)); kick(start,gain*1.4)
def boom(start,gain,dec=2.5):
    d=dec*2; t=np.arange(int(d*SR))/SR; f=40+60*np.exp(-t/0.08)
    y=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t/dec*1.5); add(y,start,gain)
    noise(start,1.2,gain*0.25,lambda x:np.exp(-x*6))

# 1. intro 0-7.5: airy A minor 9
pad([57,64,67,71,76],0,8.4,0.5,fi=2.5,fo=1.6)
for i,n in enumerate([76,79,83,81, 76,79,84,83, 76,79,83,86]):
    pluck(n,1.2+i*0.5,0.10,dec=0.4,pan=(-1)**i*0.4)
# 2. problems 7.2-20: D minor drone + pulse bass, tension
pad([38,45,50,53,57],7.0,13.6,0.55,bright=1.8,fi=1.0,fo=1.2)
bpm=100; step=60/bpm/2
t=7.2
while t<20.0:
    pluck(26 if int((t-7.2)/step)%8<6 else 29,t,0.32,dec=0.18); t+=step
for t in np.arange(8.4,20,60/bpm*2): kick(t,0.35)
for k,t in enumerate([8.4,10.3,12.2,14.1,16.0]):
    glitch(t,0.22); pluck([62,65,63,61,60][k],t+0.05,0.12,dec=0.6)
# 3. build + "shipping without a safety net" 19.5-24
noise(19.6,4.2,0.18,lambda x:x**2.5)
pad([37,44,49,52],19.8,4.0,0.45,bright=1.5,fi=0.4,fo=0.6)
boom(20.0,0.6,2.0)
# 4. fix 24-38.5: C major lift, arpeggios
boom(24.0,0.75,2.8); bell(84,24.0,0.12)
prog=[([48,55,60,64,67],[72,76,79,84]),([53,57,60,65,69],[72,77,81,84]),([45,52,57,60,64],[69,72,76,81]),([55,59,62,67,71],[74,79,83,86])]
bar=60/110*4
for b in range(4):
    st=24.0+b*bar*1.0+ (0 if b==0 else 0)
for b in range(int((38.6-24)/bar)+1):
    chord,arp=prog[b%4]; st=24.0+b*bar
    if st>38.6: break
    pad(chord,st,bar+0.6,0.42,bright=2.0,fi=0.3,fo=0.5)
    for i in range(8):
        tt=st+i*bar/8
        if tt<38.5 and tt>=25.2: pluck(arp[i%4],tt,0.09,dec=0.3,pan=(-1)**i*0.5)
    for i in range(4):
        tt=st+i*bar/4
        if 25.2<=tt<38.0: kick(tt,0.22)
for k,t in enumerate([28,29.7,31.4,33.1,34.8]): bell([79,81,83,84,88][k],t,0.16,pan=0.3)
# 5. screenshot 38.5-45.5 soft
pad([48,55,62,64,71],38.3,7.6,0.42,bright=2.4,fi=1.2,fo=1.4)
for i,n in enumerate([76,79,83,79,76,74,76,79,83,86,84,83]): pluck(n,38.8+i*0.55,0.07,dec=0.5,pan=(-1)**i*0.4)
# 6. logo 45-51
noise(43.6,2.4,0.10,lambda x:x**3)
boom(46.2,0.7,3.0)
pad([36,48,55,60,64,67,71,74],46.2,4.8,0.65,bright=2.0,fi=0.05,fo=3.0)
for n in [84,88,91,96]: bell(n,46.2+0.08*[84,88,91,96].index(n),0.10)
# simple reverb: multi-tap delays
def verb(x):
    y=x.copy()
    for d,g in [(0.029,.35),(0.037,.3),(0.053,.25),(0.079,.22),(0.113,.18),(0.167,.14),(0.241,.1),(0.353,.07)]:
        k=int(d*SR); y[k:]+=x[:-k]*g
    return y
L2=verb(L)+0.15*verb(R); R2=verb(R)+0.15*verb(L)
m=np.max(np.abs(np.stack([L2,R2])))
out=np.stack([L2,R2],1)/m*0.89
out=np.tanh(out*1.3)/np.tanh(1.3)
fo=int(1.0*SR); out[-fo:]*=np.linspace(1,0,fo)[:,None]
w=wave.open('/tmp/ph/audio/score.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out*32767).astype('<i2').tobytes()); w.close(); print('ok')
