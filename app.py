#!/usr/bin/python3

import flask

app = flask.Flask(__name__)

LEN = 120

@app.route('/home')
def home():
    req = flask.request
    next_pram = int(req.args.get('next', 0))

    body = list(range(next_pram, min(LEN, next_pram + 20)))

    resp = flask.make_response(flask.jsonify(body))
    if next_pram + 20 < LEN:
        resp.headers['Link'] = '<http://localhost:34000/home?next={}>; rel="next";'.format(next_pram + 20)

    return resp, 200


app.run('0.0.0.0', port=34000, debug=True)
