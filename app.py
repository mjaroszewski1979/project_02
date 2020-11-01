from flask import Flask, render_template, url_for,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/motto')
def motto():
    return render_template('motto.html')

@app.route('/form', methods=['POST'])
def form():
    name = request.form.get('name')
    return render_template('form.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)