from flask import Flask, render_template, request
from choose_restaurant import choose_restaurant, CUISINE_CODES

app = Flask(__name__)

@app.route('/')
def index():
    cuisines = sorted(CUISINE_CODES.keys())
    return render_template('index.html', cuisines=cuisines)

@app.route('/results', methods=['POST'])
def results():
    city = request.form['city']
    cuisine = request.form['cuisine']
    chosen_restaurant = choose_restaurant(city, cuisine)
    return render_template('results.html', restaurant=chosen_restaurant)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

