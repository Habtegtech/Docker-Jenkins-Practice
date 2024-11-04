
from flask import Flask

app = Flask(__name__)

@app.route('/')  # Add the decorator here
def hello_world():
    return "Hello world"

if __name__ == "__main__":  # Correct the conditional name
    app.run(host='0.0.0.0', port=5000)
