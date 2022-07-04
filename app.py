from flask import Flask, render_template, request
import emoji
import random
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lang = request.form["language"]
        pw, metadata = generatePW(request.form["inputEmoji"], lang)
        return render_template("index.html", result=pw, em=request.form["inputEmoji"], metadata=metadata)
    elif request.method == 'GET':
        return render_template('index.html')


def generatePW(inputEmoji, lang):

    newPW = []
    metadata = []
    shortcodes = []
    for e in inputEmoji:
        if emoji.is_emoji(e):
            shortcode = getShortCode(e, lang)
            shortcodes.append(shortcode)
            unicode = emoji.replace_emoji(e, replace=unicode_escape)
            meta = {"emoji": e, "short": shortcode,
                    "unicode_clean": clean_unicode(unicode), "unicode": unicode, "lang": lang}
            metadata.append(meta)
            newPW.append(random.choice(shortcode))
    return upperLower(newPW), metadata


def getShortCode(input, lang):
    return emoji.demojize(input, language=lang)


def unicode_escape(chars, data_dict):
    return chars.encode('unicode-escape').decode()


def clean_unicode(code):
    return code[2:].lstrip("0")


def upperLower(pw):
    lst = [str.upper, str.lower]
    return ''.join(random.choice(lst)(c) for c in pw)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
