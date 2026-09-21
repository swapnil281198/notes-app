from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Simple Notes App</h1>
    <ul>
        <li>Learn Docker</li>
        <li>Learn Jenkins</li>
        <li>Learn Kubernetes</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
