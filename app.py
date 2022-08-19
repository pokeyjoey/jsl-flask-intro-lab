rom flask import Flask
from flask import render_template
 
app = Flask(__name__, template_folder='views')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html') 

@app.route('/restaurants/<name>')
def show_player(name):
    return render_template('restaurantname.html', name=name) 

app.run(debug = True)
