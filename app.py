from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import subprocess

app = Flask(__name__)
CORS(app)  # 启用CORS

UPLOAD_FOLDER = 'uploads'
OUTPUT_FILE = 'output.txt'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def process_audio(input_path):
    try:
        # Log the beginning of the process
        print("Starting audio processing...")
        
        # Run each script step by step and log the output
        subprocess.run(['python', 'audios/handling.py'], check=True)
        print("Completed handling.py")
        
        subprocess.run(['python', 'upload.py'], check=True)
        print("Completed upload.py")
        
        with open('output.txt', 'w') as f:
            f.write("")
        with open('scores.txt', 'w') as f:
            f.write("")
        with open('final.txt', 'w') as f:
            f.write("")
        
        for file in os.listdir('splited'):
            file_path = os.path.join('splited', file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        print("Cleared splited directory")
        
        subprocess.run(['python', 'alibabacloud-nls-python-sdk-dev/transciption.py'], check=True)
        print("Completed transciption.py")
        
        subprocess.run(['python', 'split.py'], check=True)
        print("Completed split.py")
        
        subprocess.run(['python', 'emotion2vec/scripts/test.py'], check=True)
        print("Completed test.py")
        
        subprocess.run(['python', 'emoji.py'], check=True)
        print("Completed emoji.py")
        
        return 'final.txt'
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(error="No selected file"), 400

    if file and file.filename.endswith('.m4a'):
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)
        print(f"File saved to {input_path}")

        output_path = process_audio(input_path)
        if output_path and os.path.exists(output_path):
            with open(output_path, 'r', encoding='utf-8') as f:  # 指定编码为utf-8
                content = f.read()
            return jsonify(content=content)
        else:
            return jsonify(error="Failed to process audio"), 500

    return jsonify(error="Invalid file format"), 400

if __name__ == '__main__':
    app.run(debug=True)
