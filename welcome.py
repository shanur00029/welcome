from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello nitin</h1>'
@app.route('/information')
def info():
    return '<h1>Friends Forever</h1>'
@app.route('/friend/<name>')
def friend(name):
    return '<h1>My friend name is {}</h1>'.format(name)

if __name__ == '__main__':
    app.run()