from flask import Flask, render_template, request, send_from_directory, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route('/')
def upload_file_view():
    files = []
    for file in os.listdir('tmp'):
        if os.path.isfile('tmp/{}'.format(file)):
            files.append(file)
    return render_template('index.html', files=files)


@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('tmp/{}'.format(secure_filename(f.filename)))
        return redirect('/')


@app.route('/downloader/<filename>', methods=['GET'])
def download_file(filename):
    if request.method == 'GET':
        return send_from_directory('tmp', secure_filename(filename), as_attachment=True, cache_timeout=0)


@app.route('/delete/<filename>', methods=['GET'])
def delete_file(filename):
    if request.method == 'GET':
        files = []
        for file in os.listdir('tmp'):
            if os.path.isfile('tmp/{}'.format(file)):
                files.append(file)
        if filename in files:
            os.remove('tmp/{}'.format(secure_filename(filename)))

        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
