import requests
import datetime
import json


class MailAutomation:
    def __init__(self):
        with open("./data/sample_config.json", "r") as f:
            self.api_key = json.load(f)["api_key"]

    def send(self, subject, text, recipient):
        """send a single message to a single recipient"""
        response = requests.post(
            "https://api.mailgun.net/v3/mailgun.kaid3n.me/messages",
            auth=("api", self.api_key),
            data={
                "from": "<mailgun@kaid3n.me>",
                "to": [recipient],
                "subject": subject,
                "text": text,
            },
        )
        return response

    def spam(self, subject, text):
        """send the same email to a bunch of people"""
        response = requests.post(
            "https://api.mailgun.net/v3/mailgun.kaid3n.me/messages",
            auth=("api", self.api_key),
            data={
                "from": "<mailgun@kaid3n.me>",
                "to": [
                    input("Recipient: ")
                    for _ in range(int(input("How many recipients?: ")))
                ],
                "subject": subject,
                "text": text,
            },
        )
        return response

    def attach(self, subject, text, attachment_path, recipient):
        """send a single image to a single recipient"""
        response = requests.post(
            "https://api.mailgun.net/v3/mailgun.kaid3n.me/messages",
            auth=("api", self.api_key),
            files=[("inline", open(attachment_path, "rb"))],
            data={
                "from": "<mailgun@kaid3n.me>",
                "to": recipient,
                "subject": subject,
                "text": text,
            },
        )
        return response

    def spam_attach(self, subject, text, attachment_path):
        """send the same attachment to a bunch of people"""
        response = requests.post(
            "https://api.mailgun.net/v3/mailgun.kaid3n.me/messages",
            auth=("api", self.api_key),
            files=[("inline", open(attachment_path, "rb"))],
            data={
                "from": "<mailgun@kaid3n.me>",
                "to": [
                    input("Recipient: ")
                    for _ in range(int(input("How many recipients?: ")))
                ],
                "subject": subject,
                "text": text,
            },
        )
        return response

    def send_scheduled(self, subject, text, recipient, date):
        """send email on a specific time; date format: MM DD hh:mm:ss"""
        date = datetime.datetime.strptime("2023 "+date, "%Y %m %d %H:%M:%S")
        date_string = datetime.datetime.strftime(date, "%A, %d %b %Y %H:%M:%S") + '-0000'
        return requests.post(
            "https://api.mailgun.net/v3/mailgun.kaid3n.me/messages",
            auth=("api", self.api_key),
            data={
                "from": "<mailgun@kaid3n.me>",
                "to": recipient,
                "subject": subject,
                "text": text,
                "o:deliverytime": date_string,
            },
        )
