from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.form['search']:
        word = 'aesthetic ' + request.form['search']
        url = "https://api.giphy.com/v1/gifs/search?api_key=XHNvPi3vXM5WwbB2w5zWVvOGq6VsD3cK&limit=40&q=" + word
        giphy = requests.get(url)
        dataGiphy = giphy.json()
        return render_template('index.html', data = dataGiphy['data'])
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
