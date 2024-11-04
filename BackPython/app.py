from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def handler():
    word = request.args.get('world')
    return render_template('form.html', word=word)

