import os
from flask import Flask, request

from send import load_list_of_people, send_sms_to_list


app = Flask('staroste')


@app.route('/send/', methods=['POST'])
def send():
    text = request.form['text']
    response_url = request.form['response_url']

    people = load_list_of_people(os.environ['CONTACTS'])
    send_sms_to_list(people, text)

    return 'ok'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
