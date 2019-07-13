import os

import requests
from flask import Flask, request

app = Flask(__name__)
LINE_ACCESS_TOKEN = os.environ.get("LINE_ACCESS_TOKEN")
LINE_NOTIFY_URL = "https://notify-api.line.me/api/notify"


def _line_request(message):
    response = requests.post(
        url=LINE_NOTIFY_URL,
        headers={'Authorization': f'Bearer {LINE_ACCESS_TOKEN}'},
        data={"message": message}
    )
    if response.status_code >= 400:
        return f"Error: {response.text}"
    return "Webhook received"


@app.route('/message', methods=['GET', 'POST'])
def line_test():
    message = request.args.get('q')
    if not message:
        return "Invalid request"
    return _line_request(message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7788, debug=True)

