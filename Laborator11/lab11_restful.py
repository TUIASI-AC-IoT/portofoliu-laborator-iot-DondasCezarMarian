from flask import Flask, request, jsonify
import os

app = Flask(__name__)

FILES_DIR = 'D:\\SSC-2A\\files'
os.makedirs(FILES_DIR, exist_ok=True)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/files", methods=["GET"])
def list_dir():
    files = os.listdir(FILES_DIR)
    return jsonify(files)

@app.route('/files/<path:filename>', methods=['GET'])
def get_file_content(filename):
    filepath = os.path.join(FILES_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        return jsonify({'filename': filename, 'content': content})
    return jsonify({'error': 'File not found'}), 404
@app.route('/files', methods=['POST'])
def create_file_content(filename):
    filepath = os.path.join(FILES_DIR, filename)
    if os.path.exists(filepath):
        return jsonify({'filename': filename, 'content': content})
    else:
        data=request.json
        filename=data.get('filename')
        content=data.get('content','')
        with open(filepath,"w") as f:
            f.write(content)
        return jsonify({'message': f'File {filename} created successfully'})

if __name__ == "__main__":
    app.run()