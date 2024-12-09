from flask import Flask, render_template

# initalize the Flask app
app = Flask(__name__)

# define the index route 
@app.route('/')
def home():
    return render_template('index.html')

# run the app
if __name__ == '__main__':
    app.run(debug=True)