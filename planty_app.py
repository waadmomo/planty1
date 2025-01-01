from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Example plant data
plants = {
    'Fiddle Leaf Fig': {
        'watering_interval': 7,
        'last_watered': datetime.now() - timedelta(days=6),
        'tips': 'Place in bright, indirect light. Water when the top inch of soil is dry.'
    },
    'Snake Plant': {
        'watering_interval': 14,
        'last_watered': datetime.now() - timedelta(days=10),
        'tips': 'Tolerates low light. Water every 2-3 weeks, allowing the soil to dry out between waterings.'
    }
}

@app.route('/')
def index():
    return render_template('index.html', plants=plants)

@app.route('/water/<plant_name>')
def water_plant(plant_name):
    if plant_name in plants:
        plants[plant_name]['last_watered'] = datetime.now()
        flash(f'{plant_name} has been watered!', 'success')
    else:
        flash(f'Plant {plant_name} not found.', 'error')
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add_plant():
    name = request.form['name']
    interval = int(request.form['interval'])
    tips = request.form['tips']
    plants[name] = {
        'watering_interval': interval,
        'last_watered': datetime.now(),
        'tips': tips
    }
    flash(f'{name} has been added!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)