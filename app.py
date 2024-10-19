from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from main import algorithm

@app.route('/')
def home():
    return render_template('index.html')


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
    app.run(debug=True)