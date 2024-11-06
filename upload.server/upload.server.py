import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Remove the MAX_CONTENT_LENGTH limit to support larger files
executor = ThreadPoolExecutor(max_workers=4)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Stream the file to the server
    with open(file_path, 'wb') as f:
        for chunk in file.stream:
            f.write(chunk)
    
    return jsonify({'filename': filename}), 201

@app.route('/files', methods=['GET'])
def list_files():
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file_size = os.path.getsize(file_path)
        files.append({'filename': filename, 'size': file_size})
    return jsonify(files), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
