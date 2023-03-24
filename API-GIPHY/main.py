from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Display everything with get
    if request.method == 'GET':
        return render_template('index.html')
    
    # Search Gif
    if request.form['search']:      # From the form input
        word = 'aesthetic ' + request.form['search']    # Add the aesthetic word for filter (You can remove it)
        # api_key= YOUR API KEY
        # limit= Number of gifs you want
        # q= word of search
        url = "https://api.giphy.com/v1/gifs/search?api_key=YOUR_API_KEY_HERE&limit=40&q=" + word 
        giphy = requests.get(url)   # Request
        dataGiphy = giphy.json()    # Json info obtained by API
        return render_template('index.html', data = dataGiphy['data']) # data - Parameter with the json data info to the HTML for loop
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
