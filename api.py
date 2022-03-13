from flask import Flask, render_template, request, redirect, url_for

from common import helper

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    filepath = "output/{}".format(uploaded_file.filename)
    if uploaded_file.filename != '':
        uploaded_file.save(filepath)
        helper.build_symlink(filepath, uploaded_file.filename)
    return redirect(url_for('index'))
