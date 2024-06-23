from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html', x=8, y=8)

@app.route('/<int:x>/<int:y>')
def custom_checkerboard(x, y):
    return render_template('index.html', x=x, y=y)

if __name__ == '__main__':
    app.run(debug=True)
