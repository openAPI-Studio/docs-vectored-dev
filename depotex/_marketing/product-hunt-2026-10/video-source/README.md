# Vibe coding story video: source

`index.html` is a three.js scene; `window.renderAt(t)` draws second `t`. `rec.js` renders frames with Playwright:

    mkdir frames && node rec.js 0 1530      # 30 fps, 51 s
    ffmpeg -framerate 30 -i frames/f%05d.jpg -c:v libx264 -crf 18 -pix_fmt yuv420p out.mp4

Text and timings are at the top of `renderAt` (the `win(t, start, end)` calls) and in the HTML.

Soundtrack: `score.py` (numpy only) writes the original score, timed to the scenes; mux with

    ffmpeg -i video.mp4 -i soundtrack.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k out.mp4
