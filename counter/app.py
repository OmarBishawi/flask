from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html', visits=session['visits'])

@app.route('/destroy_session')
def destroy_session():
    session.pop('visits', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
