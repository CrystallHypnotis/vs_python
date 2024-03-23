from flask import Flask, render_template, request

app = Flask(__name__, template_folder="static/htmls")

@app.route("/")
@app.route('/registration', methods=['POST', 'GET'])
def registration():
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
