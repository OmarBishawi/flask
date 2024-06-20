from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return "Hello world!" 
@app.route('/dojo')
def dojo():
    return "dojo"


@app.route('/say/<name>')
def hello(name):
    print(name)
    return"hi " + name
@app.route('/repeat/<int:num>/<messege>')
def repeat_messege(num,messege):
    return messege*num
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.