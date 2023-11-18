from flask import Flask,render_template,request,abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def about():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)