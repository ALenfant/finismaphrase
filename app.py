from flask import Flask, request, jsonify

from sentence_completer import SentenceCompleter

app = Flask(__name__)
sentence_completer = SentenceCompleter()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/complete')
def complete():
    prefix = request.args.get('prefix')
    return sentence_completer.complete_sentence(prefix)


if __name__ == '__main__':
    app.run()
