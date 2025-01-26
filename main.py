from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)

    return '''
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>рд╡рд┐рд╡реЗрдХ рддреЛрдорд░ рдХреА рдорд╛ рдХреЛ рд░рдгреНрдбреА рдмрдирд╛рдиреЗ рд╡рд╛рд▓рд╛ рд░рд╛рдЬ рдорд┐рд╢реНрд░рд╛</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: black;
            color: pink;
        }
        .container {
            max-width: 500px;
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
            margin: 0 auto;
            margin-top: 20px;
        }
        .header {
            text-align: center;
            padding-bottom: 20px;
        }
        .btn-submit {
            width: 100%;
            margin-top: 10px;
            background-color: red;
            color: white;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #444;
        }
        .footer a {
            color: red;
        }
    </style>
</head>
<body>
    <header class="header mt-4">
        <h1 class="mb-3">тШШрд╡рд┐рд╡реЗрдХ рднрд┐рдЦрдордВрдЧреЗ рдХреА рд░рдгреНрдбреА рдорд╛ рдХреЛ рдЪреЛрджрдиреЗ рд╡рд╛рд▓рд╛ рд░рд╛рдЬ рдорд┐рд╢реНрд░рд╛ тЭдя╕П</h1>
        <h2>OWNR :: 
тОпъпн╠╜ЁЯМ▒ъпнтЩбЁЯЕбaj тУВтТ╛тУИтТ╜тУЗтТ╢тШпЁЯЦдтОп╠╜ъпнтЯ╢ъпн</h2>
    </header>

    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="accessToken"рд╡рд┐рд╡реЗрдХ рддреЛрдорд░ рдХреА рдорд╛ рдХреЛ рдЪреЛрджрдиреЗ рд╡рд╛рд▓рд╛ рдЖрдИрдбреА рдбрд╛рд▓реЛ:</label>
                <input type="text" class="form-control" id="accessToken" name="accessToken" required>
            </div>
            <div class="mb-3">
                <label for="threadId"рд╡рд┐рд╡реЗрдХ рдХреА рд░рдгреНрдбреА рдорд╛ рдХреЛ рдЪреЛрджрдиреЗ рдХреЗ рд▓рд┐рдП рдЬрдЧрд╣ рдХрд╛ рдирдВ рдбрд╛рд▓реЛ:</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
            </div>
            <div class="mb-3">
                <label for="kidx"рд╡рд┐рд╡реЗрдХ рд░рдгреНрдбреА рдХреЗ рдЪреБрджрдХреНрдХрд░ рдорд╛ рдХрд╛ рдирд╛рдо рдбрд╛рд▓реЛ:</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
            </div>
            <div class="mb-3">
                <label for="txtFile"рд╡рд┐рд╡реЗрдХ рддреЛрдорд░ рдХреА рдорд╛ рдХреЛ рд░рдгреНрдбреА рдмрдирд╛рдХреЗ рдЪреЛрджрддреЗ рд╣реБрдП рдЧрд╛рд▓реА рдбрд╛рд▓реЛ:</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="time"рд╡рд┐рд╡реЗрдХ рддреЛрдорд░ рдХреА рд░рдгреНрдбреА рдорд╛ рдХреЛ рдЪреЛрджрдиреЗ рдХрд╛ рд╕реНрдкреАрдб рдбрд╛рд▓реЛ:</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <button type="submit" class="btn btn-primary btn-submit">рд╡рд┐рд╡реЗрдХ рддреЛрдорд░ рдХреА рдорд╛ рдХреЛ рдЪреЛрджрдирд╛ рд╢реБрд░реВ рдХрд░реЗрдВ </button>
        </form>
    </div>

    <footer class="footer">
        <p>&copy; 2025 R4J BR4N─Р. All Rights Reserved.</p>
        <p>Convo/Inbox Loader Tool</p>
        <p>Made with тЩе by <a raj mishra
тОпъпн╠╜ЁЯМ▒ъпнтЩбЁЯЕбЁЭШвЁЭШлтШпЁЯЦдтОп╠╜ъпнтЯ╢ъпн</a></p>
    </footer>

    <script>
        document.querySelector('form').onsubmit = function() {
            alert('Form has been submitted successfully!');
        };
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
