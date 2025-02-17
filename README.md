This project is used to recognize emotion and add according emoji at the end of each sentence.

The functions of each folder or file is as follows.

HCIproj/
│
├── alibabacloud-nls-python-sdk-dev/ This is Python SDK for NLS. It supports SPEECH-RECOGNIZER/SPEECH-SYNTHESIZER/SPEECH-TRANSLATOR/COMMON-REQUESTS-						    							     	PROTO. In this project, we use it to convert speech to text.
│   ├── transcription.py: This file is used to request for AliAPI to execute FileTrans for the certain audio file uploaded in AliOSS.
│   └── ...
│
├── audios/
│   ├── handling.py/ This is used to convert the sample rate of raw radio to the required 16000Hz.
│   ├── output_audio.wav/ audio file converted to designated sample rate.
│   └── sub-dir2/

├── emotion2vec/ This is a state-of-the-art speech emotion recognition foundation model.
│   ├── scripts/
│   │   └── test.py/ Invoke the model to recognize splited audio's emotions and store according scores.
│   ├── 2312.15185.pdf/ The essay of Emo2vec.

 |    └── ...

├── splitted/Target audios after splitting by sentences.
│   └── ...

├── uploads/ Produced by app.py, aiming to upload to the front end.
│   └── ...
├── app.py/ Allow users to upload audio files in the front end, process them, and return the processed result files.

├── command.cmd/ Command file to run the entire project with one click.

├── emoji.py/ Comparing the output emotion recognition scores with grading criterion scores, thus producing reasonable emojis.

├── emotion_grading.xlsx/ Grade the emotion gradients of the emojis.

├── final.txt/ The final output file.

├── index.html/ The front page code.

├── output.txt/ The output file of speech to text.

├── raw.m4a/ The original input audio file,

├── scores.txt/ The scores output by emo2vec of each splitted videos.

├── split.py/ Split audios into pieces by sentence.
└── upload.py/ Upload the converted audio to Ali's OSS.
