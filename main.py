from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/new/')
def new():
    return 'New Page!'

if __name__ == '__main__':
    app.run()