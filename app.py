from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "ok"}), 200

@app.route('/login', methods=['GET'], endpoint='login_page')
def login():
    return app.send_static_file('pages/login.html')

if __name__ == '__main__':
    app.run(debug=True)