# HCIproj — Project Structure Documentation

This project is used to recognize emotion from speech and append corresponding emojis at the end of each sentence.

Below is an overview of each folder and file in the project.

```
HCIproj/
│
├── alibabacloud-nls-python-sdk-dev/
│   ├── transcription.py
│   └── ...
│
├── audios/
│   ├── handling.py
│   ├── output_audio.wav
│   └── sub-dir2/
│
├── emotion2vec/
│   ├── scripts/
│   │   └── test.py
│   ├── 2312.15185.pdf
│   └── ...
│
├── splitted/
│   └── ...
│
├── uploads/
│   └── ...
│
├── app.py
├── command.cmd
├── emoji.py
├── emotion_grading.xlsx
├── final.txt
├── index.html
├── output.txt
├── raw.m4a
├── scores.txt
├── split.py
└── upload.py
```

## Folder & File Descriptions

### 1. `alibabacloud-nls-python-sdk-dev/`
Python SDK for Aliyun NLS used for speech-to-text.

- `transcription.py`: Requests AliAPI to run FileTrans for audio stored in OSS.
- `...`: Other SDK files.

### 2. `audios/`
Audio preprocessing utilities.

- `handling.py`: Converts audio sample rate to 16000Hz.
- `output_audio.wav`: Converted audio output.
- `sub-dir2/`: Additional audio files.

### 3. `emotion2vec/`
State-of-the-art speech emotion recognition model.

- `scripts/test.py`: Runs model on split audio and outputs scores.
- `2312.15185.pdf`: Emo2vec paper.
- `...`

### 4. `splitted/`
Sentence-level split audio segments.

### 5. `uploads/`
Files produced by `app.py` to return to frontend.

### 6. Core Scripts
- `app.py`: Main backend to handle uploads and processing.
- `command.cmd`: One-click execution.
- `emoji.py`: Maps emotion scores to emojis.
- `split.py`: Splits audio by sentence.
- `upload.py`: Uploads processed audio to OSS.

### 7. Output & Data Files
- `emotion_grading.xlsx`: Scoring table.
- `final.txt`: Final output.
- `output.txt`: Speech-to-text results.
- `raw.m4a`: Original input file.
- `scores.txt`: Emotion scores per split audio.
