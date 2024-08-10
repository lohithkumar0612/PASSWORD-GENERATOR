from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

def generate_password(favorite_thing):
    # Create a base password with the favorite thing
    base_password = favorite_thing + ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
    # Shuffle the characters to make it less predictable
    password = ''.join(random.sample(base_password, len(base_password)))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    data = request.json
    favorite_thing = data.get('favoriteThing')
    password = generate_password(favorite_thing)
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True)
