from flask import Flask, render_template, request
import emoji
import random
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pw = generatePW(request.form["inputEmoji"])
        return render_template("index.html", result=pw, em=request.form["inputEmoji"])
    elif request.method == 'GET':
        return render_template('index.html')


def generatePW(inputEmoji):
    lst = [str.upper, str.lower]
    newPWin = []
    for e in inputEmoji:
        if emoji.demojize(e).startswith(":"):
            newPWin.append(random.choice(emoji.demojize(e)))
    return ''.join(random.choice(lst)(c) for c in newPWin)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
