from flask import Flask

app = Flask(video.ai)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if video.ai == '__main__':
    app.run(debug=True)