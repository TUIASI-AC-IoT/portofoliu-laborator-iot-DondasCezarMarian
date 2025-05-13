from flask import Flask, request, jsonify
import os
import glob
app = Flask(__name__)

FILES_DIR = 'D:\\SSC-2A\\Laborator12\\sensor'
os.makedirs(FILES_DIR, exist_ok=True)

@app.route("/")
def hello():
    return "Here you will have values of sensors."
@app.route("/sensor", methods=["GET"])
def list_dir():
    files = os.listdir(FILES_DIR)
    return jsonify(files)

@app.route('/sensor/<path:filename>', methods=["GET"])
def get_file_content(filename):
    search_pattern = os.path.join(FILES_DIR, f"{filename}.*")
    matching_files = glob.glob(search_pattern)
    if not matching_files:
        return jsonify({'error': 'File not found'}), 404

    matched_file = matching_files[0]
    try:
        with open(matched_file, 'r', encoding='utf-8') as f:
            content = f.read()
            return jsonify({
                'filename': os.path.basename(matched_file),
                'content': content
            })
    except Exception as e:
        return jsonify({'error': 'Server error', 'details': str(e)}), 500


if __name__ == "__main__":
    app.run()