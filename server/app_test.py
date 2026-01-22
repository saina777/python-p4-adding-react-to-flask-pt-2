from flask import Flask

app = Flask(__name__)

@app.route('/movies')
def movies():
    return "Hello World"

if __name__ == '__main__':
    app.run(port=5555)
