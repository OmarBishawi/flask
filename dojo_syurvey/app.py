from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit_form():
    name = request.form['name']
    dojo_location = request.form['dojo_location']
    fav_language = request.form['fav_language']
    comment = request.form.get('comment', '')  # Optional comment

    return render_template("show.html", name=name, dojo_location=dojo_location,
    fav_language=fav_language, comment=comment)

if __name__ =="__main__":
    app.run(debug=True)
