''' Simple Python Flask based webserver which renders html pages and java script
'''
from flask import Flask, render_template

app = Flask(__name__) # Note we've used __name__ and hence cmd line we need to use SimpleServer as --app arg

@app.route("/")
def hello_world():
    return "<p>Index page!!</p>"

@app.route('/hello')
def hello():
    return 'Hello World'
# to run application run below command. It will start web server on http://127.0.0.1:5000.
# flask --app SimpleServer run
# If application python file name is app.py or wsgi.py then there is no need of cli --app 

# By adding env variabl FLASK_ENV=development we can run the web app in debug mode, which allows dynamically changing code.
# This will ensure there is no need to restart the server. Alternative is to use --debug cli
# Ex: flask --app SimpleServer run --debug

@app.route('/page')
def page():
    return render_template('index.html')   # Note: flask expect html page in template folder. Hence we need to store all html file in templates folder



@app.route('/<username>')
def greeting(username=None):
    ''' refer https://flask.palletsprojects.com/en/1.1.x/quickstart/ for more details'''
    return render_template('greeting.html', name=username)   # Note: flask expect html page in template folder. Hence we need to store all html file in templates folder