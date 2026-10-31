const { chromium } = require('playwright');
(async()=>{
 const [from,to,fps]=[+process.argv[2],+process.argv[3],30];
 const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist','--allow-file-access-from-files']});
 const p=await b.newPage({viewport:{width:1920,height:1080}});
 p.on('console',m=>console.log('console',m.text())); p.on('pageerror',e=>console.log('err',e.message));
 await p.goto('file://'+process.cwd()+'/index.html'); await p.waitForFunction('window.ready===true',null,{timeout:60000});
 await p.evaluate(()=>document.fonts.ready);
 for(let f=from;f<to;f++){ await p.evaluate(t=>window.renderAt(t),f/fps); await p.screenshot({path:`frames/f${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:92}); }
 await b.close();
})();
