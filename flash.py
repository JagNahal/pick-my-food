from flask import Flask, render_template
from main import choose_restaurant

app = Flask(__name__)

@app.route('/')
def home():
    try:
      restaurant = choose_restaurant()
      return render_template('index.html', my_restaurant=restaurant)
    except Exception as e:
      print(e)
      return render_template('index.html', my_restaurant="Something is wrong with the server, try again later")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)