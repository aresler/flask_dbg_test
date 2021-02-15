from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    word = 'Hello'  # Put breakpoint here
    return render_template('index.html', word=word)


if __name__ == '__main__':
    app.run()
