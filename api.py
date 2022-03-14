from flask import Flask, render_template, request, redirect, url_for, send_from_directory

from common import helper

app = Flask(__name__,
            template_folder='template',
            static_url_path='',
            static_folder='links')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    filepath = "output/{}".format(uploaded_file.filename)
    link = "{}".format(uploaded_file.filename)
    if uploaded_file.filename != '':
        uploaded_file.save(filepath)
        helper.build_symlink(filepath, link)
    return redirect(url_for('/{}'.format(link)))

@app.route('/<path:filename>', methods=['GET'])
def fetch(filename):
    return send_from_directory(filename)
