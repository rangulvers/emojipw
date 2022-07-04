from flask import Flask, render_template, request
import emoji
import random
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lang = request.form["language"]
        pw, shortcodes = generatePW(request.form["inputEmoji"], lang)
        return render_template("index.html", result=pw, em=request.form["inputEmoji"], shortcodes=shortcodes)
    elif request.method == 'GET':
        return render_template('index.html')


def generatePW(inputEmoji, lang):
    lst = [str.upper, str.lower]
    newPWin = []
    shortcodes = []
    for e in inputEmoji:
        shortcode = getShortCode(e, lang)
        if shortcode.startswith(":"):
            shortcodes.append(shortcode)
            newPWin.append(random.choice(shortcode))
    return ''.join(random.choice(lst)(c) for c in newPWin), shortcodes


def getShortCode(input, lang):
    return emoji.demojize(input, language=lang)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
