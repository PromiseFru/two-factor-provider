from flask import Flask

app = Flask(__name__)
    
if __name__ == '__name__':
    app.run(host='0.0.0.0', port=105)