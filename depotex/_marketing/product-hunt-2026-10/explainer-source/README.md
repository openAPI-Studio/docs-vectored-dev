# Depotex explainer (narrated, illustrated): source

- `script.json`: narration lines by scene. `tts.py` reads them with Kokoro TTS (voice `am_michael`, offline; model files from github.com/thewh1teagle/kokoro-onnx releases) and writes `voice.wav` + `timeline.json` (convert to `tl.json`/`tl.js` with scene starts as in the thread).
- `anim.js`: every scene as an SVG drawn from time `t` (one function per scene in `S`). `rec.js` renders frames: `node rec.js 0 3750 frames`.
- `mix.py`: music bed, sound effects and voice with ducking (imports helpers from `synth_lib.py`; fix the path at its top).
- Encode: `ffmpeg -framerate 30 -i frames/f%05d.jpg -i mix_n.wav -c:v libx264 -crf 19 -pix_fmt yuv420p -c:a aac -shortest out.mp4`
