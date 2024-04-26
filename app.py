from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def bird_gallery():
    page = request.args.get('page', 1, type=int)
    url = "https://aves.ninjas.cl/api/birds"
    response = requests.get(url)
    birds = response.json() if response.status_code == 200 else []
    return render_template('template.html', birds=birds, page=page)

if __name__ == '__main__':
    app.run(debug=True)