import os
import requests
from base64 import b64encode
from urllib.parse import quote


def load_list_of_people(path):
    """
    Load a list of people from disk from a file which has on each line
    two values, separated by a comma: <name>, <phone number>
    """
    people = []
    with open(path, 'r') as f:
        for line in f:
            name, phone_number = line.split(',')
            name = name.strip()
            phone_number = phone_number.strip()
            people.append((name, phone_number))

    return people


def send_sms_to_list(people, message):
    """
    :param people: list of tuples (name, phone_number)
    """
    url = (
        'https://api.sendsms.ro/json?action=message_send&'
        'username={username}&'
        'password={token}&'
        'to={number}&'
        'text={message}&'
        'from=andrei'
    )

    success = 0
    error = 0
    for name, phone_number in people:
        text_to_send = (
            'Andrei si Oana | Salut {name}! ' + message
        ).format(name=name)

        response = requests.get(
            url.format(
                username=os.environ['SMS_USER'],
                token=os.environ['SMS_PASS'],
                number='4' + phone_number,
                message=quote(text_to_send)
            )
        )

        data = response.json()
        if data['message'] == 'Send':
            success += 1
        else:
            error += 1

    return success, error
