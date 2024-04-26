from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://aves.ninjas.cl/api/birds"
    response = requests.get(url)
    birds = response.json() if response.status_code == 200 else []
    return render_template('template.html', birds=birds)

if __name__ == '__main__':
    app.run(debug=True)
