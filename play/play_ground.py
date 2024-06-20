from flask import Flask, render_template

app = Flask(__name__)

# Route to render three blue boxes
@app.route('/play')
def play():
    return render_template('play.html', times=3, color='blue')

# Route to render x boxes
@app.route('/play/<int:x>')
def play_x_times(x):
    return render_template('play.html', times=x, color='blue')

# Route to render x boxes of a specified color
@app.route('/play/<int:x>/<color>')
def play_x_times_color(x, color):
    return render_template('play.html', times=x, color=color)

if __name__ == '__main__':
    app.run(debug=True)
