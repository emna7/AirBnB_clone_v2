#!/usr/bin/python3
"""
Defines return values for people requesting
various parts of my web app
"""
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<n>', strict_slashes=False)
def number_n(n):
    try:
        int(n)
        return '{} is a number'.format(n)
    except ValueError:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template_n(n):
    try:
        int(n)
        return render_template('5-number.html', n=n)
    except ValueError:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n):
    try:
        n = int(n)
        if (n % 2):
            label = 'odd'
        else:
            label = 'even'
        return render_template('6-number_odd_or_even.html', n=n, label=label)
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
