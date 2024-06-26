from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['guesses'] = 0
    
    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['guesses'] += 1
        if guess < session['number']:
            message = 'Too low!'
        elif guess > session['number']:
            message = 'Too high!'
        else:
            message = f'Correct! The number was {session["number"]}. It took you {session["guesses"]} guesses.'
            session.pop('number')
            session.pop('guesses')
            return render_template('index.html', message=message, show_form=False)
        
        return render_template('index.html', message=message, show_form=True)
    
    return render_template('index.html', show_form=True)

if __name__ == '__main__':
    app.run(debug=True)
