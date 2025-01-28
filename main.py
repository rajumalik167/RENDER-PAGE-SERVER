from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

PAGE_ACCESS_TOKEN = 'YOUR_PAGE_ACCESS_TOKEN'
VERIFY_TOKEN = 'YOUR_VERIFY_TOKEN'


# Webhook verification
@app.route('/webhook', methods=['GET'])
def verify():
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.verify_token') == VERIFY_TOKEN:
        return request.args['hub.challenge'], 200
    return 'Verification failed', 403


# Webhook to handle incoming messages
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Check if the message is from a user (not a page)
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                sender_id = messaging_event['sender']['id']
                if 'message' in messaging_event:
                    message = messaging_event['message']
                    text = message.get('text', '')  # Get text of the message

                    # Here you could add more logic to respond based on the message
                    if text:
                        send_message(sender_id, "Received your message: " + text)
    
    return 'OK', 200


# Function to send a message
def send_message(recipient_id, message_text):
    url = f'https://graph.facebook.com/v12.0/me/messages?access_token={PAGE_ACCESS_TOKEN}'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'recipient': {'id': recipient_id},
        'message': {'text': message_text}
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
