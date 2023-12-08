# line_notifier.py
import requests


def send_line_notification(message, image_path=None):
    # Set your LINE Notify access token
    token = "GPHKyqGFnz5cF00jwqn2U6sF1kiqXG0Yg2HjGWeTEGI"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "message": message
    }

    files = None
    if image_path:
        image = open(image_path, 'rb')
        files = {'imageFile': image}

    response = requests.post("https://notify-api.line.me/api/notify",
                             headers=headers, data=payload, files=files)

    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Message sending failed")
        print(response.text)
