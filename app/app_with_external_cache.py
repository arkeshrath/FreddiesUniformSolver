import time
import logging

from app.core.cache import Cache
from app.core.gridsolver import gridsolver
from app.utilities.helper import Helper
from app.utilities.cachehelper import CacheHelper
from app.controller.grid_controller import GridController
import os
from flask import Flask, flash, request, redirect, url_for, jsonify, render_template
from werkzeug.utils import secure_filename

# Setup static logger instance
# Improvement here, flush logs to storage for system analytics purposes.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize cache and grid logic
cache_instance = Cache()
cache_helper = CacheHelper()
grid_logic = gridsolver()
helper = Helper()

# Define the path to the 'uploads' directory
# In production we will point this to a cloud storage blob/container
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/process-file', methods=['GET', 'POST'])
def process_file():
    if request.method == 'POST' or request.method == 'GET':
        filename = request.json.get('filename')
        start_time = time.time()

        if not filename or not helper.allowed_file(filename):
            logger.warning("Filename is required or file extension is not accepted!")
            return jsonify({"error": "Filename is required"}), 400

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        if not os.path.exists(file_path):
            logger.warning("File not found: %s", filename)
            return jsonify({"error": "File not found"}), 404

        try:
            with open(file_path, 'r') as f:
                file_content = f.read()

            # Check for cache hits
            cache_key = helper.md5_hash(file_content)
            response = cache_helper.get(cache_key)
            if response:
                total_time = time.time() - start_time
                logger.info("Cache hit for filename: %s, now served the request in % seconds", filename, total_time)
                return jsonify({"message": "File uploaded and grid solved", "filename": filename, "solved": cache_helper.get(cache_key)})

            # Instantiate and solve grid
            grid_controller = GridController()
            status, grid, code = grid_controller.solve_grid(file_path)

            if code == 400:
                logger.warning(status)
                return jsonify({"error": status}), 400

            cache_helper.set(cache_key, grid)

            logger.info("File uploaded and solved grid for filename: %s", filename)
            return jsonify({"message": "File uploaded and grid solved", "filename": filename, "solved": grid})

        except Exception as e:
            logger.error("Error uploading file: %s", str(e))
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid request method"}), 405


@app.route('/ui/v1/uniform-finder', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and helper.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Perform a POST request to the new URL with the filename
            flash('Messages successfully uploaded')
            # List files in the upload folder

    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('upload_and_process.html', files=files)

@app.route('/delete-file', methods=['POST'])
def delete_file():
    data = request.get_json()
    filename = data.get('filename')
    if filename:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            return jsonify(message=f'File {filename} deleted successfully')
        return jsonify(message='File not found'), 404
    return jsonify(message='No filename provided'), 400

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
