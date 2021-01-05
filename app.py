from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test.html' )#return envoie la reponse

@app.route('/reponse_user', methods = ['POST'])
def reponse_user():
    if request.method == 'POST':
        data = request.form['fname']
        print(data)
        return "ok"


if __name__ == '__main__':
    app.run()