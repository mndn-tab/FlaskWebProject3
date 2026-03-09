"""

"""
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
# wsgi_app = app.wsgi_app

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/message")
def get_message():
    return jsonify({
        "message": "Hello from Flask backend!"
    })

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

