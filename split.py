import soundfile as sf
import os
import json

with open("output.txt", "r", encoding="utf-8") as input_file:
    data = input_file.read()

data_json = json.loads(data)

sentences = data_json["Result"]["Sentences"]
extracted = [sentence["EndTime"] for sentence in sentences]
timepoints = []
for i in range(len(extracted)):
    timepoints.append(extracted[i]/1000)
#print(timepoints)

input_file = "audios/output_audio.wav"  
output_dir = "splited"     

def split_audio(input_file, output_dir, time_points):
    y, sr = sf.read(input_file)
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    
    segment = y[0:int(sr*time_points[0])]
    output_file = os.path.join(output_dir, f"segment_0.wav")
    sf.write(output_file, segment, sr)
    # 分割音频
    for i in range(len(time_points)-1):
        start = int(sr * time_points[i])  
        end = int(sr * time_points[i+1])    
        
        segment = y[start:end]
        
        output_file = os.path.join(output_dir, f"segment_{i+1}.wav")
        
        sf.write(output_file, segment, sr)


split_audio(input_file, output_dir, timepoints)