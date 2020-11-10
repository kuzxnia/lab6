from flask import Flask

app = Flask(__name__)
times = 0


@app.route('/')
def hello_world():
    global times
    times += 1
    return f'Hello, World! times={times}\n'


if __name__ == '__main__':
    app.run()
