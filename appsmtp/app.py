
from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'dimovskimihso@gmail.com'
app.config['MAIL_PASSWORD'] = 'P@ssw0rd123456'

mail = Mail(app)

@app.route('/dockerhub-webhook', methods=['POST'])
def dockerhub_webhook():
    payload = request.json
    print("Received Docker Hub webhook:", payload)

    send_email(subject='Docker Image Pushed', body=str(payload))

    return 'OK'

def send_email(subject, body):
    msg = Message(subject, sender='dimovskimihso@gmail.com', recipients=['mihail.d.dimovski@gmail.com'])
    msg.body = body
    mail.send(msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

