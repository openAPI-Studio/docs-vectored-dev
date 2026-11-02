# Tour video (voiceover): source

`lines.json` is one voiceover line per gallery image. `tts.py` reads them with Kokoro TTS (voice am_michael), `build.py` sizes each slide to its line, cross-fades the gallery images and mixes voice, music and transition sounds (needs the synth helpers from `../explainer-source/synth_lib.py`; fix the path at its top). Then:

    ffmpeg -i video.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac out.mp4
