from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Python Flask world v1.0"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

