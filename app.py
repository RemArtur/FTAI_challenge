from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
import os
from main import algorithm, make_csv

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'sqlite'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#def allowed_file(filename):
#    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/db')
def db():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('db.html', files=files)

@app.route('/db/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('db'))

    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    make_csv(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    #if file.filename == '' or not allowed_file(file.filename):
    #    return redirect(url_for('db'))

    return redirect(url_for('db'))

@app.route('/db/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/api/data', methods=['POST'])
def handle_data():
    data = request.json
    users = data.get('users', [])
    biographies = data.get('biographies', [])
    posts = data.get('posts', [])
    friends = data.get('friends', [])
    groups = data.get('groups', [])
    photos = data.get('photos', [])
    types = algorithm(users, biographies, posts, friends, groups, photos)
    response = {
        "message": "Data received",
        "data": {
            "types": types
        }
    }
    return jsonify(response), 201

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)