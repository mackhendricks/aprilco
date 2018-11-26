from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to AprilCo!'

@app.route('/backend-service')
def backend_service():
    return 'AprilCo Backend Services'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
