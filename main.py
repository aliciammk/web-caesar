from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <title>Web Caesar App</title>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method= "post">
            <label for="rot">Rotate by:</label>
                <input id="rot" type="text" name="rot" value="0"/>
            <label for="textarea">Type your message:</label>
                <textarea id="textarea" type="textarea" name="text">{0}</textarea>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>
"""



@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']

    encryption = rotate_string(text, rot)
    return form.format(encryption)


app.run()