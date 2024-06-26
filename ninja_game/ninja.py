# Import necessary libraries
from flask import Flask, render_template, redirect, request
import random

# Initialize Flask application
app = Flask(__name__)

# Secret key for session management (recommended for production)
app.secret_key = 'your_secret_key_here'

# Initialize global variable to store ninja's gold
# This should ideally be stored in a session or a database in real applications
ninja_gold = 0
activities = []

# Route for the main game page
@app.route('/')
def index():
    return render_template('index.html', ninja_gold=ninja_gold, activities=activities)

# Route to process the form submission and update ninja's gold
@app.route('/process_money', methods=['POST'])
def process_money():
    global ninja_gold
    global activities

    # Define locations and their respective earning ranges
    locations = {
        'farm': (10, 20),
        'cave': (5, 10),
        'house': (2, 5),
        'casino': (-50, 50)  # can lose up to 50 gold or gain up to 50 gold
    }

    # Get the location from the form submission
    location = request.form['building']

    # Calculate gold earned
    earnings_range = locations.get(location)
    if earnings_range:
        earnings = random.randint(earnings_range[0], earnings_range[1])
        ninja_gold += earnings

        # Log activity
        if earnings >= 0:
            activities.append(f'Earned {earnings} gold from the {location}!')
        else:
            activities.append(f'Entered a casino and lost {-earnings} gold... Ouch...')

    return redirect('/')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
