from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Test5AWS</h1>'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
