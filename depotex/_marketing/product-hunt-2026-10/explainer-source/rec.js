const { chromium } = require('playwright');
(async()=>{
 const [from,to]=[+process.argv[2],+process.argv[3]]; const fps=30; const dir=process.argv[4]||'frames';
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1920,height:1080}});
 p.on('pageerror',e=>console.log('err',e.message));
 await p.goto('file://'+process.cwd()+'/index.html'); await p.waitForFunction('window.ready===true'); await p.evaluate(()=>document.fonts.ready);
 const list = process.argv[5] ? process.argv[5].split(',').map(Number) : null;
 const frames = list ? list.map(x=>Math.round(x*fps)) : Array.from({length:to-from},(_,i)=>from+i);
 for(const f of frames){ await p.evaluate(t=>window.renderAt(t),f/fps); await p.screenshot({path:`${dir}/f${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:90}); }
 await b.close();
})();
